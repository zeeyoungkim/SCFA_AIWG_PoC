import streamlit as st
import time

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "agent", "content": "안녕하세요. K-Agent입니다! 무엇을 도와드릴까요?"}
    ]

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; height: 54px; margin-bottom: 24px; border-bottom: 1.5px solid #e8e8e8;">
        <div style="flex:1; display: flex; align-items: center;">
            <button style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-left: 4px;">
                &#8592;
            </button>
        </div>
        <div style="flex:2; text-align: center; font-size: 1.25rem; font-weight: 700; letter-spacing:0.03em;">
            KT 에이전트 (대화 예시)
        </div>
        <div style="flex:1; display: flex; justify-content: flex-end; align-items: center;">
            <button id="menu-btn" style="background: none; border: none; cursor: pointer; font-size: 1.7rem; padding-right: 4px;">
                &#9776;
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("프롬프트를 입력하세요..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # with st.spinner(text="Thinking...", show_time=False):
    #     time.sleep(3)

    if "예약" in prompt:
        with st.spinner(text="전달 중입니다...", show_time=False):
            time.sleep(3)
        agent_reply = "기다려주세요. 다른 에이전트로부터 확인해보겠습니다."
        
        with st.chat_message("agent"):
            st.write(agent_reply)
        
        with st.spinner(text="전달 중입니다...", show_time=False):
            time.sleep(3)
        agent_reply = "기다려주셔서 감사합니다. NTT 도코모는 7월 27일 2시~3시 사이에 가능하고 차이나모바일은 같은 날 3시에 가능합니다."
        
        with st.chat_message("agent"):
            st.write(agent_reply)
        st.session_state.messages.append({"role": "agent", "content": agent_reply})
    elif "가능" in prompt:
        with st.spinner(text="전달 중입니다...", show_time=False):
            time.sleep(3)
        agent_reply = "예약이 7월 27일 오후 3시로 확정되었습니다."
        
        with st.chat_message("agent"):
            st.write(agent_reply)
        st.session_state.messages.append({"role": "agent", "content": agent_reply})
    
    st.session_state.messages.append({"role": "agent", "content": agent_reply})
    
    # with st.chat_message("agent"):
    #     st.write(agent_reply)

### Sample Script
### I would like to have a reservation in the Italian restaurant between July 25th and July 27th.
### I might also be available at 3PM at that day. Please let them know.