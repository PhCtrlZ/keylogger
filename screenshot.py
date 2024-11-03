import pyautogui
import time
from datetime import datetime

def take_screenshot():
    """Hàm chụp và lưu một bức ảnh màn hình."""
    # Tạo tên file theo thời gian hiện tại để tránh bị ghi đè
    file_name = datetime.now().strftime("D:\\keylogger\\screenshot\\screenshot_%Y%m%d_%H%M%S.png")
    
    # Chụp màn hình và lưu ảnh
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)
    
    print(f"Screenshot saved as {file_name}")

def auto_screenshot():
    """Hàm điều chỉnh thời gian chụp và tự động chụp màn hình."""
    # Hỏi người dùng khoảng thời gian giữa các lần chụp (tính bằng giây)
    interval = float(input("Nhập khoảng thời gian giữa các lần chụp màn hình (giây): "))
    
    # Hỏi người dùng số lần chụp
    num_shots = int(input("Nhập số lần chụp màn hình: "))
    
    # Vòng lặp chụp màn hình theo số lần và khoảng thời gian đã nhập
    for i in range(num_shots):
        print(f"Chụp màn hình lần {i + 1}...")
        take_screenshot()  # Gọi hàm chụp màn hình
        
        # Chờ khoảng thời gian do người dùng nhập trước khi chụp lần tiếp theo
        time.sleep(interval)

# Chạy hàm auto_screenshot để thực hiện chụp màn hình
auto_screenshot()
