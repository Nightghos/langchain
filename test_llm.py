import streamlit as st
from langchain.llms import OpenAI

st.title('Quickstart App')

openai_api_key= st.sidebat.text_input('Open API key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startwith('sk-'):
        st.warning('Please check your OpenAI key!',icon='⚠')
    if submitted and openai_api_key.startwith('sk-'):
        generate_response(text)