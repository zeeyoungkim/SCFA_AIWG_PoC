import streamlit as st
from vega_datasets import data

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; height: 54px; margin-bottom: 24px; border-bottom: 1.5px solid #e8e8e8;">
        <div style="flex:1; display: flex; align-items: center;">
            <button style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-left: 4px;">
                &#8592;
            </button>
        </div>
        <div style="flex:2; text-align: center; font-size: 1.25rem; font-weight: 700; letter-spacing:0.03em;">
            ADMIN
        </div>
        <div style="flex:1; display: flex; justify-content: flex-end; align-items: center;">
            <button id="menu-btn" style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-right: 4px;">
                &#9776;
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

if "user_list" not in st.session_state:
    st.session_state.user_list = [
        {
            "username": "kim_443",
            "registered": "2025-03-24",
            "phone": "111-222-3333",
            "carrier": "KT"
        },
        {
            "username": "park_443",
            "registered": "2025-03-24",
            "phone": "111-222-3333",
            "carrier": "KT"
        },
        {
            "username": "susan_123",
            "registered": "2025-04-05",
            "phone": "222-333-4444",
            "carrier": "NTT Docomo"
        },
        {
            "username": "jessie_222",
            "registered": "2022-01-05",
            "phone": "444-5555-66666",
            "carrier": "China Mobile"
        },
    ]

with st.container():
    st.markdown("""
        <div style="background: #f7fafc; border-radius: 20px; padding: 30px 20px 20px 20px; margin-bottom: 24px;">
            <h2 style="text-align: left; font-weight: bold; color: #1a202c; margin-bottom: 16px;">
                📊 Statistics
            </h2>
    """, unsafe_allow_html=True)

    st.divider()
    source = data.barley()
    st.bar_chart(source, x="year", y="yield", color="site", stack=False)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div style="background: #fff; border-radius: 20px; padding: 28px 20px 16px 20px; box-shadow: 0 3px 12px 0 #ebedf0; margin-bottom: 8px;">
        <h2 style="font-weight: bold; color: #1a202c; margin-bottom: 18px; display: flex; align-items: center;">
            👥 User List
        </h2>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 3], gap="small")
with col1:
    carrier = st.selectbox(
        "Carriers", 
        ("All", "KT", "NTT Docomo", "China Mobile"),
        label_visibility="collapsed"
    )
with col2:
    search = st.text_input(
        "User List", 
        placeholder="Search User...", 
        label_visibility="collapsed"
    )

users = st.session_state.user_list

if carrier != "All":
    users = [u for u in users if u["carrier"] == carrier]
if search:
    users = [u for u in users if search.lower() in u["username"].lower()]

for idx, user in enumerate(users):
    user_col1, user_col2 = st.columns([3, 1], gap="medium")
    with user_col1:
        st.markdown(f"""
            <div style="padding: 10px 0;">
                <span style="font-size: 18px; font-weight: bold;">{user['username']}</span>  
                <span style="font-size: 13px; color: #6b7280; margin-left: 8px;">(Registered: {user['registered']})</span><br>
                <span style="font-size: 15px; color: #555;">📞 {user['phone']}</span>
                <span style="font-size: 15px; color: #555;">({user['carrier']})</span>
            </div>
        """, unsafe_allow_html=True)
    with user_col2:
        if st.button("Delete", key=f"delete_user_{user['username']}"):
            st.session_state.user_list = [
                u for u in st.session_state.user_list if u["username"] != user["username"]
            ]
            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

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