import streamlit as st
import time

st.markdown("""
    <style>
        div.stButton > button {
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    c1, c2 = st.columns([3,1])

    with c1:
        phone = st.text_input("Phone Number", placeholder="000-0000-0000")
    with c2:
        st.write("")
        sms_req_btn = st.button("SMS Request", use_container_width=True)
    
    if sms_req_btn:
        time.sleep(2)
        st.warning("SMS Code is 112233")


    c3, c4 = st.columns([3,1])
    
    with c3:
        sms = st.text_input("SMS Code", placeholder="000000")
    with c4:
        st.write("")
        sms_ok_btn = st.button("OK", use_container_width=True)
    
    if sms_ok_btn:
        time.sleep(2)
        st.warning("User is authorized!!")

with st.container():
    login_button = st.button("Login", use_container_width=True)
    register_button = st.button("Register", use_container_width=True)

    if register_button:
        st.switch_page("pages/registration.py")
    if login_button:
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