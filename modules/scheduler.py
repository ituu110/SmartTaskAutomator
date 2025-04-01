import schedule
import time

def sample_task():
    print("⏰ 定期実行タスクが動作しました。")

def run():
    print("🗓 スケジューラ起動中（サンプルタスク：5秒ごと）")
    schedule.every(5).seconds.do(sample_task)

    # 実行を止めない限り回り続ける
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 スケジューラ停止")
