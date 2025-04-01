import pandas as pd

# Webスクレイピングで取得したデータをCSVファイルに保存するスクリプト
def run():
    # ダミーデータ（本来はselenium等で取得）
    data = [
        {'商品名': 'サンプル商品1', '価格': 1000},
        {'商品名': 'サンプル商品2', '価格': 1500},
    ]
    # データをDataFrameに変換
    df = pd.DataFrame(data)
    # 出力先のパスを指定
    output_path = './output/商品情報.csv'
    # CSVファイルとして保存
    df.to_csv(output_path, index=False)
    # 保存完了メッセージを表示
    print(f"📦 商品データを保存しました: {output_path}")
