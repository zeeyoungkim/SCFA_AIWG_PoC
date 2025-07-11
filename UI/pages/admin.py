import streamlit as st
from vega_datasets import data

with st.container():
    st.markdown("""
        <div style="background: #f7fafc; border-radius: 20px; padding: 30px 20px 20px 20px; margin-bottom: 24px;">
            <h2 style="text-align: left; font-weight: bold; color: #1a202c; margin-bottom: 16px;">
                📊 Statistics
            </h2>
    """, unsafe_allow_html=True)

    st.divider()
    
    source = data.barley()
    st.bar_chart(source, x="year", y="yield", color="site", stack=False)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div style="background: #fff; border-radius: 20px; padding: 28px 20px 16px 20px; box-shadow: 0 3px 12px 0 #ebedf0; margin-bottom: 8px;">
        <h2 style="font-weight: bold; color: #1a202c; margin-bottom: 18px; display: flex; align-items: center;">
            👥 User List
        </h2>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 3], gap="small")
with col1:
    carrier = st.selectbox(
        "Carriers", 
        ("KT", "NTT Docomo", "China Mobile"),
        label_visibility="collapsed"
    )
with col2:
    search = st.text_input(
        "User List", 
        placeholder="Search User...", 
        label_visibility="collapsed"
    )

user_col1, user_col2 = st.columns([3, 1], gap="medium")

with user_col1:
    st.markdown("""
        <div style="padding: 10px 0;">
            <span style="font-size: 18px; font-weight: bold;">james_443</span>  
            <span style="font-size: 13px; color: #6b7280; margin-left: 8px;">(Registered: 2025-03-24)</span><br>
            <span style="font-size: 15px; color: #555;">📞 111-222-3333</span>
        </div>
    """, unsafe_allow_html=True)

with user_col2:
    st.button("Delete", key="delete_user_1", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

user_col1, user_col2 = st.columns([3, 1], gap="medium")
with user_col1:
    st.markdown("""
        <div style="padding: 10px 0;">
            <span style="font-size: 18px; font-weight: bold;">susan_123</span>  
            <span style="font-size: 13px; color: #6b7280; margin-left: 8px;">(Registered: 2025-04-05)</span><br>
            <span style="font-size: 15px; color: #555;">📞 222-333-4444</span>
        </div>
    """, unsafe_allow_html=True)
with user_col2:
    st.button("Delete", key="delete_user_2", use_container_width=True)
