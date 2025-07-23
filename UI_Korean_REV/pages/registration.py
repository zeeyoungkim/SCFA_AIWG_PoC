import streamlit as st
from streamlit_modal import Modal
import re
import time

if "show_modal" not in st.session_state:
    st.session_state.show_modal = False
if "sms_code_enabled" not in st.session_state:
    st.session_state.sms_code_enabled = False

modal = Modal("등록", key="modal", padding=20, max_width=450)

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; height: 54px; margin-bottom: 24px; border-bottom: 1.5px solid #e8e8e8;">
        <div style="flex:1; display: flex; align-items: center;">
            <button style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-left: 4px;">
                &#8592;
            </button>
        </div>
        <div style="flex:2; text-align: center; font-size: 1.25rem; font-weight: 700; letter-spacing:0.03em;">
            사용자 등록
        </div>
        <div style="flex:1; display: flex; justify-content: flex-end; align-items: center;">
            <button id="menu-btn" style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-right: 4px;">
                &#9776;
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <style>
    .avatar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 16px;
    }
    .avatar-img {
        width: 120px;
        height: 120px;
        object-fit: cover;
        border-radius: 50%;
        border: 2px solid #ddd;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)
    
    avatar_html = '<div class="avatar-container"><img class="avatar-img" src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="default-avatar"></div>'
    st.markdown(avatar_html, unsafe_allow_html=True)

    with st.container():
        sms_code_placeholder = st.empty()
        auth_placeholder = st.empty()

        nickname = st.text_input("닉네임", placeholder="닉네임을 입력하세요", key="user_id_input")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            carrier = st.selectbox("통신사 *", ["KT", "NTT Docomo", "China Mobile"], key="carrier_input")
        with col2:
            phone = st.text_input("전화번호 *", placeholder="000-0000-0000", key="phone_input")
        with col3:
            st.write("")
            sms_req_btn = st.button("SMS 코드", use_container_width=True)
        
        if sms_req_btn:
            st.session_state.sms_code_enabled = True

            with sms_code_placeholder:
                st.warning("SMS 코드는 112233입니다.")
                time.sleep(2)
            sms_code_placeholder.empty()
        
        col4, col5 = st.columns([3, 1])
        with col4:
            sms = st.text_input("SMS 코드", placeholder="000000", disabled=not st.session_state.sms_code_enabled)
        with col5:
            st.write("")
            sms_ok_btn = st.button("확인", use_container_width=True, disabled=not st.session_state.sms_code_enabled)
    
    if sms_ok_btn:
        with auth_placeholder:
            st.warning("사용자 인증이 완료되었습니다!!")
            time.sleep(2)
        auth_placeholder.empty()

register_button = st.button("등록", use_container_width=True)

phone_pattern = r'^\d{3}-\d{4}-\d{4}$'

if register_button:
    if not phone.strip():
        st.warning("전화번호를 입력하세요!!")
    elif not re.match(phone_pattern, phone.strip()):
        st.warning("포맷에 맞게 전화번호를 입력하세요!!")
    else:
        st.session_state.show_modal = True
        modal.open()

if modal.is_open() and st.session_state.show_modal:
    with modal.container():
        st.write(f"사용자 {nickname.upper() or ''}가 성공적으로 등록되었습니다!!")
        if st.button("OK", use_container_width=True, key="ok_in_modal"):
            st.session_state.show_modal = False
            st.switch_page("pages/login.py")

st.markdown("""
    <style>
    .stButton>button {
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 20px;
        margin: 2px 0px 8px 0px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)