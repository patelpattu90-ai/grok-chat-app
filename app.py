import streamlit as st
from groq_client import chat_with_groq


st.set_page_config(page_title="Grok Chat")
st.title("🤖 Grok Chat")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask Grok...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        reply = chat_with_groq(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)




