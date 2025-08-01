import streamlit as st
import time

if "user_lang_clicked" not in st.session_state:
    st.session_state.user_lang_clicked = None
if "show_warning" not in st.session_state:
    st.session_state.show_warning = False

with st.container():
    st.image("media/title.svg", use_container_width=True)
    st.image("media/trip.png", use_container_width=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("한국어 사용자", type="primary", use_container_width=True):
            st.session_state.user_lang_clicked = "ko"
            st.session_state.show_warning = True
    with col2:
        if st.button("日本のユーザー", type="primary", use_container_width=True):
            st.session_state.user_lang_clicked = "jp"
            st.session_state.show_warning = True
    with col3:
        if st.button("中国用户", type="primary", use_container_width=True):
            st.session_state.user_lang_clicked = "cn"
            st.session_state.show_warning = True

warning_placeholder = st.empty()

if st.session_state.show_warning:
    lang = st.session_state.user_lang_clicked
    if lang == "ko":
        msg = "한국어 서비스로 이동합니다. (Korean provided)"
        with warning_placeholder:
            st.warning(msg)
        time.sleep(2)
        warning_placeholder.empty()
        st.session_state.show_warning = False
        st.session_state.user_lang_clicked = None
        st.switch_page("pages/userguide.py")
    elif lang == "jp":
        msg = "日本語サービスは準備中です。 (Japanese provided)"
        with warning_placeholder:
            st.warning(msg)
        time.sleep(2)
        warning_placeholder.empty()
        st.session_state.show_warning = False
        st.session_state.user_lang_clicked = None
    elif lang == "cn":
        msg = "中文服务正在筹备中。 (Chinese provided)"
        with warning_placeholder:
            st.warning(msg)
        time.sleep(2)
        warning_placeholder.empty()
        st.session_state.show_warning = False
        st.session_state.user_lang_clicked = None

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
