# Gradio MCP の サンプルリポジトリ: gradio-mcp-codex-template

```plaintext
OS: posix
Directory: /root/prj/gradio-mcp-codex-template

├── .github/
│   └── workflows/
│       └── sync-to-hf.yml
├── .env.example
├── .SourceSageignore
├── app.py
├── gMaL.md
├── README.md
└── requirements.txt
```

## 📂 Gitリポジトリ情報

### 🌐 基本情報

- 🔗 リモートURL: https://github.com/Sunwood-ai-labs/gradio-mcp-codex-template.git
- 🌿 デフォルトブランチ: main
- 🎯 現在のブランチ: main
- 📅 作成日時: 2025-05-07 13:02:45
- 📈 総コミット数: 1

### 🔄 最新のコミット

- 📝 メッセージ: Initial commit
- 🔍 ハッシュ: 1fe9b6d7
- 👤 作者: Maki (108736814+Sunwood-ai-labs@users.noreply.github.com)
- ⏰ 日時: 2025-05-07 12:58:07

### 👥 主要コントリビューター

| 👤 名前 | 📊 コミット数 |
|---------|-------------|
| Maki | 1 |

## 📊 プロジェクト統計

- 📅 作成日時: 2025-05-07 13:06:43
- 📁 総ディレクトリ数: 2
- 📄 総ファイル数: 7
- 📏 最大深度: 2
- 📦 最大ディレクトリ:  (9 エントリ)

### 📊 ファイルサイズと行数

| ファイル | サイズ | 行数 | 言語 |
|----------|--------|------|------|
| README.md | 4.5 KB | 138 | markdown |
| app.py | 2.5 KB | 107 | python |
| .SourceSageignore | 691.0 B | 54 | plaintext |
| .github/workflows/sync-to-hf.yml | 605.0 B | 22 | yaml |
| .env.example | 347.0 B | 12 | plaintext |
| requirements.txt | 154.0 B | 6 | plaintext |
| gMaL.md | 0.0 B | 0 | markdown |
| **合計** |  | **339** |  |

### 📈 言語別統計

| 言語 | ファイル数 | 総行数 | 合計サイズ |
|------|------------|--------|------------|
| markdown | 2 | 138 | 4.5 KB |
| python | 1 | 107 | 2.5 KB |
| plaintext | 3 | 72 | 1.2 KB |
| yaml | 1 | 22 | 605.0 B |

`.SourceSageignore`

**サイズ**: 691.0 B | **行数**: 54 行
```plaintext
# バージョン管理システム関連
.git/
.gitignore

# キャッシュファイル
__pycache__/
.pytest_cache/
**/__pycache__/**
*.pyc

# ビルド・配布関連
build/
dist/
*.egg-info/

# 一時ファイル・出力
output/
output.md
test_output/
.SourceSageAssets/
.SourceSageAssetsDemo/

# アセット
*.png
*.svg
*.jpg
*.jepg
assets/

# その他
LICENSE
example/
package-lock.json
.DS_Store

# 特定のディレクトリを除外
tests/temp/
docs/drafts/

# パターンの例外（除外対象から除外）
!docs/important.md
!.github/workflows/
repository_summary.md

# Terraform関連
.terraform
*.terraform.lock.hcl
*.backup
*.tfstate

# Python仮想環境
venv
.venv
```

`.env.example`

**サイズ**: 347.0 B | **行数**: 12 行
```plaintext
### .env.example
# 環境変数のサンプルファイル

# OpenAI APIキー
OPENAI_API_KEY=your_openai_api_key

# GitHub APIトークン（省略可: GitHub Actionsでは自動で提供されます）
GITHUB_TOKEN=your_github_token

# Codex挙動の設定
# 静粛モード: 1 に設定すると余分なログ出力を抑制
CODEX_QUIET_MODE=1
```

`README.md`

