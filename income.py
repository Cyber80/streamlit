import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json

# โหลด credentials จาก Streamlit Secrets
credentials_info = st.secrets["gcp_service_account"]
credentials = Credentials.from_service_account_info(credentials_info)

# เชื่อมต่อ Google Sheets
client = gspread.authorize(credentials)
#SHEET_URL = "https://docs.google.com/spreadsheets/d/xxxxxxxxxxxx/edit"
SHEET_URL ="https://docs.google.com/spreadsheets/d/1TgmPK6cF2uy1_yuctQQJBgp23hw5M8OD31JQ7AYemjo/edit"
spreadsheet = client.open_by_url(SHEET_URL)
sheet = spreadsheet.sheet1

# ดึงข้อมูลจาก Google Sheets
data = sheet.get_all_records()
df = pd.DataFrame(data)

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
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df.groupby("ประเภท")["จำนวนเงิน"].sum().plot(kind="bar", ax=ax, color=["green", "red"])
st.pyplot(fig)
