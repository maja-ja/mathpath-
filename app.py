“””
數學概念溯源探索器 — Streamlit 版
點擊任一概念，逐層溯源直到公理

執行方式：streamlit run math_explorer.py

擴充方式：在 CONCEPTS 字典中新增條目
“””

import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────

# 知識圖譜資料（可自由擴充）

# 每個概念包含：

# title    顯示名稱

# emoji    圖示

# color    主色（CSS 顏色）

# summary  簡短說明

# detail   詳細說明（Markdown）

# parents  前驅概念的 key（點擊後繼續溯源）

# formula  可選：代表性公式（LaTeX）

# ─────────────────────────────────────────────────────────────────────────────

CONCEPTS = {

```
# ════════ 終點：公理（無父節點）════════
"axiom": {
    "title": "公理",
    "emoji": "⚡",
    "color": "#ffd700",
    "summary": "不證自明的真理，數學的最終基石",
    "detail": """
```

**公理**（Axiom）是數學的起點——無需證明、直接接受的命題。

歐幾里得在《幾何原本》中提出五大公設，奠定了幾何學的基礎。
20 世紀，策梅洛-弗蘭克爾集合論（ZFC）成為現代數學的標準公理系統。

> *「數學的真理，不在外部世界，而在公理的邏輯推演之中。」*
> “””,
> “parents”: [],
> “formula”: r”\text{ZFC: } \forall x \forall y [\forall z(z \in x \leftrightarrow z \in y) \rightarrow x = y]”,
> },

```
# ════════ 第一層 ════════
"logic": {
    "title": "邏輯學",
    "emoji": "🔗",
    "color": "#c8a0ff",
    "summary": "推理的規則與結構",
    "detail": """
```

**邏輯學**研究有效推理的形式規則。

- **命題邏輯**：真假值的運算
- **謂詞邏輯**：量詞 ∀、∃ 的使用
- **模態邏輯**：必然性與可能性

數學的每一個證明，本質上都是一個邏輯推導鏈。
“””,
“parents”: [“axiom”],
“formula”: r”(P \rightarrow Q) \land P \vdash Q \quad \text{(Modus Ponens)}”,
},
“set_theory”: {
“title”: “集合論”,
“emoji”: “∈”,
“color”: “#c8a0ff”,
“summary”: “數學對象的基礎語言”,
“detail”: “””
**集合論**是現代數學的通用語言，由康托爾於 19 世紀末創立。

所有數學結構——數字、函數、空間——都可以用集合來定義。
ZFC 公理系統為集合論提供嚴格的邏輯基礎。
“””,
“parents”: [“axiom”],
“formula”: r”A \cup B = {x \mid x \in A \lor x \in B}”,
},

```
# ════════ 第二層：古典分支 ════════
"algebra": {
    "title": "代數",
    "emoji": "🔢",
    "color": "#b88aff",
    "summary": "符號與運算的抽象研究",
    "detail": """
```

**代數**源自阿拉伯語 *الجبر*（al-jabr），由花拉子密於約 820 CE 系統化。

從求解方程，到研究抽象結構（群、環、域），
代數貫穿了數學的每個分支。
“””,
“parents”: [“logic”, “set_theory”],
“formula”: r”ax^2 + bx + c = 0 \implies x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}”,
},
“geometry”: {
“title”: “幾何”,
“emoji”: “📐”,
“color”: “#b88aff”,
“summary”: “空間、形狀與測量的研究”,
“detail”: “””
**幾何**源自希臘語 *γεωμετρία*（測量大地）。

歐幾里得《幾何原本》（約 300 BCE）是人類歷史上最有影響力的數學著作之一。
從歐氏幾何到非歐幾何，再到微分幾何，空間的概念不斷深化。
“””,
“parents”: [“logic”, “set_theory”],
“formula”: r”a^2 + b^2 = c^2 \quad \text{(畢氏定理)}”,
},
“number_theory”: {
“title”: “數論”,
“emoji”: “🔍”,
“color”: “#b88aff”,
“summary”: “整數與質數的深層規律”,
“detail”: “””
**數論**被高斯稱為「數學的女王」。

研究整數的性質、質數分布、同餘關係。
費馬大定理、黎曼猜想皆屬此門。
“””,
“parents”: [“logic”, “set_theory”],
“formula”: r”e^{i\pi} + 1 = 0 \quad \text{（歐拉恆等式）}”,
},

