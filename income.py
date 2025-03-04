import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import matplotlib.pyplot as plt

# โหลด credentials จาก Streamlit Secrets
try:
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials_info = st.secrets["gcp_service_account"]
    credentials = Credentials.from_service_account_info(credentials_info, scopes=SCOPES)
except KeyError:
    st.error("❌ ไม่พบข้อมูล API Key! ตรวจสอบ secrets.toml ใน Streamlit Cloud")
    st.stop()

# เชื่อมต่อ Google Sheets
client = gspread.authorize(credentials)

# URL ของ Google Sheets
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TgmPK6cF2uy1_yuctQQJBgp23hw5M8OD31JQ7AYemjo/edit"

try:
    spreadsheet = client.open_by_url(SHEET_URL)
    sheet = spreadsheet.sheet1
    data = sheet.get_all_records()
except Exception as e:
    st.error(f"❌ ไม่สามารถโหลดข้อมูลจาก Google Sheets: {e}")
    st.stop()

# แปลงข้อมูลเป็น DataFrame
df = pd.DataFrame(data)

# ตรวจสอบว่ามีคอลัมน์ "จำนวนเงิน" และ "ประเภท" หรือไม่
if "จำนวนเงิน" not in df.columns or "ประเภท" not in df.columns:
    st.error("❌ ข้อมูลใน Google Sheets ไม่ถูกต้อง! ต้องมีคอลัมน์ 'จำนวนเงิน' และ 'ประเภท'")
    st.stop()

# แปลงคอลัมน์เป็นตัวเลข
df["จำนวนเงิน"] = pd.to_numeric(df["จำนวนเงิน"], errors="coerce")

# คำนวณรายรับ รายจ่าย และคงเหลือ
total_income = df[df["ประเภท"] == "รายรับ"]["จำนวนเงิน"].sum()
total_expense = df[df["ประเภท"] == "รายจ่าย"]["จำนวนเงิน"].sum()
balance = total_income - total_expense

# สร้าง Dashboard บน Streamlit
st.title("📊 Dashboard รายรับ-รายจ่าย")
st.metric(label="💰 รายรับทั้งหมด", value=f"{total_income:,.2f} บาท")
st.metric(label="📉 รายจ่ายทั้งหมด", value=f"{total_expense:,.2f} บาท")
st.metric(label="📌 คงเหลือ", value=f"{balance:,.2f} บาท")

# แสดงตารางข้อมูล
st.dataframe(df)

# สร้างกราฟ
fig, ax = plt.subplots()
df.groupby("ประเภท")["จำนวนเงิน"].sum().plot(kind="bar", ax=ax, color=["green", "red"])
st.pyplot(fig)
