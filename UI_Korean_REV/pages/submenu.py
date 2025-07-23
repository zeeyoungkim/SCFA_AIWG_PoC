import streamlit as st

st.markdown("""
<style>
.sidebar-menu {
    position: fixed;
    top: 45px;
    right: 0;
    width: 260px;
    height: 100%;
    background: linear-gradient(to bottom right, #ffffff, #f2f5fa);
    box-shadow: -4px 0 12px rgba(0,0,0,0.1);
    padding: 32px 24px;
    font-family: 'Apple SD Gothic Neo', sans-serif;
    z-index: 9999;
    overflow-y: auto;
}

.sidebar-menu .profile-img {
    display: block;
    margin: 20px auto 0 auto;
    border-radius: 50%;
    width: 90px;
    height: 90px;
    object-fit: cover;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}

.sidebar-menu .nickname {
    text-align: center;
    margin-top: 12px;
    font-weight: 600;
    font-size: 18px;
    color: #2c3e50;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 16px;
}

.sidebar-menu .menu {
    margin-top: 24px;
    list-style: none;
    padding: 0;
}

.sidebar-menu .menu li {
    margin-bottom: 0;
    border-bottom: 1px solid #e5e7eb;
}

.sidebar-menu .menu li a {
    text-decoration: none;
    font-size: 16px;
    color: #34495e;
    padding: 12px;
    display: block;
    border-radius: 4px;
    transition: all 0.2s ease;
    width: 100%;
    box-sizing: border-box;
}

.sidebar-menu .menu li a:hover {
    background-color: #eaf1f8;
    color: #1f5faa;
}

.sidebar-menu .logout {
    margin-top: 135px;
    padding-top: 16px;
    # border-top: 1px solid #dcdfe4;
    text-align: center;
}

.sidebar-menu .logout button {
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
}

.sidebar-menu .logout button:hover {
    background-color: #c0392b;
}
</style>

<div class="sidebar-menu">
    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="profile-img" />
    <div class="nickname">aabbcc11</div>
    <ul class="menu">
        <li><a href="#">🕘 히스토리</a></li>
        <li><a href="#">⚙️ 사용자 설정</a></li>
        <li><a href="#">🛠 관리자</a></li>
    </ul>
    <div class="logout">
        <button>로그아웃</button>
    </div>
</div>
""", unsafe_allow_html=True)
