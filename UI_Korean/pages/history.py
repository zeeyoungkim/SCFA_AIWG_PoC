import streamlit as st

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; height: 54px; margin-bottom: 24px; border-bottom: 1.5px solid #e8e8e8;">
        <div style="flex:1; display: flex; align-items: center;">
            <button style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-left: 4px;">
                &#8592;
            </button>
        </div>
        <div style="flex:2; text-align: center; font-size: 1.25rem; font-weight: 700; letter-spacing:0.03em;">
            히스토리
        </div>
        <div style="flex:1; display: flex; justify-content: flex-end; align-items: center;">
            <button id="menu-btn" style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-right: 4px;">
                &#9776;
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])

with col1:
    search = st.text_input(label="search", key="search_input", placeholder="검색어를 입력하세요...", label_visibility="hidden")
with col2:
    st.markdown("""
        <style>
            div.stButton > button {
                margin-top: 8px;
            }
        </style>
    """, unsafe_allow_html=True)
    search_btn = st.button("검색", use_container_width=True, key="search_button")

st.markdown("---", unsafe_allow_html=True)

st.markdown("""
    <style>
    .custom-card {
        background-color: #f8f9fa;
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.09);
        padding: 24px 32px 20px 32px;
        margin-bottom: 24px;
        border: 1px solid #e5e7eb;
        transition: box-shadow 0.18s;
    }
    .custom-card:hover {
        box-shadow: 0 6px 28px rgba(0,0,0,0.14);
    }
    .custom-card .title {
        font-size: 1.15rem;
        font-weight: bold;
        color: #253142;
        margin-bottom: 9px;
        letter-spacing: 0.5px;
    }
    .custom-card .desc {
        font-size: 1rem;
        color: #505b6b;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

def card_box(location, date, interest, summary):
    st.markdown(f"""
    <div class="custom-card">
        <div class="title">위치: { location }</div>
        <div class="desc">날짜: { date }</div>
        <div class="desc">관심사: { interest }</div>
        <div class="desc">검색 요약: { summary }</div>
    </div>
    """, unsafe_allow_html=True)

cards = [
    {
        "location": "일본",
        "date": "2025/05/02",
        "interest": "요리",
        "summary": "오사카의 유명한 레스토랑"
    },
    {
        "location": "중국",
        "date": "2025/07/30",
        "interest": "박물관",
        "summary": "상하이의 역사 박물관"
    },
]

if "filtered_cards" not in st.session_state:
    st.session_state.filtered_cards = cards

if search_btn:
    keyword = search.strip().lower()
    if keyword:
        st.session_state.filtered_cards = [
            card for card in cards if keyword in card["interest"].lower()
        ]
    else:
        st.session_state.filtered_cards = cards

if st.session_state.filtered_cards:
    for card in st.session_state.filtered_cards:
        card_box(location=card["location"], date=card["date"], interest=card["interest"], summary=card["summary"])
else:
    st.info("결과를 찾지 못했습니다.")

st.markdown("""
    <style>
    .stButton>button {
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 20px;
        margin: 2px 0px 8px 0px;
    }
    </style>
    """, unsafe_allow_html=True)