```
# ════════ 第三層：現代領域 ════════
"linear_algebra": {
    "title": "線性代數",
    "emoji": "🧮",
    "color": "#50c8ff",
    "summary": "向量、矩陣與線性變換",
    "detail": """
```

**線性代數**研究向量空間與線性映射。

矩陣運算、特徵值分解、奇異值分解（SVD）是現代計算的核心工具，
廣泛應用於物理、工程與機器學習。
“””,
“parents”: [“algebra”],
“formula”: r”A\mathbf{v} = \lambda\mathbf{v} \quad \text{（特徵值方程）}”,
},
“abstract_algebra”: {
“title”: “抽象代數”,
“emoji”: “🌀”,
“color”: “#50c8ff”,
“summary”: “群、環、域的結構理論”,
“detail”: “””
**抽象代數**研究具有特定運算性質的代數結構。

- **群**（Group）：具有封閉性、結合律、單位元、反元素
- **環**（Ring）：兩種運算的結構
- **域**（Field）：可加可乘可除的結構

伽羅瓦理論用群論解釋了為何五次方程沒有根式解。
“””,
“parents”: [“algebra”],
“formula”: r”\forall a \in G, \exists a^{-1}: a \cdot a^{-1} = e”,
},
“calculus”: {
“title”: “微積分”,
“emoji”: “∫”,
“color”: “#50c8ff”,
“summary”: “變化率與累積量的數學”,
“detail”: “””
**微積分**由牛頓與萊布尼茲在 17 世紀各自獨立發展。

- **微分**：瞬時變化率、切線斜率
- **積分**：面積、累積量
- **微積分基本定理**：二者互為逆運算
  “””,
  “parents”: [“algebra”, “geometry”],
  “formula”: r”\int_a^b f’(x),dx = f(b) - f(a)”,
  },
  “topology”: {
  “title”: “拓撲學”,
  “emoji”: “🍩”,
  “color”: “#50c8ff”,
  “summary”: “連續變形下不變的性質”,
  “detail”: “””
  **拓撲學**研究在連續變形（拉伸、彎曲，但不撕裂）下保持不變的性質。

咖啡杯與甜甜圈在拓撲上是「一樣的」（都有一個洞）。
龐加萊猜想（2003 年由佩雷爾曼證明）是拓撲學的里程碑。
“””,
“parents”: [“geometry”, “set_theory”],
“formula”: r”\chi = V - E + F = 2 \quad \text{（歐拉示性數）}”,
},

```
# ════════ 第四層：當代應用 ════════
"machine_learning": {
    "title": "機器學習",
    "emoji": "🤖",
    "color": "#7affcc",
    "summary": "從資料中學習規律的演算法",
    "detail": """
```

**機器學習**結合線性代數、微積分與統計學。

