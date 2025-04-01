import os

# ファイル名を一括リネームする処理
def run():
    folder = './renamefiles'
    # 対象フォルダの存在確認
    if not os.path.exists(folder):
        print("⚠️ 対象フォルダが見つかりません。")
        return

    # フォルダ内のファイルを順番にリネーム
    for idx, filename in enumerate(os.listdir(folder), 1):
        old_path = os.path.join(folder, filename)
        new_name = f'renamed_file_{idx}.txt'
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)  # ファイル名を変更
        print(f'🔁 {filename} → {new_name}')
    # 処理完了メッセージを表示
    print("✅ ファイル名の一括リネーム完了")
