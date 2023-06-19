import streamlit as st
def set_openai_api_key(api_key: str):
   st.session_state["OPENAI_API_KEY"] = api_key

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Ask a question to get to know what we sell here \n"
        )
        
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