**サイズ**: 4.5 KB | **行数**: 138 行
```markdown
---
title: Gradio MCP Minimal
emoji: 🌍
colorFrom: blue
colorTo: blue
sdk: gradio
sdk_version: 5.26.0
app_file: app.py
pinned: false
---

<div align="center">

![Image](https://github.com/user-attachments/assets/89233e89-d2e4-4e29-b1b8-fc5c90a7e4b2)


# 🚀 **Gradio MCP Minimal**

<p align="center">
  <a href="https://www.python.org">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white">
  </a>
  <a href="https://www.gradio.app">
    <img alt="Gradio" src="https://img.shields.io/badge/Gradio-5.26.0-orange?logo=gradio">
  </a>
  <a href="https://github.com/makiai/gradio-mcp-minimal/blob/main/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green">
  </a>
  <a href="https://github.com/makiai/gradio-mcp-minimal/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/makiai/gradio-mcp-minimal?style=social">
  </a>
<a href="https://huggingface.co/spaces/MakiAi/gradio-mcp-minimal">
    <img alt="HF Spaces" src="https://img.shields.io/badge/Spaces-Live%20Demo-blueviolet?logo=huggingface&logoColor=white">
  </a>
</p>
</div>

## ✨ 概要
このリポジトリは **最小構成** で Gradio アプリを立ち上げ、同時に **MCP (Model Context Protocol) サーバー** として機能させるサンプルです。  
たった 1 つのファイルを実行するだけで、Web UI と MCP SSE エンドポイントの両方が手に入ります。

## 📄 ファイル構成
| ファイル / ディレクトリ | 役割 |
|------------------------|------|
| `app.py`               | Gradio UI + MCP サーバー（`letter_counter` ツール） |
| `requirements.txt`     | 依存パッケージ（`gradio[mcp]` のみ） |
| `assets/header.svg`    | README 用ヘッダー画像（任意） |

## 📦 セットアップ

### 🚀 uv を使ったクイックスタート（推奨）

```bash
# 仮想環境の作成
uv venv
# 仮想環境の有効化
source .venv/bin/activate
# 依存インストール
uv pip install -r requirements.txt
```

### 🐍 標準 pip のみで実行したい場合

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🚀 実行
以下のコマンドを実行でローカルサーバーが起動します。
```bash
python app.py
```

- Web UI: <http://127.0.0.1:7860>  
- MCP SSE エンドポイント: <http://127.0.0.1:7860/gradio_api/mcp/sse>  
  - UI フッター → **View API** → **MCP** をクリックすると、コピペ可能な設定 JSON が表示されます。

## ⚙️ MCP クライアント設定例
Claude Desktop / Cline などで `claude_desktop_config.json` 等に追記:
```jsonc
{
  "mcpServers": {
    "gradio-local": {
      "url": "http://127.0.0.1:7860/gradio_api/mcp/sse"
    }
  }
}
```
クライアントを再起動すると `letter_counter` ツールが利用できるようになります 🎉

## 🔧 仕組み
```python
demo.launch(mcp_server=True)
```
この 1 行で Gradio アプリが SSE ベースの MCP サーバーとして動作します。  
ドキュストリングと型ヒントから自動でスキーマが生成されます。

## 🌠 拡張方法
1. `app.py` に関数を追加し、適切なドキュストリングを記述  
2. `Interface(...)` へ登録（または Blocks を使用）  
3. 再起動すれば新しい MCP ツールとして自動公開

## 🛫 🤗 Spaces へ無料デプロイ
ファイル一式を Hugging Face Spaces (Gradio テンプレート) へプッシュすると、無料の公開 MCP サーバーになります:
```
https://<your-space>.hf.space/gradio_api/mcp/sse
```
例）`https://makiai-gradio-mcp-minimal.hf.space/gradio_api/mcp/sse`

## 🔗 MCP クライアント設定例 (Spaces)

Spaces で公開したサーバーを **MCP クライアント（Claude Desktop / Cline など）** から呼び出す手順です。

1. **エンドポイント URL**
   ```
   https://<your-space>.hf.space/gradio_api/mcp/sse
   ```
   例）`https://makiai-gradio-mcp-minimal.hf.space/gradio_api/mcp/sse`

