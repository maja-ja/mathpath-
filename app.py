import streamlit as st
import streamlit.components.v1 as components

# ─────────────────────────────────────────────────────────────────────────────
# 1. 知識圖譜資料擴充 (結構化與內容增強)
# ─────────────────────────────────────────────────────────────────────────────

CONCEPTS = {
    "axiom": {
        "level": 0, "title": "公理系統", "emoji": "⚡", "color": "#FFD700",
        "summary": "不證自明的真理，數學的最終基石",
        "detail": "**公理**（Axiom）是邏輯系統的起點。現代數學大多建立在 **ZFC 集合論** 與 **一階邏輯** 之上。",
        "parents": [],
        "formula": r"\forall x \forall y [\forall z(z \in x \leftrightarrow z \in y) \rightarrow x = y]"
    },
    "logic": {
        "level": 1, "title": "邏輯學", "emoji": "🔗", "color": "#C8A0FF",
        "summary": "推理的規則與結構",
        "detail": "研究命題、量詞與證明的形式科學。它是所有數學論證的「作業系統」。",
        "parents": ["axiom"],
        "formula": r"P \land (P \implies Q) \vdash Q"
    },
    "set_theory": {
        "level": 1, "title": "集合論", "emoji": "∈", "color": "#C8A0FF",
        "summary": "數學對象的基礎語言",
        "detail": "由康托爾創立，將一切對象（數、函數、空間）統一定義為「集合」。",
        "parents": ["axiom"],
        "formula": r"A \cap B = \{x \mid x \in A \land x \in B\}"
    },
    "analysis": {
        "level": 2, "title": "分析學", "emoji": "📈", "color": "#B88AFF",
        "summary": "關於極限與連續性的研究",
        "detail": "從實數的完備性出發，研究函數的極限、微分與積分。",
        "parents": ["set_theory", "logic"],
        "formula": r"\forall \epsilon > 0, \exists \delta > 0 : |x-c| < \delta \implies |f(x)-L| < \epsilon"
    },
    "algebra": {
        "level": 2, "title": "代數", "emoji": "🔢", "color": "#B88AFF",
        "summary": "符號與運算的抽象研究",
        "detail": "研究結構（群、環、域）及其對稱性。",
        "parents": ["logic", "set_theory"],
        "formula": r"G \times G \to G, \quad (a,b) \mapsto a \cdot b"
    },
    "geometry": {
        "level": 2, "title": "幾何", "emoji": "📐", "color": "#B88AFF",
        "summary": "空間與測量的科學",
        "detail": "研究空間的曲率、流形與度量性質。",
        "parents": ["logic", "set_theory"],
        "formula": r"R_{uv} - \frac{1}{2}Rg_{uv} = T_{uv}"
    },
    "calculus": {
        "level": 3, "title": "微積分", "emoji": "∫", "color": "#50C8FF",
        "summary": "動態變化的數學",
        "detail": "結合代數與分析，處理瞬時變化與累積量。",
        "parents": ["analysis", "algebra"],
        "formula": r"\frac{d}{dx}\int_a^x f(t)dt = f(x)"
    },
    "linear_algebra": {
        "level": 3, "title": "線性代數", "emoji": "🧮", "color": "#50C8FF",
        "summary": "向量空間與線性變換",
        "detail": "現代科學的矩陣語言，應用於幾乎所有科學領域。",
        "parents": ["algebra"],
        "formula": r"\det(A - \lambda I) = 0"
    },
    "probability": {
        "level": 3, "title": "機率論", "emoji": "🎲", "color": "#50C8FF",
        "summary": "隨機現象的量化",
        "detail": "建立在測度論（分析學分支）之上的隨機規律研究。",
        "parents": ["analysis", "set_theory"],
        "formula": r"P(A|B) = \frac{P(B|A)P(A)}{P(B)}"
    },
    "machine_learning": {
        "level": 4, "title": "機器學習", "emoji": "🤖", "color": "#7AFFCC",
        "summary": "資料驅動的預測模型",
        "detail": "當代最強大的應用工具，結合優化理論與統計。",
        "parents": ["linear_algebra", "calculus", "probability"],
        "formula": r"w \leftarrow w - \eta \nabla J(w)"
    },
    "cryptography": {
        "level": 4, "title": "密碼學", "emoji": "🔐", "color": "#7AFFCC",
        "summary": "資訊安全與計算困難性",
        "detail": "利用數論與代數結構（如橢圓曲線）保護資訊。",
        "parents": ["algebra", "logic"],
        "formula": r"m \equiv c^d \pmod{n}"
    },
    "quantum_mechanics": {
        "level": 4, "title": "量子力學", "emoji": "⚛️", "color": "#7AFFCC",
        "summary": "微觀世界的線性代數",
        "detail": "描述粒子狀態的希爾伯特空間理論。",
        "parents": ["linear_algebra", "calculus"],
        "formula": r"\hat{H}|\psi\rangle = E|\psi\rangle"
    }
}

ENTRY_POINTS = ["machine_learning", "cryptography", "quantum_mechanics", "probability"]

