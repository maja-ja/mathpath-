import streamlit as st
import database as db
import styles
from extensions import MathExplorerExtensions as ext

# ─────────────────────────────────────────────────────────────────────────────
# 1. 初始化設定 (Page Config & Session State)
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="數源探索 Math Origin",
    page_icon="♾️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化全域狀態
if "history" not in st.session_state:
    st.session_state.history = []  # 存放走過的路徑 key
if "current" not in st.session_state:
    st.session_state.current = None  # 當前正在看的 concept key
if "search_mode" not in st.session_state:
    st.session_state.search_mode = False

# ─────────────────────────────────────────────────────────────────────────────
# 2. 側邊欄 (導航、搜尋與工具)
# ─────────────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("<h2 style='letter-spacing:-1px;'>🧩 探索控制台</h2>", unsafe_allow_html=True)
    
    # 主題切換
    theme_choice = st.select_slider(
        "切換視覺風格",
        options=["Dark Space", "Classic Parchment"],
        help="Dark Space 適合現代開發者；Classic Parchment 適合數學史研究者。"
    )
    styles.apply_styles(theme=theme_choice)
    
    st.divider()

    # 智慧搜尋功能
    search_query = st.text_input("🔍 搜尋概念或關鍵字", placeholder="例如：矩陣、極限...")
    if search_query:
        search_results = db.search_concepts(search_query)
        if search_results:
            st.caption(f"找到 {len(search_results)} 個相關結果：")
            for res_key in search_results:
                res_data = db.get_concept(res_key)
                if st.button(f"{res_data['emoji']} {res_data['title']}", key=f"sidebar_search_{res_key}", use_container_width=True):
                    # 跳轉邏輯
                    if st.session_state.current:
                        st.session_state.history.append(st.session_state.current)
                    st.session_state.current = res_key
                    st.rerun()
        else:
            st.warning("查無此概念，試試其他關鍵字？")

    st.divider()

    # 歷史軌跡 (可點擊跳回)
    st.markdown("#### 🛤️ 溯源軌跡")
    if not st.session_state.history:
        st.info("尚未開始探索。")
    else:
        for i, h_key in enumerate(st.session_state.history):
            h_data = db.get_concept(h_key)
            if st.button(f"{i+1}. {h_data['emoji']} {h_data['title']}", key=f"history_{i}", use_container_width=True):
                # 點擊歷史：回到那一步，並清除之後的路徑
                st.session_state.current = h_key
                st.session_state.history = st.session_state.history[:i]
                st.rerun()

    st.divider()
    
    # 重置按鈕
    if st.button("🏠 回到首頁 / 重置探索", use_container_width=True, type="primary"):
        st.session_state.current = None
        st.session_state.history = []
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# 3. 主畫面邏輯
# ─────────────────────────────────────────────────────────────────────────────

# --- A. 首頁 (未選取概念時) ---
if st.session_state.current is None:
    styles.render_header("♾️ 數學概念溯源探索器", "點擊任一應用領域，展開從當代技術到公理基石的溯源之旅")
    
    # 全域地圖擴充 (從 extensions 呼叫)
    ext.render_global_graph()
    
    st.markdown("### 🚀 從當代應用出發")
    entry_keys = db.get_entry_points()
    cols = st.columns(len(entry_keys))
    
    for i, key in enumerate(entry_keys):
        concept = db.get_concept(key)
        with cols[i]:
            card_html = f"""
            <div style="text-align:center;">
                <span style="font-size:3.5rem;">{concept['emoji']}</span>
                <h3 style="margin-top:10px;">{concept['title']}</h3>
                <p style="font-size:0.85rem; color:#8892b0; min-height:60px;">{concept['summary']}</p>
            </div>
            """
            st.markdown(styles.card_wrapper(card_html), unsafe_allow_html=True)
            if st.button(f"進入 {concept['title']}", key=f"entry_btn_{key}", use_container_width=True):
                st.session_state.current = key
                st.rerun()

# --- B. 詳情頁 (選取概念時) ---
else:
    curr_key = st.session_state.current
    concept = db.get_concept(curr_key)
    
    # 頂部導航 (麵包屑)
    path_html = '<div class="breadcrumb-container">'
    for h_key in st.session_state.history:
        h_data = db.get_concept(h_key)
        path_html += f'<span class="breadcrumb-item">{h_data["emoji"]} {h_data["title"]}</span> <span>→</span>'
    path_html += f'<span class="breadcrumb-item" style="background:{concept["color"]}33; border-color:{concept["color"]}">{concept["emoji"]} {concept["title"]}</span>'
    path_html += '</div>'
    st.markdown(path_html, unsafe_allow_html=True)

    # 內容佈局
    col_content, col_meta = st.columns([2, 1])

    with col_content:
        # 主卡片內容
        st.markdown(f"""
            <h1 style="color:{concept['color']}; font-size:3rem; margin-bottom:0px;">{concept['emoji']} {concept['title']}</h1>
            <p style="font-size:1.3rem; font-style:italic; opacity:0.8; margin-bottom:25px;">{concept['summary']}</p>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<div style='font-size:1.15rem; line-height:1.7;'>{concept['detail']}</div>", unsafe_allow_html=True)
        
        if concept.get('formula'):
            st.markdown("#### 📐 代表性公式 / 定義")
            st.markdown(f"""<div class="formula-container">""", unsafe_allow_html=True)
            st.latex(concept['formula'])
            st.markdown("</div>", unsafe_allow_html=True)
        
        # AI 導師延伸思考 (從 extensions 呼叫)
        ext.ai_tutor_mode(concept)

    with col_meta:
        # 進度與深度顯示
        st.markdown(f"**溯源深度：LEVEL {concept['level']}**")
        progress_val = (4 - concept['level']) / 4.0
        st.progress(progress_val)
        
        # 匯出報告 (從 extensions 呼叫)
        ext.export_journey(st.session_state.history, curr_key)
        
        st.divider()
        
        # 下一層級 (Parents)
        st.markdown("### 🔍 這建立在什麼之上？")
        parents = concept.get('parents', [])
        
        if parents:
            for p_key in parents:
                p_data = db.get_concept(p_key)
                st.markdown(f"""
                <div style="border-left: 3px solid {p_data['color']}; padding-left:15px; margin-bottom:10px;">
                    <p style="margin:0; font-weight:bold;">{p_data['emoji']} {p_data['title']}</p>
                    <p style="margin:0; font-size:0.8rem; opacity:0.7;">{p_data['summary']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"追溯至 {p_data['title']}", key=f"p_btn_{p_key}", use_container_width=True):
                    # 進入下一層
                    st.session_state.history.append(curr_key)
                    st.session_state.current = p_key
                    st.rerun()
        else:
            # 到達公理層
            st.balloons()
            st.success("✨ 您已到達數學的終點：公理系統。這裡是不證自明的真理，是一切邏輯的起點。")

    # 底部返回按鈕
    st.write("<br>", unsafe_allow_html=True)
    if st.button("⬅️ 返回上一層", use_container_width=False):
        if st.session_state.history:
            st.session_state.current = st.session_state.history.pop()
            st.rerun()
        else:
            st.session_state.current = None
            st.rerun()
