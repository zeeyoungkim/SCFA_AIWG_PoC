import streamlit as st
import time

st.session_state.messages = [
    {"role": "agent", "content": "Hello! What can I do for you?"}
]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Enter prompt..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner(text="Thinking...", show_time=False):
        time.sleep(3)

    agent_reply = "OK. Please share some detailed location for the recommendation."
    st.session_state.messages.append({"role": "agent", "content": agent_reply})
    
    with st.chat_message("agent"):
        st.write(agent_reply)
