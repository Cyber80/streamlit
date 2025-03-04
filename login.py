'''
import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    password = st.text_input("กรอกรหัสผ่าน", type="password")
    if password == "1234":
        st.session_state.logged_in = True
        st.experimental_rerun()
    else:
        st.warning("รหัสผ่านไม่ถูกต้อง")
else:
    st.success("เข้าสู่ระบบสำเร็จ!")
'''
import streamlit as st

# ฟังก์ชันสำหรับแสดงเมนู
def show_menu():
    st.sidebar.title("📌 เมนู")
    menu = ["p1", "p2", "p3", "p4", "p5"]
    page = st.sidebar.radio("เลือกหน้า", menu)
    return page

# ฟังก์ชันสำหรับตรวจสอบการล็อกอิน
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔑 ระบบล็อกอิน")
        username = st.text_input("👤 Username", key="username")
        password = st.text_input("🔒 Password", type="password", key="password")

        if st.button("เข้าสู่ระบบ"):
            if username == "user" and password == "1234":
                st.session_state.logged_in = True
                st.session_state.page = "p1"  # ไปที่หน้าแรกหลังล็อกอิน
                st.experimental_rerun()
            else:
                st.error("❌ Username หรือ Password ไม่ถูกต้อง")

    return st.session_state.logged_in

# เช็คการล็อกอิน
if check_login():
    # แสดงเมนูด้านข้าง
    page = show_menu()

    # แสดงเนื้อหาตามหน้า
    st.title(f"📄 หน้าปัจจุบัน: {page}")

    st.write("🔗 ไปยังหน้าอื่น:")
    for p in ["p1", "p2", "p3", "p4", "p5"]:
        if p != page:
            st.markdown(f"- [{p}](?page={p})", unsafe_allow_html=True)

    # อัปเดต state ของหน้าปัจจุบัน
    if "page" in st.query_params:
        st.session_state.page = st.query_params["page"]
    else:
        st.session_state.page = page

