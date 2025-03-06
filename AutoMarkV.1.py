import time
import pyperclip
import streamlit as st

st.title("AutoMark V.1")
st.title("กรอกคะแนน SGS อัตโนมัติ บน Google Chrome")
st.write("1. เปิด App ผ่าน Browser อื่นเช่น Edge ")
st.write("2. เปิด sgs ใน Chrome (เปิดไว้หน้าต่างเดียว เปิดเยอะเดี๋ยวหาไม่เจอ) พร้อมทำเครื่องหมายถูก ในคอลัมน์ที่ต้องกรอกคะแนน ")
st.write("3. สำคัญ ต้องคลิกที่ช่องแรกไว้ ย้ำว่าช่องแรกต้องเป็นช่องว่าง ส่วนช่องถัดไปจะถูกแทนที่อัตโนมัติ ")
st.write("4. คัดลอกคะแนนจาก sheet ตามจำนวนคอลัมน์ที่ต้องกรอก และตามจำนวนคน ทำทีละห้องจำนวนคนจะตรงกัน")
st.write("5. กดปุ่ม 'เริ่มคัดลอกไปยัง SGS' เพื่อเริ่มการเติมข้อมูลจากคลิปบอร์ดไปยังช่อง Input ใน Google Chrome")  
st.write("6. ทำซ้ำข้อ 2-5 ตามต้องการ ")
st.write("############ ครูเจษฎา ชมเชย ############ ")

# ฟังก์ชั่นสำหรับการทำงาน
def autofill():
    # ดึงข้อมูลจาก Clipboard (ต้อง Copy ข้อมูลจาก Google Sheet มาก่อน)
    clipboard_data = pyperclip.paste()

    # แปลงข้อมูลเป็นแถวและคอลัมน์
    rows = clipboard_data.strip().split("\n")

    # เริ่มวางข้อมูลในช่องฟอร์ม
    for row in rows:
        columns = row.split("\t")  # แยกข้อมูลแต่ละคอลัมน์
        for cell in columns:
            pyperclip.copy(cell)  # คัดลอกข้อมูลแต่ละเซลล์
            # ที่นี่เราไม่สามารถใช้ GUI ได้แล้ว ดังนั้นสามารถใช้วิธีการวางข้อมูลผ่านฟอร์ม (ที่ไม่ได้ทำโดยอัตโนมัติใน Streamlit)
            st.text_input("กรอกข้อมูล", value=cell)  # แสดงช่องให้กรอกข้อมูล
            time.sleep(0.2)  # รอให้ระบบรับค่า

# ฟังก์ชั่นหลักในการสร้าง UI
def main(): 
    # ปุ่ม Start ที่จะเริ่มทำงาน
    if st.button("เริ่มคัดลอกไปยัง SGS"):
        st.info("กำลังเริ่มการกรอกคะแนน...")
        autofill()
        st.success("กรอกคะแนนเสร็จสิ้น..โปรดตรวจทานความถูกต้อง ")

if __name__ == "__main__":
    main()
