import streamlit as st

col1, col2 = st.columns([4, 1])

with col1:
    search = st.text_input(label="search", key="search_input", placeholder="Search...", label_visibility="hidden")
with col2:
    st.markdown("""
        <style>
            div.stButton > button {
                margin-top: 8px;
            }
        </style>
    """, unsafe_allow_html=True)
    st.button("Search", use_container_width=True, key="search_button")

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
        <div class="title">Location: { location }</div>
        <div class="desc">Date: { date }</div>
        <div class="desc">Interest: { interest }</div>
        <div class="desc">Summary: { summary }</div>
    </div>
    """, unsafe_allow_html=True)

cards = [
    {
        "location": "Japan",
        "date": "2025/05/02",
        "interest": "Cuisine",
        "summary": "The famous Sushi restaurant in Osaka"
    },
    {
        "location": "China",
        "date": "2025/07/30",
        "interest": "Museum",
        "summary": "The oldest historic museum in Shanghai"
    },
]

for card in cards:
    card_box(location=card["location"], date=card["date"], interest=card["interest"], summary=card["summary"])