梯度下降法最小化損失函數，反向傳播計算梯度。
神經網路本質上是高維函數的組合近似。
“””,
“parents”: [“linear_algebra”, “calculus”],
“formula”: r”\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}(\theta)”,
},
“cryptography”: {
“title”: “密碼學”,
“emoji”: “🔐”,
“color”: “#7affcc”,
“summary”: “基於數學難題保護資訊”,
“detail”: “””
**現代密碼學**建立在計算困難性假設之上。

- **RSA**：依賴大數分解困難
- **橢圓曲線**：依賴離散對數問題
- **零知識證明**：不洩露秘密即可驗證真實性
  “””,
  “parents”: [“abstract_algebra”, “number_theory”],
  “formula”: r”c = m^e \bmod n \quad \text{（RSA 加密）}”,
  },
  “fourier”: {
  “title”: “傅里葉分析”,
  “emoji”: “〰️”,
  “color”: “#7affcc”,
  “summary”: “將函數分解為頻率成分”,
  “detail”: “””
  **傅里葉分析**由約瑟夫·傅里葉於 1822 年發展。

任何週期函數都可以分解為正弦與餘弦的疊加。
廣泛應用於音訊處理、影像壓縮（JPEG）、量子力學。
“””,
“parents”: [“calculus”],
“formula”: r”\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x), e^{-2\pi i x\xi}, dx”,
},
“quantum”: {
“title”: “量子力學”,
“emoji”: “⚛️”,
“color”: “#7affcc”,
“summary”: “微觀世界的數學描述”,
“detail”: “””
**量子力學**的數學框架建立在線性代數與函數分析之上。

- 狀態空間是希爾伯特空間
- 可觀測量是厄米算符
- 測量結果是算符的特徵值
  “””,
  “parents”: [“linear_algebra”, “calculus”, “abstract_algebra”],
  “formula”: r”i\hbar\frac{\partial}{\partial t}|\psi\rangle = \hat{H}|\psi\rangle”,
  },
  “computer_graphics”: {
  “title”: “電腦圖形”,
  “emoji”: “🖥️”,
  “color”: “#7affcc”,
  “summary”: “用數學渲染虛擬世界”,
  “detail”: “””
  **電腦圖形學**將幾何與線性代數應用於視覺化。
- 矩陣變換：旋轉、縮放、投影
- 光線追蹤：射線與幾何體的求交
- 貝茲曲線：字體與曲面設計
  “””,
  “parents”: [“linear_algebra”, “geometry”],
  “formula”: r”\mathbf{p’} = \mathbf{M}*{proj} \cdot \mathbf{M}*{view} \cdot \mathbf{M}_{model} \cdot \mathbf{p}”,
  },
  “network_analysis”: {
  “title”: “網路分析”,
  “emoji”: “🕸️”,
  “color”: “#7affcc”,
  “summary”: “圖論與連通性的應用”,
  “detail”: “””
  **網路分析**以圖論為基礎，研究節點與邊的關係。

應用於：社群網路、交通規劃、網際網路路由、生物網路。
PageRank 演算法是線性代數在圖上的經典應用。
“””,
“parents”: [“abstract_algebra”, “topology”],
“formula”: r”PR(u) = \sum_{v \in B_u} \frac{PR(v)}{L(v)}”,
},
}

# ─────────────────────────────────────────────────────────────────────────────

# 入口頁（可供使用者選擇出發點）

# ─────────────────────────────────────────────────────────────────────────────

ENTRY_POINTS = [
(“machine_learning”,  “🤖 機器學習”),
(“cryptography”,      “🔐 密碼學”),
(“fourier”,           “〰️ 傅里葉分析”),
(“quantum”,           “⚛️ 量子力學”),
(“computer_graphics”, “🖥️ 電腦圖形”),
(“network_analysis”,  “🕸️ 網路分析”),
]

# ─────────────────────────────────────────────────────────────────────────────

# Streamlit UI

# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
page_title=“數學溯源探索器”,
page_icon=“⚡”,
layout=“centered”,
)

st.markdown(”””

<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'EB Garamond', Georgia, serif;
}
.stApp { background: #0b0e1a; }
.block-container { max-width: 720px; padding-top: 2rem; }

/* 概念卡片 */
.concept-card {
    border-radius: 14px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}
.concept-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 14px;
    padding: 1px;
    background: linear-gradient(135deg, var(--c), transparent 60%);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    pointer-events: none;
}

/* 麵包屑 */
.breadcrumb {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    align-items: center;
    margin-bottom: 1.5rem;
    font-size: 0.85rem;
    color: rgba(200,210,255,0.45);
}
.breadcrumb-item {
    padding: 2px 10px;
    border-radius: 20px;
    border: 1px solid rgba(200,200,255,0.2);
    color: rgba(200,210,255,0.6);
    font-size: 0.8rem;
}
.breadcrumb-item.current {
    border-color: rgba(200,200,255,0.5);
    color: #e0e8ff;
}

