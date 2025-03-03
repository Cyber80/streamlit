import streamlit as st
import pandas as pd
import numpy as np

# ตั้งค่าชื่อ Dashboard
st.title("📊 My First Streamlit Dashboard")

# เพิ่ม Sidebar
st.sidebar.header("🔧 ตัวเลือก")
option = st.sidebar.selectbox("เลือกข้อมูลที่ต้องการดู", ["Random Data", "Sine Wave"])

# สร้างข้อมูลตัวอย่าง
if option == "Random Data":
    df = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
    st.write("### 📌 Random Data Table")
    st.dataframe(df)
    st.line_chart(df)

elif option == "Sine Wave":
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    st.write("### 🌊 Sine Wave")
    st.line_chart({"x": x, "sin(x)": y})

# Input text & button
name = st.text_input("กรอกชื่อของคุณ")
if st.button("ส่งข้อมูล"):
    st.success(f"ยินดีต้อนรับ {name} 🎉")
