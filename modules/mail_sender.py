import smtplib
from email.message import EmailMessage
import os
import yaml

# メール送信処理
def run():
    # 設定ファイルからメールアカウント情報を取得
    with open('./config/settings.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    sender = config['email'].get('user')
    password = config['email'].get('password')
    recipient = config['email'].get('recipient')
    smtp_server = config['email'].get('smtp_server', 'smtp.gmail.com')
    smtp_port = config['email'].get('smtp_port', 465)
    attachment_path = './output/毎月の売上レポート.xlsx'

    # 必須情報の確認
    if not sender or not password:
        print("⚠️ メールアカウント情報が設定されていません。")
        return

    # 添付ファイルの存在確認
    if not os.path.exists(attachment_path):
        print("⚠️ 添付ファイルが見つかりません。")
        return

    # メールメッセージの作成
    msg = EmailMessage()
    msg['Subject'] = '売上レポート'
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content('売上レポートを送付いたします。')

    # 添付ファイルを追加
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(f.name)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # SMTPサーバーを使用してメールを送信
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
            smtp.login(sender, password)  # ログイン
            smtp.send_message(msg)  # メール送信
        print("✅ メール送信完了")
    except smtplib.SMTPAuthenticationError:
        print("⚠️ 認証エラー: メールアカウント情報を確認してください。")
    except Exception as e:
        print(f"⚠️ メール送信中にエラーが発生しました: {e}")
