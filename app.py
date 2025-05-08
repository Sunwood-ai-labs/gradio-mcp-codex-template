"""app.py — Gradio MCP: Omikuji (Fortune) App

This Gradio application exposes several "omikuji" (fortune-telling) tools as both a
visual web UI (tabbed) and Model Context Protocol (MCP) SSE endpoints. Each tool is
implemented as a standalone Python function with a rich docstring so that Gradio
can automatically generate a JSON schema for MCP clients (Claude Desktop, Cline,
etc.).

Patterns implemented
--------------------
1. draw_omikuji_basic
   └─ Returns a single traditional Japanese fortune such as "大吉", "凶" …

2. draw_omikuji_lucky_item
   └─ Adds a random lucky item (財布, 植物, …) to the basic fortune.

3. draw_omikuji_lucky_color_number
   └─ Adds a lucky colour (赤, 青 …) *and* lucky number (1-99).

4. draw_omikuji_full
   └─ Gives a comprehensive result (overall/love/money/health fortunes, lucky
      colour, item and number).  Optional `name` input personalises the message.

Running
-------
```
uv venv            # optional: create virtual-env with uv (or use pip)
source .venv/bin/activate
uv pip install -r requirements.txt

python app.py      # UI http://127.0.0.1:7860/
                  # SSE http://127.0.0.1:7860/gradio_api/mcp/sse
```
"""

from __future__ import annotations

import random
from typing import Dict

import gradio as gr

# ---------------------------------------------------------------------------
# 🎴 Omikuji base data
# ---------------------------------------------------------------------------

FORTUNES = [
    "大吉",  # Excellent luck
    "中吉",  # Good luck
    "小吉",  # Little luck
    "吉",    # Luck
    "末吉",  # Future luck
    "凶",    # Bad luck
    "大凶",  # Terrible luck
]

LUCKY_ITEMS = [
    "財布",
    "スマホ",
    "手帳",
    "時計",
    "本",
    "鉛筆",
    "植物",
    "マグカップ",
    "イヤホン",
    "傘",
]

LUCKY_COLORS = [
    "赤",
    "青",
    "緑",
    "黄色",
    "紫",
    "オレンジ",
    "ピンク",
    "白",
    "黒",
    "金",
]


# ---------------------------------------------------------------------------
# 🔮 Omikuji functions (MCP tools)
# ---------------------------------------------------------------------------


def draw_omikuji_basic() -> str:
    """Draw a single omikuji fortune.

    Returns
    -------
    str
        A traditional Japanese fortune string such as "大吉" (excellent luck)
        or "凶" (bad luck).
    """

    return random.choice(FORTUNES)


def draw_omikuji_lucky_item() -> str:
    """Draw an omikuji fortune **with a lucky item**.

    Returns
    -------
    str
        A sentence combining the fortune and a randomly chosen lucky item.
        Example: "中吉 — 今日のラッキーアイテムは『時計』！".
    """

    fortune = random.choice(FORTUNES)
    item = random.choice(LUCKY_ITEMS)
    return f"{fortune} — 今日のラッキーアイテムは『{item}』！"


def draw_omikuji_lucky_color_number() -> str:
    """Draw an omikuji fortune **with lucky colour & number**.

    Returns
    -------
    str
        A formatted string that includes:
        - Fortune (大吉, …)
        - Lucky colour (赤, 青, …)
        - Lucky number (1–99)
    """

    fortune = random.choice(FORTUNES)
    color = random.choice(LUCKY_COLORS)
    number = random.randint(1, 99)
    return f"{fortune} — ラッキーカラー: {color} / ラッキーナンバー: {number}"


def draw_omikuji_full(name: str | None = None) -> Dict[str, str]:
    """Comprehensive omikuji result.

    Parameters
    ----------
    name : str | None, optional
        User's name.  When provided the message becomes personalised.

    Returns
    -------
    dict of str
        Keys: "overall", "love", "money", "health", "lucky_color",
        "lucky_item", "lucky_number".

    Notes
    -----
    This function returns a dict so that MCP clients receive structured JSON.
    In the Gradio UI the dictionary is rendered nicely as a JSON viewer.
    """

    overall = random.choice(FORTUNES)

    # Sub-category fortunes use a biased list (no 大凶) to avoid discouragement
    sub_fortunes = FORTUNES[:-1]  # remove 大凶
    love = random.choice(sub_fortunes)
    money = random.choice(sub_fortunes)
    health = random.choice(sub_fortunes)

    return {
        "name": name or "あなた",
        "overall": overall,
        "love": love,
        "money": money,
        "health": health,
        "lucky_color": random.choice(LUCKY_COLORS),
        "lucky_item": random.choice(LUCKY_ITEMS),
        "lucky_number": str(random.randint(1, 99)),
    }


# ---------------------------------------------------------------------------
# 🖼️  Gradio UI — TabbedInterface
# ---------------------------------------------------------------------------

# Each tool is mapped to a separate Interface for clarity.  The outputs are
# chosen so that both web UI and MCP behave nicely.

iface_basic = gr.Interface(
    fn=draw_omikuji_basic,
    inputs=[],  # no user input
    outputs=gr.Textbox(label="結果"),
    api_name="draw_omikuji_basic",
    description="最もシンプルな伝統おみくじです。クリックするだけで運勢が表示されます。",
)

iface_item = gr.Interface(
    fn=draw_omikuji_lucky_item,
    inputs=[],
    outputs=gr.Textbox(label="結果"),
    api_name="draw_omikuji_lucky_item",
    description="運勢に加えてラッキーアイテムを教えてくれるおみくじです。",
)


iface_color_number = gr.Interface(
    fn=draw_omikuji_lucky_color_number,
    inputs=[],
    outputs=gr.Textbox(label="結果"),
    api_name="draw_omikuji_lucky_color_number",
    description="運勢＋ラッキーカラー＆ナンバーのおみくじです。",
)


iface_full = gr.Interface(
    fn=draw_omikuji_full,
    inputs=[gr.Textbox(label="名前（任意）", placeholder="入力しなくてもOK")],
    outputs=gr.JSON(label="総合結果"),
    api_name="draw_omikuji_full",
    description="総合運・恋愛運・金運・健康運とラッキー情報を一度に表示します。",
)


# Combine into tabs
demo = gr.TabbedInterface(
    interface_list=[iface_basic, iface_item, iface_color_number, iface_full],
    tab_names=[
        "シンプルおみくじ",
        "アイテム付きおみくじ",
        "カラー＆ナンバーおみくじ",
        "総合おみくじ",
    ],
)


if __name__ == "__main__":
    # `mcp_server=True` exposes the functions to SSE clients at
    # /gradio_api/mcp/sse.  Passing `share=True` is optional here but useful for
    # quickly sharing the demo.
    demo.launch(mcp_server=True)
