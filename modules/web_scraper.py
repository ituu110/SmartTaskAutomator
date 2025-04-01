import pandas as pd

def run():
    # ダミーデータ（本来はselenium等で取得）
    data = [
        {'商品名': 'サンプル商品1', '価格': 1000},
        {'商品名': 'サンプル商品2', '価格': 1500},
    ]
    df = pd.DataFrame(data)
    output_path = './output/商品情報.csv'
    df.to_csv(output_path, index=False)
    print(f"📦 商品データを保存しました: {output_path}")