2. **config 追記例** (`claude_desktop_config.json` 等)
   ```jsonc
   {
     "mcpServers": {
       "gradio-space": {                // 任意の名前
         "url": "https://makiai-gradio-mcp-minimal.hf.space/gradio_api/mcp/sse"
       }
     }
   }
   ```

3. **動作確認**
   クライアントを再起動 → Tool Palette で `server = gradio-space` を選択 →
   `letter_counter` ツールに `text: "hello"` を送信し、`length: 5` が返れば接続完了です 🎉

## 📝 ライセンス
MIT
```

`app.py`

**サイズ**: 2.5 KB | **行数**: 107 行
```python
import numpy as np
import gradio as gr
import qrcode
from PIL import Image
import io  # Added for parity with user-provided snippet (currently unused)


def reverse_text(text):
    """
    テキストを反転する。

    Args:
        text (str): 反転したいテキスト。

    Returns:
        str: 反転されたテキスト。
    """
    return text[::-1]


def generate_qr_code(text):
    """
    テキストからQRコードを生成する。

    Args:
        text (str): QRコードに埋め込むテキスト。

    Returns:
        numpy.ndarray: 生成されたQRコード画像 (RGB)。
    """
    qr = qrcode.QRCode(version=5, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # PILイメージをNumPy配列に変換
    img_array = np.array(img.convert("RGB"))
    return img_array


def count_words(text):
    """
    テキストの単語数をカウントする。

    Args:
        text (str): カウントしたいテキスト。

    Returns:
        int: 単語数。
    """
    if not text.strip():
        return 0
    return len(text.split())


def resize_image(image, width, height):
    """
    画像をリサイズする。

    Args:
        image (numpy.ndarray): リサイズしたい画像。
        width (int): 新しい幅。
        height (int): 新しい高さ。

    Returns:
        numpy.ndarray: リサイズされた画像 (RGB)。
    """
    # NumPy配列からPILイメージに変換
    pil_image = Image.fromarray(image)

    resized_image = pil_image.resize((int(width), int(height)))
    return np.array(resized_image)


# --- Interface -----------------------------------------------------------

resize_interface = gr.Interface(
    fn=resize_image,
    inputs=[
        gr.Image(),
        gr.Number(label="幅", value=300),
        gr.Number(label="高さ", value=300),
    ],
    outputs=gr.Image(),
    api_name="resize_image",
)


demo = gr.TabbedInterface(
    [
        gr.Interface(reverse_text, gr.Textbox(), gr.Textbox(), api_name="reverse_text"),
        gr.Interface(generate_qr_code, gr.Textbox(), gr.Image(), api_name="generate_qr_code"),
        gr.Interface(count_words, gr.Textbox(), gr.Number(), api_name="count_words"),
        resize_interface,
    ],
    [
        "テキスト反転",
        "QRコード生成",
        "単語数カウント",
        "画像リサイズ",
    ],
)


if __name__ == "__main__":
    # mcp_server=True starts the SSE endpoint at /gradio_api/mcp/sse
    demo.launch(mcp_server=True)
```

`gMaL.md`

**サイズ**: 0.0 B | **行数**: 0 行
```markdown
(Empty file)
```

`requirements.txt`

**サイズ**: 154.0 B | **行数**: 6 行
```plaintext
gradio
numpy
qrcode[pil]
pillow
mcp
https://gradio-pypi-previews.s3.amazonaws.com/3b5cace94781b90993b596a83fb39fd1584d68ee/gradio-5.26.0-py3-none-any.whl
```

`.github/workflows/sync-to-hf.yml`

**サイズ**: 605.0 B | **行数**: 22 行
```yaml
name: Sync to Hugging Face hub
on:
  push:
    branches: [main]

  # to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  sync-to-hub:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          lfs: true
      - name: Push to hub
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          git fetch https://MakiAi:$HF_TOKEN@huggingface.co/spaces/MakiAi/gradio-mcp-template main || true
          git push --force https://MakiAi:$HF_TOKEN@huggingface.co/spaces/MakiAi/gradio-mcp-template main
```

