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

def get_error_message(error):
    error_text = str(error).lower()
    status_code = getattr(error, "status_code", None)

    if status_code == 404 or (
        "model" in error_text and "not found" in error_text
    ):
        return (
            f"Model '{MODEL_NAME}' is not installed. "
            f"Run `ollama pull {MODEL_NAME}` and try again."
        )

    if isinstance(error, (ConnectionError, TimeoutError, OSError)):
        return "Ollama is unavailable. Start Ollama and try again."

    if "connection" in error_text or "connect" in error_text:
        return "Ollama is unavailable. Start Ollama and try again."

    return "The request failed. Check Ollama and try again."


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content" : "Hello! I'm your AI assistant. How can I help you today?"
        }
    ]
if "last_error" not in st.session_state:
    st.session_state.last_error = None
if "retry_request" not in st.session_state:
    st.session_state.retry_request = False

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"]).write(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])

def request_response():
    response_placeholder = st.empty()
    full_response = ""

    try:
        stream = ollama.chat(
            model=MODEL_NAME,
            messages=st.session_state.messages,
            stream=True
        )

        for chunk in stream:
            content = chunk["message"]["content"]

            if content:
                full_response += content
                response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    except Exception as error:
        response_placeholder.empty()
        st.session_state.last_error = get_error_message(error)
        st.session_state.retry_request = True
        st.rerun()

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })
    st.session_state.last_error = None
    st.session_state.retry_request = False


if st.session_state.retry_request:
    st.error(f"Unable to generate a response. {st.session_state.last_error}")

    if st.button("Retry", type="primary"):
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                request_response()


if prompt := st.chat_input("What is on your mind?"):
    st.session_state.last_error = None
    st.session_state.retry_request = False
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            request_response()
