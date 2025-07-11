import streamlit as st
import time

with st.container():
    st.image("media/title.svg", use_container_width=True)
    st.image("media/trip.png", use_container_width=True)

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        ko_user = st.button("한국어 사용자", type="primary", use_container_width=True)
        if ko_user:
            ko_placeholder = st.empty()
            with ko_placeholder:
                st.warning("한국어 서비스로 이동합니다.", width="stretch")

            time.sleep(2)
            ko_placeholder.empty()
            time.sleep(1)
            st.switch_page("pages/userguide.py")
    
    with col2:
        jp_user = st.button("日本のユーザー", type="primary", use_container_width=True)

        if jp_user:
            jp_placeholder = st.empty()
            with jp_placeholder:
                st.warning("日本語サービスは準備中です。")

            time.sleep(2)
            jp_placeholder.empty()
    
    with col3:
        cn_user = st.button("中国用户", type="primary", use_container_width=True)

        if cn_user:
            cn_placeholder = st.empty()
            with cn_placeholder:
                st.warning("中文服务正在筹备中。")

            time.sleep(2)
            cn_placeholder.empty()