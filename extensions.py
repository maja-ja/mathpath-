import streamlit as st
import streamlit.components.v1 as components

class MathExplorerExtensions:
    
    @staticmethod
    def render_global_graph():
        """全域地圖：使用 Mermaid 渲染完整拓撲"""
        with st.expander("🌐 查看全域知識地圖", expanded=False):
            graph_code = "graph TD\n"
            from database import CONCEPTS
            for k, v in CONCEPTS.items():
                for p in v.get('parents', []):
                    graph_code += f"  {p}[{CONCEPTS[p]['title']}] --> {k}[{v['title']}]\n"
            
            components.html(f"""
                <pre class="mermaid">{graph_code}</pre>
                <script type="module">
                    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                    mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
                </script>
            """, height=400, scrolling=True)

    @staticmethod
    def export_journey(path, current_key):
        """匯出功能：生成 Markdown 學習報告"""
        from database import CONCEPTS
        full_path = path + [current_key]
        report = "# 數學溯源學習報告\n\n"
        for i, key in enumerate(full_path):
            c = CONCEPTS[key]
            report += f"## {i+1}. {c['emoji']} {c['title']}\n- **定義**: {c['summary']}\n- **細節**: {c['detail']}\n\n"
        
        st.download_button(
            label="📥 匯出當前溯源筆記 (Markdown)",
            data=report,
            file_name="math_journey.md",
            mime="text/markdown"
        )

    @staticmethod
    def ai_tutor_mode(concept):
        """AI 助手：模擬針對該概念的延伸問題"""
        st.info(f"🤖 **AI 導師提問**：你覺得『{concept['title']}』如果沒有了『{concept['parents'][0] if concept['parents'] else '公理'}』會發生什麼事？")
        if st.button("查看 AI 深度解析"):
            st.write("這是一個深度思考題：數學的結構是層層堆疊的，若底層失效，上層邏輯將崩塌...")
