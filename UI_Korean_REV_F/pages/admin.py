import streamlit as st
from streamlit_modal import Modal
from vega_datasets import data
from datetime import datetime, timedelta

if "api_keys" not in st.session_state:
    st.session_state.api_keys = [
        {
            "agent": "KT Agent",
            "key": "kt_agent",
            "status": "🟢 활성",
            "expired": "2025.07.29",
            "created": "2026.02.03",
        }
    ]

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; height: 54px; margin-bottom: 24px; border-bottom: 1.5px solid #e8e8e8;">
        <div style="flex:1; display: flex; align-items: center;">
            <button style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-left: 4px;">
                &#8592;
            </button>
        </div>
        <div style="flex:2; text-align: center; font-size: 1.25rem; font-weight: 700; letter-spacing:0.03em;">
            관리자
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
            "username": "kim",
            "registered": "2025-03-24",
            "phone": "111-222-3333",
            "carrier": "KT"
        },
        {
            "username": "lee",
            "registered": "2025-03-24",
            "phone": "111-222-3333",
            "carrier": "KT"
        },
        {
            "username": "takeshi",
            "registered": "2025-04-05",
            "phone": "222-333-4444",
            "carrier": "NTT Docomo"
        },
        {
            "username": "yuriko",
            "registered": "2025-04-05",
            "phone": "222-333-4444",
            "carrier": "NTT Docomo"
        },
        {
            "username": "kaixi",
            "registered": "2022-01-05",
            "phone": "444-5555-66666",
            "carrier": "China Mobile"
        },
    ]

with st.container(height=680, border=False):
    st.markdown("""
        <div style="background: #f7fafc; border-radius: 20px; padding: 30px 20px 20px 20px; margin-bottom: 24px;">
            <h2 style="text-align: left; font-weight: bold; color: #1a202c; margin-bottom: 16px;">
                📊 사용자 통계 (예시 차트)
            </h2>
    """, unsafe_allow_html=True)

    # st.divider()
    # source = data.barley()
    # st.bar_chart(source, x="year", y="yield", color="site", stack=False)
    # st.markdown("</div>", unsafe_allow_html=True)

    source = data.barley()
    xaxis = ['year', 'site', 'variety']
    yaxis = ['yield']

    colx, coly = st.columns(2)
    with colx:
        x_col = st.selectbox("X축", xaxis, index = 0)
    with coly:
        y_col = st.selectbox("Y축", yaxis, index = 0)
    
    st.bar_chart(source[[x_col, y_col]].groupby(x_col).mean(), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with st.container(height=680, border=False):
    st.markdown("""
        <div style="background: #fff; border-radius: 20px; padding: 28px 20px 16px 20px; box-shadow: 0 3px 12px 0 #ebedf0; margin-bottom: 8px;">
            <h2 style="font-weight: bold; color: #1a202c; margin-bottom: 18px; display: flex; align-items: center;">
                👥 사용자 리스트
            </h2>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns([1, 3], gap="small")
    with col1:
        carrier = st.selectbox(
            "통신사", 
            ("전체", "KT", "NTT Docomo", "China Mobile"),
            label_visibility="collapsed"
        )
    with col2:
        search = st.text_input(
            "사용자 리스트", 
            placeholder="사용자 검색...", 
            label_visibility="collapsed"
        )

    users = st.session_state.user_list

    if carrier != "전체":
        users = [u for u in users if u["carrier"] == carrier]
    if search:
        users = [u for u in users if search.lower() in u["username"].lower()]

    for idx, user in enumerate(users):
        user_col1, user_col2 = st.columns([7, 1], gap='medium')
        with user_col1:
            st.markdown(f"""
                <div style="padding: 10px 0;">
                    <span style="font-size: 18px; font-weight: bold;">{user['username']}</span>  
                    <span style="font-size: 13px; color: #6b7280; margin-left: 8px;">(등록일: {user['registered']})</span><br>
                    <span style="font-size: 15px; color: #555;">📞 {user['phone']}</span>
                    <span style="font-size: 15px; color: #555;">({user['carrier']})</span>
                </div>
            """, unsafe_allow_html=True)
        with user_col2:
            if st.button("삭제", key=f"delete_user_{user['username']}"):
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

api_modal = Modal("API 키 신규 발급", key="create_api_key", max_width=460)

with st.container():
    st.markdown("""
        <div style="background: #f7fafc; border-radius: 20px; padding: 30px 20px 20px 20px; margin-bottom: 24px;">
            <h2 style="text-align: left; font-weight: bold; color: #1a202c; margin-bottom: 16px;">
                🔑 API 키 관리
            </h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([8, 2])
    with col1:
        st.write("")
    with col2:
        new_key = st.button("신규 발급", use_container_width=True, type="primary")
        if new_key:
            api_modal.open()

if api_modal.is_open():
    with api_modal.container():
        with st.form("api_key_form", clear_on_submit=True):
            agent_name = st.text_input("AGENT 이름 *")
            key_name = st.text_input("KEY 이름 *")
            status = st.selectbox("KEY 값 상태", ["🟢 활성", "🔴 비활성"])
            expired_date = st.date_input("만료일", value=datetime.now() + timedelta(days=180))
            submitted = st.form_submit_button("확인", use_container_width=True)

            if submitted and agent_name.strip() and key_name.strip():
                st.session_state.api_keys.append({
                    "agent": agent_name,
                    "key": key_name,
                    "status": status,
                    "expired": expired_date.strftime("%Y.%m.%d"),
                    "created": datetime.now().strftime("%Y.%m.%d")
                })
                api_modal.close()

for idx, item in enumerate(st.session_state.api_keys):
    st.markdown("""
        <div style="background: #fff; border-radius: 16px; padding: 16px 24px; box-shadow: 4px 3px 10px rgba(0,0,0,0.06); margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-weight: bold; font-size: 20px; color: #2d3748;">AGENT 이름: {agent}</div>
                    <div style="font-size: 15px;">KEY 이름: {key}</div>
                    <div style="font-size: 15px;">만료일: {expired}</div>
                    <div style="font-size: 15px;">등록일: {created}</div>
                    <div style="font-size: 15px; color: red; font-weight: 500;"> 상태: {status}</div>
                </div>
                <button type="submit" 
                    style="
                        width: 150px;
                        padding: 6px 12px;
                        background-color: #e53e3e;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        cursor: pointer;
                        font-weight: bold;">
                    삭제
                </button>
            </div>
        </div>
    """.format(
        agent=item["agent"],
        key=item["key"],
        expired=item["expired"],
        created=item["created"],
        status=item["status"],
        idx=idx
    ), unsafe_allow_html=True)