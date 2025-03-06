import time
import pyautogui
import pyperclip
import pygetwindow as gw

# ค้นหาหน้าต่าง Google Chrome
chrome_windows = [win for win in gw.getWindowsWithTitle("Google Chrome") if win.isActive or win.isMinimized]

if chrome_windows:
    chrome_window = chrome_windows[0]  # เลือกหน้าต่างแรกที่พบ
    chrome_window.restore()  # กู้คืนหน้าต่างหากถูกย่อขนาด
    chrome_window.activate()  # สลับไปที่หน้าต่าง Chrome
    time.sleep(1)  # หน่วงเวลาให้ Chrome พร้อมใช้งาน
else:
    print("❌ ไม่พบหน้าต่าง Google Chrome")
    exit()

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
        time.sleep(0.3)  # รอให้ Chrome รับค่า
        pyautogui.press("tab")  # กด Tab เพื่อเลื่อนไปช่องถัดไป
    #pyautogui.press("enter")  # กด Enter เพื่อขึ้นบรรทัดใหม่
    #time.sleep(0.2)
