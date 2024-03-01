'''                     Conversational Q&A Chatbot                                                              '''
# Importing Necessary Libraries
import os
import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

# Loading The environment variable
load_dotenv()

chat_llm=ChatOpenAI(openai_api_key=os.environ['OPENAI_API_KEY'],temperature=0.7,model='gpt-3.5-turbo')

# Initializing the Session
if 'flowmessage' not in st.session_state:
    st.session_state['flowmessage']=[
        SystemMessage(content="You are a conversational AI assistant"),
        ]

# Getting response from the model
def get_response(question):
    st.session_state['flowmessage'].append(HumanMessage(content=question))
    answer=chat_llm(st.session_state['flowmessage'])
    st.session_state['flowmessage'].append(AIMessage(content=answer.content))
    return answer.content


# Streamlit UI
st.set_page_config(page_title="Conversational Q&A ChatBot")
st.header("Hey, Let's Chat")

# Input from the user
input=st.text_input("",key="input")
response=get_response(input)
submit=st.button("Ask")

# if button is clicked
if submit:
    st.subheader("")
    st.write(response)

