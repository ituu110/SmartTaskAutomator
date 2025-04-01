from modules import excel_aggregator, mail_sender, web_scraper, scheduler
from modules import get_file_renamer

file_renamer = get_file_renamer()

def main():
    print("=== SmartTask Automator 起動 ===")
    # 各機能を必要に応じて呼び出し
    excel_aggregator.run()
    mail_sender.run()
    file_renamer.run()
    web_scraper.run()
    scheduler.run()

if __name__ == '__main__':
    main()
