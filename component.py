import streamlit as st
def set_openai_api_key(api_key: str):
   st.session_state["OPENAI_API_KEY"] = api_key

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API Key](https://platform.openai.com/account/api-keys) below🔑\n"
            "2. Ask a question to get to know what we sell here \n"
        )
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI Key here",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )
        if api_key:
            set_openai_api_key(api_key)
        
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "GPT Customer Assistant allows you to get to know more about the products being sell"
            "Allow customers to gain quick information and faster checkout"
            "Note: This app is only a demonstration of using GPT. This chatbot does not sell anything"
        )
        st.markdown(
            "This tool is a work in progress"
        )