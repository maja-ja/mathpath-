import streamlit as st

def apply_styles(theme="Dark Space"):
    """
    套用全域 CSS 樣式與主題切換。
    可用主題: "Dark Space" (預設), "Classic Parchment" (復古羊皮紙)
    """
    
    # 定義主題變數
    if theme == "Classic Parchment":
        # 復古學術風格
        bg_color = "#f4f1ea"
        card_bg = "rgba(255, 255, 255, 0.5)"
        text_color = "#3d2b1f"
        accent_color = "#8b4513"
        border_color = "rgba(139, 69, 19, 0.2)"
        secondary_text = "#5d4037"
        font_family = "'EB Garamond', serif"
    else:
        # 現代深空風格
        bg_color = "#05070a"
        card_bg = "rgba(255, 255, 255, 0.03)"
        text_color = "#e0e6ed"
        accent_color = "#4facfe"
        border_color = "rgba(255, 255, 255, 0.1)"
        secondary_text = "#8892b0"
        font_family = "'Inter', sans-serif"

    # 注入 Google Fonts
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=EB+Garamond:ital,wght@0,400;0,700;1,400&family=Fira+Code&display=swap');
        </style>
    """, unsafe_allow_html=True)

    # 核心 CSS 樣式
    st.markdown(f"""
        <style>
        /* 基礎設置 */
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
            font-family: {font_family};
        }}

        /* 隱藏 Streamlit 預設裝飾 */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}

        /* 自定義捲軸 */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: {bg_color};
        }}
        ::-webkit-scrollbar-thumb {{
            background: {accent_color}44;
            border-radius: 10px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: {accent_color}88;
        }}

        /* 毛玻璃概念卡片 */
        .concept-card {{
            background: {card_bg};
            border: 1px solid {border_color};
            border-radius: 20px;
            padding: 30px;
            backdrop-filter: blur(12px);
            margin-bottom: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, border 0.3s ease;
        }}
        .concept-card:hover {{
            transform: translateY(-5px);
            border-color: {accent_color}aa;
        }}

        /* 漸層文字標題 */
        .gradient-title {{
            background: linear-gradient(135deg, {text_color} 0%, {accent_color} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: -1px;
        }}

        /* 溯源路徑標籤 (Breadcrumbs) */
        .breadcrumb-container {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}
        .breadcrumb-item {{
            background: {accent_color}15;
            color: {accent_color};
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid {accent_color}33;
        }}

        /* 公式容器 */
        .formula-container {{
            background: rgba(0, 0, 0, 0.2);
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            border-left: 4px solid {accent_color};
            font-family: 'Fira Code', monospace;
        }}

        /* 側邊欄優化 */
        [data-testid="stSidebar"] {{
            background-color: {bg_color};
            border-right: 1px solid {border_color};
        }}
        [data-testid="stSidebar"] .stButton button {{
            background-color: transparent;
            border: 1px solid {border_color};
            color: {secondary_text};
            transition: 0.2s;
        }}
        [data-testid="stSidebar"] .stButton button:hover {{
            border-color: {accent_color};
            color: {accent_color};
            background-color: {accent_color}11;
        }}

        /* 進度條自定義 */
        .stProgress > div > div > div > div {{
            background-image: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        }}

        /* 針對列印/匯出的樣式控制 */
        @media print {{
            .no-print {{ display: none !important; }}
            .stApp {{ background-color: white !important; color: black !important; }}
            .concept-card {{ border: 1px solid #ccc !important; box-shadow: none !important; }}
        }}
        </style>
    """, unsafe_allow_html=True)

def render_header(title, subtitle):
    """渲染統一的頁首樣式"""
    st.markdown(f"""
        <div style="text-align: center; padding: 40px 0;">
            <h1 class="gradient-title" style="font-size: 3.5rem; margin-bottom: 10px;">{title}</h1>
            <p style="color: #8892b0; font-size: 1.2rem; max-width: 700px; margin: 0 auto;">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)

def card_wrapper(content_html):
    """將 HTML 內容包裝在卡片樣式中"""
    return f'<div class="concept-card">{content_html}</div>'
