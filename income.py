import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# ตั้งค่า OAuth Scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# โหลด credentials จาก Streamlit Secrets
try:
    credentials_info = st.secrets["gcp_service_account"]
    credentials = Credentials.from_service_account_info(credentials_info, scopes=SCOPES)
    st.success("✅ เชื่อมต่อ Google API สำเร็จ!")
except KeyError:
    st.error("❌ ไม่พบข้อมูล API Key! ตรวจสอบ secrets.toml ใน Streamlit Cloud")
    st.stop()
except Exception as e:
    st.error(f"❌ เกิดข้อผิดพลาดในการโหลด Credentials: {e}")
    st.stop()

# เชื่อมต่อ Google Sheets
client = gspread.authorize(credentials)

# URL ของ Google Sheets
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TgmPK6cF2uy1_yuctQQJBgp23hw5M8OD31JQ7AYemjo/edit?gid=0#gid=0"

try:
    spreadsheet = client.open_by_url(SHEET_URL)
    sheet = spreadsheet.sheet1
    data = sheet.get_all_records()
  #  df = pd.DataFrame(data)
    st.success("✅ โหลดข้อมูลจาก Google Sheets สำเร็จ!")
except Exception as e:
    st.error(f"❌ ไม่สามารถโหลดข้อมูลจาก Google Sheets: {e}")
    st.stop()

# แสดงข้อมูล
st.dataframe(df)
