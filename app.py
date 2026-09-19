import streamlit as st
import ollama

APP_TITLE = "Ollama Streamlit App"
APP_ICON = "🤖"
MODEL_NAME = "llama3.2"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="centered"
)

st.title(f"{APP_ICON} {APP_TITLE}")
st.caption(f"Powered by Ollama • Model: {MODEL_NAME} • Runs locally")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content" : "Hello! I'm your AI assistant. How can I help you today?"
        }
    ]

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"]).write(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("what is on your mind?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        response_placeholder=st.empty()
        full_response=""

        stream=ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages,
            stream=True
        )

        for chunk in stream:
            if chunk['message']['content']:
                content=chunk['message']['content']
                full_response+=content
                response_placeholder.markdown(full_response + "▌")


            response_placeholder.markdown(full_response)


    st.session_state.messages.append({"role":"assistant","content":full_response})
