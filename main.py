from modules import excel_aggregator, mail_sender, web_scraper, scheduler
from modules import get_file_renamer

# ファイルリネームモジュールを動的に取得
file_renamer = get_file_renamer()

# アプリケーションのエントリーポイント
def main():
    print("=== SmartTask Automator 起動 ===")
    # 各機能を必要に応じて呼び出し
    excel_aggregator.run()  # Excel集計処理
    mail_sender.run()  # メール送信処理
    file_renamer.run()  # ファイルリネーム処理
    web_scraper.run()  # スクレイピング処理
    scheduler.run()  # スケジューラ処理

# スクリプトが直接実行された場合にmain関数を呼び出す
if __name__ == '__main__':
    main()
