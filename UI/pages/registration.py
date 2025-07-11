import streamlit as st
from streamlit_modal import Modal

if "show_modal" not in st.session_state:
    st.session_state.show_modal = False

modal = Modal("Confirm", key="modal", padding=20, max_width=300)

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

    user_id = st.text_input("User ID", placeholder="Enter your ID", key="user_id_input")
    phone = st.text_input("Phone Number *", placeholder="Enter your Phone Number", key="phone_input")

register_button = st.button("Register", use_container_width=True)

if register_button and phone.strip():
    st.session_state.show_modal = True
    modal.open()

if modal.is_open() and st.session_state.show_modal:
    with modal.container():
        st.write(f"User '{user_id or '...'}' is registered successfully!!")
        if st.button("OK", use_container_width=True, key="ok_in_modal"):
            st.session_state.show_modal = False
            st.switch_page("pages/login.py")