import streamlit as st
from streamlit_modal import Modal

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False
if "user_id" not in st.session_state:
    st.session_state.user_id = "aabbcc"
if "modal_is_open" not in st.session_state:
    st.session_state.modal_is_open = True

modal_1 = Modal("Confirm", key="modal_1", padding=20, max_width=300)

def enable_edit_mode():
    st.session_state.edit_mode = True

def disable_edit_mode_and_save():
    st.session_state.edit_mode = False
    st.session_state.user_id = st.session_state.user_id_input
    st.session_state.modal_is_open = True
    modal_1.open()

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

    phone = st.text_input("Phone Number", "111-222-3333", disabled=True)

    user_id = st.text_input("User ID", st.session_state.user_id, disabled=not st.session_state.edit_mode, key="user_id_input")

    if not st.session_state.edit_mode:
        st.button("Modify", use_container_width=True, on_click=enable_edit_mode)
    else:
        st.button("OK", use_container_width=True, on_click=disable_edit_mode_and_save)

if modal_1.is_open():
    with modal_1.container():
        st.write("User Info is modified successfully!!")
        if st.button("OK", use_container_width=True):
            if st.session_state.modal_is_open:
                st.session_state.modal_is_open = False
            else:
                modal_1.close()
