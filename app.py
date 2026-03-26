import streamlit as st
from database import CONCEPTS, search_concepts
from extensions import MathExplorerExtensions as ext
from styles import apply_custom_css

# --- 初始化 ---
st.set_page_config(page_title="數源探索 2.0", layout="wide")
apply_custom_css()

if "history" not in st.session_state: st.session_state.history = []
if "current" not in st.session_state: st.session_state.current = None

# --- 側邊欄：搜尋與導航 ---
with st.sidebar:
    st.title("🧩 探索面板")
    
    # 功能 1：快速檢索
    search_q = st.text_input("🔍 快速搜尋概念", placeholder="例如：線性代數...")
    if search_q:
        results = search_concepts(search_q)
        for k, v in results:
            if st.button(f"前往 {v['emoji']} {v['title']}", key=f"search_{k}"):
                st.session_state.history.append(st.session_state.current)
                st.session_state.current = k
                st.rerun()

    st.divider()
    
    # 功能 2：路徑追蹤
    st.subheader("🛤️ 已走過的路徑")
    for i, h in enumerate(st.session_state.history):
        if h: st.caption(f"{i+1}. {CONCEPTS[h]['title']}")
    
    if st.button("🏠 回到首頁", use_container_width=True):
        st.session_state.current = None
        st.session_state.history = []
        st.rerun()

# --- 主內容區 ---
if st.session_state.current is None:
    st.markdown("<h1 style='text-align:center;'>♾️ 數學概念溯源探索器</h1>", unsafe_allow_html=True)
    
    # 功能 3：全域地圖擴充
    ext.render_global_graph()
    
    st.write("### 🚀 從當代應用開始...")
    cols = st.columns(3)
    starters = ["machine_learning", "cryptography", "quantum"]
    for i, s in enumerate(starters):
        with cols[i % 3]:
            c = CONCEPTS[s]
            st.markdown(f"<div class='concept-card'><h3>{c['emoji']} {c['title']}</h3><p>{c['summary']}</p></div>", unsafe_allow_html=True)
            if st.button(f"追溯 {c['title']}", key=f"start_{s}"):
                st.session_state.current = s
                st.rerun()

else:
    curr_key = st.session_state.current
    c = CONCEPTS[curr_key]
    
    # 麵包屑導航
    st.markdown(f"路徑：{' > '.join([CONCEPTS[h]['title'] for h in st.session_state.history if h])} > **{c['title']}**")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title(f"{c['emoji']} {c['title']}")
        st.markdown(c['detail'])
        if c.get('formula'): st.latex(c['formula'])
        
        # 功能 4：AI 導師擴充
        ext.ai_tutor_mode(c)
        
    with col2:
        # 功能 5：匯出筆記擴充
        ext.export_journey(st.session_state.history, curr_key)
        
        st.divider()
        st.subheader("⛓️ 它的基石是：")
        for p in c.get('parents', []):
            pc = CONCEPTS[p]
            if st.button(f"⬇️ {pc['emoji']} {pc['title']}", key=f"p_{p}", use_container_width=True):
                st.session_state.history.append(curr_key)
                st.session_state.current = p
                st.rerun()
                
        if not c.get('parents'):
            st.warning("✨ 恭喜！你已抵達公理層級，這是數學的終極邊界。")

    if st.button("⬅️ 返回上一層"):
        if st.session_state.history:
            st.session_state.current = st.session_state.history.pop()
            st.rerun()
