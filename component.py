import streamlit as st


def set_openai_api_key(api_key: str):
   st.session_state["OPENAI_API_KEY"] = api_key

def sidebar():
    with st.sidebar:
        st.markdown("## How to use\n"
                    "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"
                    "2. Ask a question to get to know what we sell here \n")
        API_KEY = st.text_input("OpenAI API Key",
                                            placeholder="Paste your OpenAI API key here (sk-...)",
                                            type="password")
        
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "GPT Customer Assistant allows you to get to know more about the products being sell"
            "Allow customers to gain quick information and faster checkout"
            "Note: This app is only a demonstration of using GPT. This chatbot does not sell anything"
        )
        st.markdown("---")
        st.markdown("Privacy")
        st.markdown(
            "Your conversation and API key will not saved at all."
        )
        st.markdown("This tool is a work in progress")

        if API_KEY:
            set_openai_api_key(API_KEY)
        
