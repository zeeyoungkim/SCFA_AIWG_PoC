import streamlit as st
import time

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
            LOGIN
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

    c1, c2 = st.columns([3,1])
    with c1:
        phone = st.text_input("Phone Number", placeholder="000-0000-0000")
    with c2:
        st.write("")
        sms_req_btn = st.button("SMS Request", use_container_width=True)

    if sms_req_btn:
        with sms_code_placeholder:
            st.warning("SMS Code is 112233")
            time.sleep(2)
        sms_code_placeholder.empty()

    c3, c4 = st.columns([3,1])
    with c3:
        sms = st.text_input("SMS Code", placeholder="000000")
    with c4:
        st.write("")
        sms_ok_btn = st.button("OK", use_container_width=True)
    
    if sms_ok_btn:
        with auth_placeholder:
            st.warning("User is authorized!!")
            time.sleep(2)
        auth_placeholder.empty()

with st.container():
    login_button = st.button("Login", use_container_width=True)
    register_button = st.button("Register", use_container_width=True)

    login_warn_placeholder = st.empty()

    if login_button:
        if not phone.strip() or not sms.strip():
            with login_warn_placeholder:
                st.warning("Please enter your phone number and SMS code.")
                time.sleep(2)
            login_warn_placeholder.empty()
        else:
            st.switch_page("pages/prompt.py")

    if register_button:
        st.switch_page("pages/registration.py")

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
