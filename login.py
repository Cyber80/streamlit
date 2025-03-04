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
