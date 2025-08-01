import streamlit as st
import time

if "menu_open" not in st.session_state:
    st.session_state.menu_open = False
if "menu_closing" not in st.session_state:
    st.session_state.menu_closing = False

with st.container():
    st.markdown("### 서브메뉴 동작")
    if st.button("메뉴 열기/닫기", key="menu_toggle_btn"):
        if st.session_state.menu_open:
            st.session_state.menu_closing = True
        else:
            st.session_state.menu_open = True
            st.session_state.menu_closing = False

animation_class = ""

if st.session_state.menu_open and not st.session_state.menu_closing:
    animation_class = "slideIn"
elif st.session_state.menu_closing:
    animation_class = "slideOut"

# 스타일 정의
if st.session_state.menu_open or st.session_state.menu_closing:
    st.markdown(f"""
    <style>
    @keyframes slideIn {{
        from {{ transform: translateX(100%); opacity: 0; }}
        to {{ transform: translateX(0); opacity: 1; }}
    }}
    @keyframes slideOut {{
        from {{ transform: translateX(0); opacity: 1; }}
        to {{ transform: translateX(100%); opacity: 0; }}
    }}
    .sidebar-menu {{
        animation: {animation_class} 0.5s ease forwards;
        position: fixed;
        top: 54px;
        right: 0;
        width: 260px;
        height: 100%;
        background: linear-gradient(to bottom right, #ffffff, #f2f5fa);
        box-shadow: -4px 0 12px rgba(0,0,0,0.1);
        padding: 32px 24px;
        font-family: 'Apple SD Gothic Neo', sans-serif;
        z-index: 9999;
        overflow-y: auto;
    }}
    .sidebar-menu .profile-img {{
        display: block;
        margin: 20px auto 0 auto;
        border-radius: 50%;
        width: 90px;
        height: 90px;
        object-fit: cover;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }}
    .sidebar-menu .nickname {{
        text-align: center;
        margin-top: 12px;
        font-weight: 600;
        font-size: 18px;
        color: #2c3e50;
        border-bottom: 1px solid #e0e0e0;
        padding-bottom: 16px;
    }}
    .sidebar-menu .menu {{
        margin-top: 24px;
        list-style: none;
        padding: 0;
    }}
    .sidebar-menu .menu li {{
        margin-bottom: 0;
        border-bottom: 1px solid #e5e7eb;
    }}
    .sidebar-menu .menu li a {{
        text-decoration: none;
        font-size: 16px;
        color: #34495e;
        padding: 12px;
        display: block;
        border-radius: 4px;
        transition: all 0.2s ease;
        width: 100%;
        box-sizing: border-box;
    }}
    .sidebar-menu .menu li a:hover {{
        background-color: #eaf1f8;
        color: #1f5faa;
    }}
    .sidebar-menu .logout {{
        margin-top: 135px;
        padding-top: 16px;
        text-align: center;
    }}
    .sidebar-menu .logout button {{
        background-color: #e74c3c;
        color: white;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        font-size: 15px;
        border-radius: 6px;
        cursor: pointer;
        transition: background 0.2s ease;
        width: 100%;
        box-sizing: border-box;
    }}
    .sidebar-menu .logout button:hover {{
        background-color: #c0392b;
    }}
    </style>

    <div class="sidebar-menu">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="profile-img" title="프로필 이미지입니다." />
        <div class="nickname" title="사용자 닉네임입니다.">테스트</div>
        <ul class="menu">
            <li><a href="#" title="사용자 검색 내역 메뉴로 이동합니다.">🕘 히스토리</a></li>
            <li><a href="#" title="사용자 설정 메뉴로 이동합니다.">⚙️ 사용자 설정</a></li>
            <li><a href="#" title="관리자 메뉴로 이동합니다.">🛠 관리자</a></li>
        </ul>
        <div class="logout">
            <button title="현재 계정에서 로그아웃합니다.">로그아웃</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.menu_closing:
    time.sleep(0.5)
    st.session_state.menu_open = False
    st.session_state.menu_closing = False
    st.rerun()
