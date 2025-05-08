# おみくじアプリ Gradio MCP 開発タスク

## 目的
`app.py` を改修して、複数パターンのおみくじを提供する **Gradio MCP** アプリを構築する。

## タスク一覧

### 基本実装
- [x] 既存 `app.py` を置き換え／バックアップし、新規実装用に整理する
- [x] 伝統的な運勢のみを返す `draw_omikuji_basic` 関数を実装
- [x] ラッキーアイテム付き `draw_omikuji_lucky_item` 関数を実装
- [x] ラッキーカラー＆ナンバー付き `draw_omikuji_lucky_color_number` 関数を実装
- [x] 総合結果（恋愛・金運・健康 etc.）を返す `draw_omikuji_full` 関数を実装
- [x] 各関数に Docstring を追加（MCP スキーマ生成用）

### UI / MCP
- [x] 各関数に対応する `gr.Interface` を作成
- [x] `gr.TabbedInterface` で 4 つのタブを作成
- [x] `demo.launch(mcp_server=True)` で MCP エンドポイントを有効化

### ドキュメント
- [ ] `README.md` に「おみくじ」パートを追記（任意）
- [ ] 必要に応じて `gMaL.md` を更新（自動生成のままでも可）

### テスト・確認
- [ ] `python app.py` でローカル動作確認
- [ ] タブごとにクリックして結果が表示されることを確認
- [ ] `/gradio_api/mcp/sse` へ接続し、JSON スキーマに 4 つのツールが反映されていることを確認
