import time
import pyautogui
import pyperclip
import pygetwindow as gw
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
    # ค้นหาหน้าต่างที่มีคำว่า "Google Chrome"
    chrome_windows = [win for win in gw.getWindowsWithTitle("Google Chrome") if "Google Chrome" in win.title]

    if chrome_windows:
        chrome_window = chrome_windows[0]  # เลือกหน้าต่างแรกที่พบ
        chrome_window.restore()  # กู้คืนหน้าต่างหากถูกย่อขนาด
        chrome_window.activate()  # สลับไปที่หน้าต่าง Google Chrome
        time.sleep(1)  # หน่วงเวลาให้ Chrome พร้อมใช้งาน
    else:
        st.error("❌ ไม่พบหน้าต่าง Google Chrome")
        return

    # ดึงข้อมูลจาก Clipboard (ต้อง Copy ข้อมูลจาก Google Sheet มาก่อน)
    clipboard_data = pyperclip.paste()

    # แปลงข้อมูลเป็นแถวและคอลัมน์
    rows = clipboard_data.strip().split("\n")

    # เริ่มวางข้อมูลใน Chrome
    for row in rows:
        columns = row.split("\t")  # แยกข้อมูลแต่ละคอลัมน์
        for cell in columns:
            pyperclip.copy(cell)  # คัดลอกข้อมูลแต่ละเซลล์
            pyautogui.hotkey("ctrl", "v")  # วางข้อมูลลงฟอร์ม
            time.sleep(0.2)  # รอให้ Chrome รับค่า
            pyautogui.press("tab")  # กด Tab เพื่อเลื่อนไปช่องถัดไป
        #pyautogui.press("enter")  # กด Enter เพื่อขึ้นบรรทัดใหม่
        #time.sleep(0.2)

# ฟังก์ชั่นหลักในการสร้าง UI
def main(): 
    # ปุ่ม Start ที่จะเริ่มทำงาน
    if st.button("เริ่มคัดลอกไปยัง SGS"):
        st.info("กำลังเริ่มการกรอกคะแนน...")
        autofill()
        st.success("กรอกคะแนนเสร็จสิ้น..โปรดตรวจทานความถูกต้อง ")


if __name__ == "__main__":
    main()
