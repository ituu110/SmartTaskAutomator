import os
import pandas as pd

def run():
    folder_path = './excel'
    output_path = './output/毎月の売上レポート.xlsx'

    if not os.path.exists(folder_path):
        print("⚠️ Excelフォルダが存在しません。")
        return

    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    if not files:
        print("⚠️ Excelファイルが見つかりません。")
        return
    data = [pd.read_excel(f) for f in files]
    df = pd.concat(data, ignore_index=True)

    summary = df.groupby('商品')['売上'].agg(['sum', 'mean']).reset_index()
    summary.columns = ['商品', '売上合計', '売上平均']
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    summary.to_excel(output_path, index=False)
    print(f"✅ Excelレポート出力完了: {output_path}")