/* 標題 */
h1 { color: #e8e0ff !important; font-family: 'EB Garamond', serif !important; }
h2 { color: #c8d8ff !important; font-family: 'EB Garamond', serif !important; }

/* formula box */
.formula-box {
    background: rgba(20,30,60,0.6);
    border-left: 3px solid;
    border-radius: 0 8px 8px 0;
    padding: 0.8rem 1.2rem;
    margin: 1rem 0;
}
</style>

“””, unsafe_allow_html=True)

# ── Session State 初始化 ──────────────────────────────

if “path” not in st.session_state:
st.session_state.path = []   # 瀏覽歷史：key 的串列
if “current” not in st.session_state:
st.session_state.current = None

def go_to(key):
if st.session_state.current:
st.session_state.path.append(st.session_state.current)
st.session_state.current = key

def go_back():
if st.session_state.path:
st.session_state.current = st.session_state.path.pop()
else:
st.session_state.current = None

# ── 首頁 ─────────────────────────────────────────────

if st.session_state.current is None:
st.markdown(”# ⚡ 數學溯源探索器”)
st.markdown(
“<p style='color:rgba(180,200,255,0.6);font-size:1.05rem'>”
“選擇一個你感興趣的概念，逐層追溯，直到數學的根基——公理。”
“</p>”,
unsafe_allow_html=True,
)
st.markdown(”—”)
st.markdown(”### 選擇起點”)

```
cols = st.columns(2)
for i, (key, label) in enumerate(ENTRY_POINTS):
    with cols[i % 2]:
        c = CONCEPTS[key]
        if st.button(
            f"{c['emoji']} **{c['title']}**\n\n{c['summary']}",
            key=f"entry_{key}",
            use_container_width=True,
        ):
            go_to(key)
            st.rerun()

st.markdown(
    "<p style='color:rgba(180,200,255,0.3);font-size:0.8rem;text-align:center;margin-top:2rem'>"
    "每個概念都有其前驅概念，一路點擊即可追溯到公理 ⚡</p>",
    unsafe_allow_html=True,
)
```

# ── 概念詳情頁 ───────────────────────────────────────

else:
key = st.session_state.current
c = CONCEPTS[key]
color = c[“color”]

```
# 麵包屑
crumb_html = '<div class="breadcrumb">'
for k in st.session_state.path:
    crumb_html += f'<span class="breadcrumb-item">{CONCEPTS[k]["emoji"]} {CONCEPTS[k]["title"]}</span>'
    crumb_html += '<span>›</span>'
crumb_html += f'<span class="breadcrumb-item current">{c["emoji"]} {c["title"]}</span>'
crumb_html += '</div>'
st.markdown(crumb_html, unsafe_allow_html=True)

# 主卡片
st.markdown(
    f"""<div class="concept-card" style="background:linear-gradient(135deg,rgba(20,25,50,0.9),rgba(10,14,30,0.95));--c:{color}">
    <h1 style="color:{color};font-size:2.2rem;margin-bottom:0.3rem">{c['emoji']} {c['title']}</h1>
    <p style="color:rgba(200,220,255,0.55);font-style:italic;margin-bottom:1rem">{c['summary']}</p>
    </div>""",
    unsafe_allow_html=True,
)

# 詳細說明
st.markdown(c["detail"])

# 公式
if c.get("formula"):
    st.markdown(
        f'<div class="formula-box" style="border-color:{color}55">',
        unsafe_allow_html=True,
    )
    st.latex(c["formula"])
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# 前驅概念（繼續溯源）
parents = c.get("parents", [])
if parents:
    st.markdown(
        f"<p style='color:rgba(200,220,255,0.6);font-size:1rem'>"
        f"**{c['title']}** 建立在以下概念之上：</p>",
        unsafe_allow_html=True,
    )
    cols = st.columns(len(parents))
    for i, pk in enumerate(parents):
        pc = CONCEPTS[pk]
        with cols[i]:
            if st.button(
                f"{pc['emoji']} **{pc['title']}**\n\n{pc['summary']}",
                key=f"parent_{pk}_{key}",
                use_container_width=True,
            ):
                go_to(pk)
                st.rerun()
else:
    st.markdown(
        f"<div style='text-align:center;padding:2rem;border:1px solid {color}44;border-radius:12px;"
        f"background:rgba(20,25,50,0.4)'>"
        f"<p style='font-size:2rem'>{c['emoji']}</p>"
        f"<p style='color:{color};font-size:1.2rem;font-weight:600'>已到達根基</p>"
        f"<p style='color:rgba(200,220,255,0.5)'>這裡沒有更深的前驅——這就是數學的公理。</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# 返回按鈕
bcol1, bcol2 = st.columns([1, 3])
with bcol1:
    if st.button("← 返回上一步", use_container_width=True):
        go_back()
        st.rerun()
with bcol2:
    if st.button("🏠 回到起點", use_container_width=True):
        st.session_state.current = None
        st.session_state.path = []
        st.rerun()
```
