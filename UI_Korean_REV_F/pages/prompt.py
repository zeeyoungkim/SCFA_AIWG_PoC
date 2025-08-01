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
        agent_reply_1 = "기다려주세요. 다른 에이전트로부터 확인해보겠습니다."
        
        with st.chat_message("agent"):
            st.write(agent_reply_1)
        
        st.session_state.messages.append({"role": "agent", "content": agent_reply_1})
        
        with st.spinner(text="전달 중입니다...", show_time=False):
            time.sleep(3)
        agent_reply_2 = "기다려주셔서 감사합니다. NTT 사용자는 7월 27일 오후 2시에서 3시 사이에 가능하고 차이나모바일 사용자는 7월 27일 오후 3시에만 가능합니다."
        
        with st.chat_message("agent"):
            st.write(agent_reply_2)

        st.session_state.messages.append({"role": "agent", "content": agent_reply_2})
    elif "가능" in prompt:
        with st.spinner(text="전달 중입니다...", show_time=False):
            time.sleep(3)
        agent_reply_3 = "예약이 7월 27일 오후 3시로 확정되었습니다. 확정된 일정으로 전달드립니다."

        with st.chat_message("agent"):
            st.write(agent_reply_3)
        
        st.session_state.messages.append({"role": "agent", "content": agent_reply_3})
    
        st.markdown("""
            <style>
                .agent-card {
                    background: #f6f9fc;
                    border: 1.5px solid #e3e8ee;
                    border-radius: 17px;
                    box-shadow: 0 2px 10px rgba(40, 80, 150, 0.06);
                    padding: 22px 28px 15px 28px;
                    margin: 24px 0 12px 0;
                    font-size: 1.07rem;
                    color: #2d3748;
                    font-family: 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
                }
                .agent-card .card-title {
                    font-size:1.09rem;
                    font-weight:600;
                    margin-bottom:8px;
                    color:#2563eb;
                }
                .agent-card .card-row {
                    margin-bottom: 7px;
                }
            </style>
            
            <div class="agent-card">
                <div class="card-title">✅ 예약 확정 안내</div>
                <div class="card-row"><b>예약일시</b>: 25년 7월 27일 오후 3시</div>
                <div class="card-row"><b>장소</b>: 북경오리 레스토랑</div>
                <div class="card-row"><b>인원수</b>: 6명</div>
                <div class="card-row"><b>참석자</b>: Kim, Lee (KT), Takeshi, Yuriko, Issei (NTT), Kaixi (CMCC)</div>
            </div>
        """, unsafe_allow_html=True)
    
    # st.session_state.messages.append({"role": "agent", "content": agent_reply})
    
    # with st.chat_message("agent"):
    #     st.write(agent_reply)

### Sample Script
### I would like to have a reservation in the Italian restaurant between July 25th and July 27th.
### I might also be available at 3PM at that day. Please let them know.