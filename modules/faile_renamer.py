import os

def run():
    folder = './rename対象'
    if not os.path.exists(folder):
        print("⚠️ 対象フォルダが見つかりません。")
        return

    for idx, filename in enumerate(os.listdir(folder), 1):
        old_path = os.path.join(folder, filename)
        new_name = f'renamed_file_{idx}.txt'
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f'🔁 {filename} → {new_name}')
    print("✅ ファイル名の一括リネーム完了")
