# SmartTask Automator - 業務効率化アプリケーション 要件定義書

## 1. アプリ名（仮）
**SmartTask Automator（スマートタスク・オートメーター）**

---

## 2. 背景・目的  
日々のルーチンタスク（例：データ整理、ファイル操作、メール送信など）をPythonで自動化し、作業時間の短縮とヒューマンエラーの削減を目的とする。  
特に中小企業や個人事業主にとって有用なツールを目指す。

---

## 3. 主な機能一覧

| 機能名 | 概要 |
|--------|------|
| **① Excel自動処理** | 指定フォルダのExcelファイルを集計・加工し、レポートを作成。 |
| **② メール自動送信** | 添付ファイル付きでメールを一括送信（Gmail/Outlook対応）。 |
| **③ ファイル名一括リネーム** | 条件に基づきフォルダ内のファイル名を一括変更。 |
| **④ スクレイピング収集** | 指定サイト（例：楽天、Amazonなど）から商品情報を取得しExcel出力。 |
| **⑤ タスクスケジューラ** | 上記処理を日時指定で自動実行。 |

---

## 4. ターゲットユーザー
- 企業の事務職・総務
- 小規模事業者
- フリーランス（特にeコマース、営業職）

---

## 5. 非機能要件
- **操作性**：CLIまたはシンプルなGUI（Tkinter/PyQt）で直感的に操作できる  
- **環境**：Windows対応（Python 3.10 以上）  
- **保守性**：設定ファイル（.ini/.yaml）による柔軟なカスタマイズ  
- **セキュリティ**：メール送信時はパスワードを平文で保存しない（例：環境変数や暗号化）

---

## 6. 使用技術（予定）
- Python（pandas / openpyxl / schedule / selenium / tkinter or PyQt / smtplib）
- 外部API（Google Sheets APIなども検討）

---

## 7. 成果物・アウトプット例
- 「毎月の売上レポート.xlsx」が自動作成され、営業チームにメール配信される  
- 毎週月曜9時に指定のECサイトから最新商品情報がCSVで保存される  

---

## 8. 開発スケジュール（例）

| フェーズ | 期間（目安） | 内容 |
|----------|---------------|------|
| 要件定義・設計 | 1週間 | 上記のような仕様確定 |
| 実装（基本機能） | 2〜3週間 | Excel操作・メール送信など |
| 実装（拡張＋スケジューラ） | 1〜2週間 | スクレイピング、定期実行など |
| テスト・改善 | 1週間 | ユースケースで動作確認 |
| README・ポートフォリオ反映 | 1週間 | GitHub整理、紹介資料作成 |

---

## 備考
- 実行時にエラーが出た場合のログ出力、通知機能の追加も今後の課題として検討する。
- 業務現場でのニーズに応じて機能の取捨選択が可能なモジュール構成を想定。
