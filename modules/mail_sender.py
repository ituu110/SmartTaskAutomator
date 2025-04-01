import smtplib
from email.message import EmailMessage
import os

def run():
    sender = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')
    recipient = 'example@example.com'
    attachment_path = './output/毎月の売上レポート.xlsx'

    if not os.path.exists(attachment_path):
        print("⚠️ 添付ファイルが見つかりません。")
        return

    msg = EmailMessage()
    msg['Subject'] = '売上レポート'
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content('売上レポートを送付いたします。')

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(f.name)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("✅ メール送信完了")
