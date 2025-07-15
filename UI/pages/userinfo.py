import streamlit as st
from streamlit_modal import Modal

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; height: 54px; margin-bottom: 24px; border-bottom: 1.5px solid #e8e8e8;">
        <div style="flex:1; display: flex; align-items: center;">
            <button style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-left: 4px;">
                &#8592;
            </button>
        </div>
        <div style="flex:2; text-align: center; font-size: 1.25rem; font-weight: 700; letter-spacing:0.03em;">
            USER SETTING
        </div>
        <div style="flex:1; display: flex; justify-content: flex-end; align-items: center;">
            <button id="menu-btn" style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-right: 4px;">
                &#9776;
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False
if "user_id" not in st.session_state:
    st.session_state.user_id = "aabbcc"
if "modal_is_open" not in st.session_state:
    st.session_state.modal_is_open = True

modal_1 = Modal("Confirm", key="modal_1", padding=20, max_width=450)

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