import streamlit as st
from streamlit_modal import Modal
import re

if "show_modal" not in st.session_state:
    st.session_state.show_modal = False

modal = Modal("Registration", key="modal", padding=20, max_width=450)

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

    nickname = st.text_input("Nickname", placeholder="Enter your nickname", key="user_id_input")

    col1, col2 = st.columns([1, 2])
    with col1:
        carrier = st.selectbox("Carrier *", ["KT", "NTT Docomo", "China Mobile"], key="carrier_input")
    with col2:
        phone = st.text_input("Phone Number *", placeholder="000-0000-0000", key="phone_input")

register_button = st.button("Register", use_container_width=True)

phone_pattern = r'^\d{3}-\d{4}-\d{4}$'

if register_button:
    if not phone.strip():
        st.warning("Enter your phone number!!")
    elif not re.match(phone_pattern, phone.strip()):
        st.warning("Enter the correct format of your phone number!!")
    else:
        st.session_state.show_modal = True
        modal.open()

if modal.is_open() and st.session_state.show_modal:
    with modal.container():
        st.write(f"User {nickname.upper() or ''} is registered successfully!!")
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
    }
    </style>
    """, unsafe_allow_html=True)