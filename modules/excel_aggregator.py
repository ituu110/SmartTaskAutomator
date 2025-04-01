import os
import pandas as pd

# Excelファイルを集計し、レポートを作成する処理
def run():
    folder_path = './excel'
    output_path = './output/毎月の売上レポート.xlsx'

    # 入力フォルダの存在確認
    if not os.path.exists(folder_path):
        print("⚠️ Excelフォルダが存在しません。")
        return

    # フォルダ内のExcelファイルを取得
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    if not files:
        print("⚠️ Excelファイルが見つかりません。")
        return

    # 各Excelファイルを読み込み、データを結合
    data = [pd.read_excel(f) for f in files]
    df = pd.concat(data, ignore_index=True)

    # 商品ごとの売上合計と平均を計算
    summary = df.groupby('商品')['売上'].agg(['sum', 'mean']).reset_index()
    summary.columns = ['商品', '売上合計', '売上平均']

    # 出力フォルダを作成し、結果をExcelに保存
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    summary.to_excel(output_path, index=False)
    # 処理完了メッセージを表示
    print(f"✅ Excelレポート出力完了: {output_path}")
