import streamlit as st

guide_images = [
    "media/guide1.png",
    "media/guide2.png",
    "media/guide3.png"
]

if 'guide_idx' not in st.session_state:
    st.session_state.guide_idx = 0

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Previous", key="prev", use_container_width=True, disabled=st.session_state.guide_idx == 0):
        st.session_state.guide_idx = max(0, st.session_state.guide_idx - 1)
with col2:
    if st.button("Guide 1", key="g1", use_container_width=True):
        st.session_state.guide_idx = 0
with col3:
    if st.button("Guide 2", key="g2", use_container_width=True):
        st.session_state.guide_idx = 1
with col4:
    if st.button("Guide 3", key="g3", use_container_width=True):
        st.session_state.guide_idx = 2
with col5:
    if st.button("Next", key="next", use_container_width=True, disabled=st.session_state.guide_idx == len(guide_images) - 1):
        st.session_state.guide_idx = min(len(guide_images) - 1, st.session_state.guide_idx + 1)

st.image(guide_images[st.session_state.guide_idx], use_container_width=True)

goToApp = st.button("OK", type="primary", use_container_width=True)

if goToApp:
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