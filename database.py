# database.py

# ─────────────────────────────────────────────────────────────────────────────
# 知識圖譜主資料庫
# ─────────────────────────────────────────────────────────────────────────────

CONCEPTS = {
    # ════════ LEVEL 0: 終極基石 (公理) ════════
    "axiom": {
        "level": 0,
        "title": "公理系統",
        "emoji": "⚡",
        "color": "#FFD700",
        "summary": "無需證明、直接接受的真理",
        "detail": """
**公理**（Axiom）是數學大廈的地基。它們是邏輯推導的起點，本身不需要證明。

現代數學的標準基石是 **ZFC 集合論**。
1. **外延公理**：集合由其元素唯一決定。
2. **選擇公理**：在無限個集合中選出元素的可能性。
3. **皮亞諾公理**：定義了自然數與算術。
        """,
        "parents": [],
        "formula": r"\forall x \forall y [\forall z(z \in x \leftrightarrow z \in y) \rightarrow x = y]"
    },

    # ════════ LEVEL 1: 數學語言 ════════
    "logic": {
        "level": 1,
        "title": "形式邏輯",
        "emoji": "🔗",
        "color": "#C8A0FF",
        "summary": "推理的規則與結構",
        "detail": "邏輯學研究「有效論證」的結構。數學證明本質上是從公理出發，遵循邏輯規則的路徑。",
        "parents": ["axiom"],
        "formula": r"P \land (P \implies Q) \vdash Q"
    },
    "set_theory": {
        "level": 1,
        "title": "集合論",
        "emoji": "∈",
        "color": "#C8A0FF",
        "summary": "數學對象的統一語言",
        "detail": "康托爾創立的理論，認為所有數學對象（數、函數、空間）都可以被看作集合。",
        "parents": ["axiom"],
        "formula": r"A \cup B = \{x \mid x \in A \lor x \in B\}"
    },

    # ════════ LEVEL 2: 核心領域 ════════
    "algebra": {
        "level": 2,
        "title": "代數結構",
        "emoji": "🔢",
        "color": "#B88AFF",
        "summary": "符號運算與結構對稱性",
        "detail": "研究群、環、域等抽象結構，探索運算的本質而非具體的數字。",
        "parents": ["logic", "set_theory"],
        "formula": r"a(b+c) = ab + ac"
    },
    "analysis": {
        "level": 2,
        "title": "數學分析",
        "emoji": "📈",
        "color": "#B88AFF",
        "summary": "極限與連續性的研究",
        "detail": "微積分的嚴格化版本。它研究實數的完備性、序列的收斂性與函數的連續性。",
        "parents": ["logic", "set_theory"],
        "formula": r"\lim_{n \to \infty} a_n = L"
    },
    "geometry": {
        "level": 2,
        "title": "幾何學",
        "emoji": "📐",
        "color": "#B88AFF",
        "summary": "空間、形狀與度量",
        "detail": "從歐幾里得幾何到微分幾何，研究對象在空間中的位置與變換性質。",
        "parents": ["logic", "set_theory"],
        "formula": r"ds^2 = \sum g_{ij} dx^i dx^j"
    },

    # ════════ LEVEL 3: 進階工具 ════════
    "linear_algebra": {
        "level": 3,
        "title": "線性代數",
        "emoji": "🧮",
        "color": "#50C8FF",
        "summary": "向量空間與矩陣運算",
        "detail": "研究線性映射與向量空間。它是現代科學中最重要的計算語言。",
        "parents": ["algebra"],
        "formula": r"A\mathbf{x} = \mathbf{b}"
    },
    "calculus": {
        "level": 3,
        "title": "微積分",
        "emoji": "∫",
        "color": "#50C8FF",
        "summary": "變化率與累積量",
        "detail": "由牛頓與萊布尼茲創立，解決瞬時變化的量化問題。",
        "parents": ["analysis", "algebra"],
        "formula": r"f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}"
    },
    "probability": {
        "level": 3,
        "title": "機率論",
        "emoji": "🎲",
        "color": "#50C8FF",
        "summary": "隨機現象的量化模型",
        "detail": "基於測度論（分析學分支），為不確定性提供嚴格的數學描述。",
        "parents": ["analysis", "set_theory"],
        "formula": r"P(A) = \int_\Omega dP"
    },
    "topology": {
        "level": 3,
        "title": "拓撲學",
        "emoji": "🍩",
        "color": "#50C8FF",
        "summary": "連續變形下的不變性",
        "detail": "研究形狀在拉伸或彎曲（不撕裂）時保持不變的性質，如連通性。",
        "parents": ["geometry", "set_theory"],
        "formula": r"V - E + F = \chi"
    },

    # ════════ LEVEL 4: 當代應用 ════════
    "machine_learning": {
        "level": 4,
        "title": "機器學習",
        "emoji": "🤖",
        "color": "#7AFFCC",
        "summary": "統計優化與自動推理",
        "detail": "利用大規模數據與梯度下降算法，讓電腦自動尋找最優函數。依賴線性代數做特徵轉換，微積分做優化，機率論做預測。",
        "parents": ["linear_algebra", "calculus", "probability"],
        "formula": r"\theta^* = \arg\min_\theta \mathcal{L}(\theta)"
    },
    "cryptography": {
        "level": 4,
        "title": "現代密碼學",
        "emoji": "🔐",
        "color": "#7AFFCC",
        "summary": "基於計算困難性的安全",
        "detail": "利用數論（代數分支）中的困難問題（如大數分解或橢圓曲線）保護隱私。",
        "parents": ["algebra", "logic"],
        "formula": r"c = m^e \pmod{n}"
    },
    "quantum": {
        "level": 4,
        "title": "量子力學",
        "emoji": "⚛️",
        "color": "#7AFFCC",
        "summary": "微觀物理的數學描述",
        "detail": "物理世界的底層運作。其數學架構完全建立在複數希爾伯特空間（線性代數）與算符理論之上。",
        "parents": ["linear_algebra", "analysis"],
        "formula": r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi"
    },
    "computer_graphics": {
        "level": 4,
        "title": "電腦圖形學",
        "emoji": "🖥️",
        "color": "#7AFFCC",
        "summary": "渲染視覺世界的幾何學",
        "detail": "利用矩陣變換處理物體位置，利用微積分處理光線模擬（光線追蹤）。",
        "parents": ["linear_algebra", "geometry"],
        "formula": r"\mathbf{P}' = \mathbf{M}_{view} \cdot \mathbf{M}_{model} \cdot \mathbf{P}"
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# 輔助函式 (工具模組)
# ─────────────────────────────────────────────────────────────────────────────

def get_concept(key):
    """安全獲取概念資料"""
    return CONCEPTS.get(key)

def search_concepts(query):
    """
    智慧搜尋：在標題、摘要與詳細內容中查找關鍵字
    """
    if not query:
        return []
    
    query = query.lower()
    results = []
    
    for key, data in CONCEPTS.items():
        # 搜尋權重：標題 > 摘要 > 詳細內容
        if (query in data['title'].lower() or 
            query in data['summary'].lower() or 
            query in data['detail'].lower()):
            results.append(key)
            
    return results

def get_entry_points():
    """獲取預設的起始點（通常是最高 Level 的應用層）"""
    return [k for k, v in CONCEPTS.items() if v['level'] == 4]

def get_ancestry(key, visited=None):
    """
    遞迴獲取某個概念的所有祖先（用於全域地圖渲染）
    """
    if visited is None:
        visited = set()
    
    ancestry = []
    concept = CONCEPTS.get(key)
    
    if concept and key not in visited:
        visited.add(key)
        for parent_key in concept.get('parents', []):
            ancestry.append((parent_key, key))
            ancestry.extend(get_ancestry(parent_key, visited))
            
    return ancestry
