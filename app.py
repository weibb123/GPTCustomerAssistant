# bring in streamlit for UI/app interface
import streamlit as st
from streamlit_chat import message
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain
from component import sidebar
from langchain.memory import ConversationBufferMemory
# Import os/file to set API key
import os
import json
from key import code
from product_info import output_string # will be used as context
os.environ["OPENAI_API_KEY"] = code

context = output_string

sidebar()

# template / prompt
template = """I want you to act as a customer service assistant for a
large electronic store. Respond in a friendly and helpful tone, with very concise answers.
Make sure to ask the user relevant follow up questions.

Given the context, these are the allowed products
Do not assume, from the name of the product, any features or attributes such as relative quality or price.
If users type something not related to the allowed products \
Please say "Sorry! I am unable to complete this request."
Please keep all response to less than 100 tokens.
{context}

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input", "context"],
    template=template
)

# Initialization
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory(
        memory_key="chat_history", input_key="human_input"
    )

# LLM chain to make responses
llm = LLMChain(
             llm = OpenAI(),
             prompt = prompt,
             memory=st.session_state['memory'],
             )

# UI SECTION
st.title('GPT Customer Service Demo💻')
st.markdown("""
Welcome! Come talk with the customer assistant to learn about what we sell here.
\
This is a demo of leveraging GPT to build a end to end customer service system
"""
)

# container for chat history
response_container = st.container()
# container for text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        if not st.session_state.get("api_key_configured")
        response = llm.predict(human_input=user_input, context=context)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(response)
        
        
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

           






    




