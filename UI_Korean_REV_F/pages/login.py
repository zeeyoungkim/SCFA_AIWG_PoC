import streamlit as st
from streamlit_modal import Modal
import time
import re

if "sms_code_enabled" not in st.session_state:
    st.session_state.sms_code_enabled = False
if "show_login_modal" not in st.session_state:
    st.session_state.show_login_modal = False

login_modal = Modal("로그인 완료", key="login_modal", padding=20, max_width=450)

st.markdown("""
    <style>
        div.stButton > button {
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; height: 54px; margin-bottom: 24px; border-bottom: 1.5px solid #e8e8e8;">
        <div style="flex:1; display: flex; align-items: center;">
            <button style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-left: 4px;">
                &#8592;
            </button>
        </div>
        <div style="flex:2; text-align: center; font-size: 1.25rem; font-weight: 700; letter-spacing:0.03em;">
            로그인
        </div>
        <div style="flex:1; display: flex; justify-content: flex-end; align-items: center;">
            <button id="menu-btn" style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-right: 4px;">
                &#9776;
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    sms_code_placeholder = st.empty()
    auth_placeholder = st.empty()

    c1, c2 = st.columns([3, 1])
    with c1:
        phone = st.text_input("전화번호", placeholder="000-0000-0000")
    with c2:
        st.write("")
        sms_req_btn = st.button("SMS 코드", use_container_width=True)

    if sms_req_btn:
        st.session_state.sms_code_enabled = True
        with sms_code_placeholder:
            st.warning("SMS 코드는 112233입니다.")
            time.sleep(2)
        sms_code_placeholder.empty()

    c3, c4 = st.columns([3, 1])
    with c3:
        sms = st.text_input("SMS 코드", placeholder="000000", disabled=not st.session_state.sms_code_enabled)
    with c4:
        st.write("")
        sms_ok_btn = st.button("확인", use_container_width=True, disabled=not st.session_state.sms_code_enabled)

    if sms_ok_btn:
        with auth_placeholder:
            st.warning("사용자 인증이 완료되었습니다!!")
            time.sleep(2)
        auth_placeholder.empty()

with st.container():
    login_button = st.button("로그인", use_container_width=True)
    register_button = st.button("등록", use_container_width=True)

    login_warn_placeholder = st.empty()

    phone_pattern = r'^\d{3}-\d{4}-\d{4}$'

    if login_button:
        if not phone.strip():
            with login_warn_placeholder:
                st.warning("전화번호를 입력하세요!!")
                time.sleep(2)
            login_warn_placeholder.empty()
        elif not re.match(phone_pattern, phone.strip()):
            st.warning("포맷에 맞게 전화번호를 입력하세요!!")
        else:
            st.session_state.show_login_modal = True
            login_modal.open()

    if register_button:
        st.switch_page("pages/registration.py")

if login_modal.is_open() and st.session_state.show_login_modal:
    with login_modal.container():
        st.write("로그인이 정상적으로 완료되었습니다!")
        if st.button("확인", use_container_width=True, key="ok_in_login_modal"):
            st.session_state.show_login_modal = False
            st.switch_page("pages/prompt.py")

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