# ─────────────────────────────────────────────────────────────────────────────
# 2. 頁面配置與 CSS 優化
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(page_title="Math Origin Explorer", page_icon="♾️", layout="wide")

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Fira+Code&display=swap');
    
    .stApp {{ background-color: #05070a; color: #e0e0e0; font-family: 'Inter', sans-serif; }}
    
    /* 毛玻璃卡片 */
    .glass-card {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
    }}
    
    /* 漸層標題 */
    .gradient-text {{
        background: linear-gradient(90deg, #fff, #888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }}

    /* 麵包屑導航 */
    .nav-link {{
        color: #888; text-decoration: none; font-size: 0.9rem;
        transition: 0.2s; cursor: pointer;
    }}
    .nav-link:hover {{ color: #00f2ff; }}

    /* 深度進度條 */
    .progress-container {{
        width: 100%; height: 4px; background: rgba(255,255,255,0.1);
        border-radius: 2px; margin: 20px 0;
    }}
    .progress-bar {{
        height: 100%; background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        box-shadow: 0 0 10px #4facfe; border-radius: 2px; transition: width 0.5s;
    }}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# 3. 邏輯處理 (Session State)
# ─────────────────────────────────────────────────────────────────────────────

if "history" not in st.session_state:
    st.session_state.history = []
if "current_key" not in st.session_state:
    st.session_state.current_key = None

def navigate_to(key):
    if key != st.session_state.current_key:
        if st.session_state.current_key:
            # 避免重複路徑
            if st.session_state.current_key in st.session_state.history:
                idx = st.session_state.history.index(st.session_state.current_key)
                st.session_state.history = st.session_state.history[:idx]
            st.session_state.history.append(st.session_state.current_key)
        st.session_state.current_key = key

def navigate_back(idx):
    st.session_state.current_key = st.session_state.history[idx]
    st.session_state.history = st.session_state.history[:idx]

# ─────────────────────────────────────────────────────────────────────────────
# 4. UI 渲染
# ─────────────────────────────────────────────────────────────────────────────

# --- 側邊欄：歷史追蹤與地圖 ---
with st.sidebar:
    st.markdown("<h2 class='gradient-text'>探索軌跡</h2>", unsafe_allow_html=True)
    if not st.session_state.history and not st.session_state.current_key:
        st.info("尚未開始溯源")
    else:
        if st.button("🏠 重置導航"):
            st.session_state.history = []
            st.session_state.current_key = None
            st.rerun()
        
        for i, h_key in enumerate(st.session_state.history):
            if st.button(f"{CONCEPTS[h_key]['emoji']} {CONCEPTS[h_key]['title']}", key=f"hist_{i}", use_container_width=True):
                navigate_back(i)
                st.rerun()

# --- 主畫面 ---
if st.session_state.current_key is None:
    # 首頁展示
    st.markdown("<h1 style='text-align:center; font-size:3.5rem;' class='gradient-text'>數學概念溯源</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>追尋知識的終極邊界：從應用科學回到第一性原理</p>", unsafe_allow_html=True)
    st.write("---")
    
    cols = st.columns(len(ENTRY_POINTS))
    for i, key in enumerate(ENTRY_POINTS):
        concept = CONCEPTS[key]
        with cols[i]:
            st.markdown(f"""<div class='glass-card' style='height:200px; text-align:center; border-top: 4px solid {concept['color']}'>
                <div style='font-size:3rem'>{concept['emoji']}</div>
                <h3>{concept['title']}</h3>
                <p style='font-size:0.8rem; color:#aaa'>{concept['summary']}</p>
            </div>""", unsafe_allow_html=True)
            if st.button(f"探究 {concept['title']}", key=f"btn_{key}", use_container_width=True):
                navigate_to(key)
                st.rerun()

else:
    # 概念詳細頁
    key = st.session_state.current_key
    concept = CONCEPTS[key]
    
    # 頂部進度條 (深度：4->0)
    depth_pct = (4 - concept['level']) * 25
    st.markdown(f"""
        <div style='display:flex; justify-content:space-between; align-items:center'>
            <span style='color:#888; font-size:0.8rem;'>溯源深度：LEVEL {concept['level']}</span>
            <span style='color:{concept['color']}; font-weight:bold;'>{concept['title']}</span>
        </div>
        <div class="progress-container"><div class="progress-bar" style="width: {depth_pct}%"></div></div>
    """, unsafe_allow_html=True)

    col_main, col_viz = st.columns([2, 1])

    with col_main:
        st.markdown(f"<h1 style='color:{concept['color']}'>{concept['emoji']} {concept['title']}</h1>", unsafe_allow_html=True)
        st.markdown(f"### *{concept['summary']}*")
        st.write(concept['detail'])
        
        if concept.get("formula"):
            st.latex(concept["formula"])

    with col_viz:
        # Mermaid 局部圖譜
        mermaid_code = "graph BT\n"
        for p_key in concept['parents']:
            mermaid_code += f"  {key}[{concept['title']}] --> {p_key}[{CONCEPTS[p_key]['title']}]\n"
        
        if concept['parents']:
            st.markdown("**局部關係圖**")
            components.html(f"""
                <div class="mermaid" style="background:transparent;">
                    {mermaid_code}
                </div>
                <script type="module">
                    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                    mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
                </script>
            """, height=200)

    st.write("---")
    
    # 下一步：溯源路徑
    if concept['parents']:
        st.subheader("🔍 向下溯源：這建立在什麼之上？")
        p_cols = st.columns(len(concept['parents']))
        for i, p_key in enumerate(concept['parents']):
            p_concept = CONCEPTS[p_key]
            with p_cols[i]:
                st.markdown(f"""<div style='padding:15px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid {p_concept['color']}44'>
                    <h4 style='margin:0'>{p_concept['emoji']} {p_concept['title']}</h4>
                    <p style='font-size:0.8rem; color:#888'>{p_concept['summary']}</p>
                </div>""", unsafe_allow_html=True)
                if st.button(f"進入 {p_concept['title']}", key=f"p_btn_{p_key}"):
                    navigate_to(p_key)
                    st.rerun()
    else:
        st.balloons()
        st.success("🎉 你已到達數學的終點：公理系統。這裡是不證自明的真理。")

    # 底層導航
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("⬅️ 返回上一層"):
        if st.session_state.history:
            st.session_state.current_key = st.session_state.history.pop()
            st.rerun()
        else:
            st.session_state.current_key = None
            st.rerun()
