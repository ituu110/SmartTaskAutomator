import schedule
import time

# サンプルタスク：定期実行される処理
def sample_task():
    print("⏰ 定期実行タスクが動作しました。")

# スケジューラのメイン処理
def run():
    print("🗓 スケジューラ起動中（サンプルタスク：5秒ごと）")
    # 5秒ごとにサンプルタスクを実行
    schedule.every(5).seconds.do(sample_task)

    # スケジューラを無限ループで実行
    try:
        while True:
            schedule.run_pending()  # 実行待ちタスクを処理
            time.sleep(1)  # CPU負荷を軽減するためのスリープ
    except KeyboardInterrupt:
        # ユーザーが停止した場合の処理
        print("🛑 スケジューラ停止")
