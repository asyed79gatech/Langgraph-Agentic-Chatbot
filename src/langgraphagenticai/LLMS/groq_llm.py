import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:

    def __init__(self, user_controls_inputs):
        self.user_controls_inputs = user_controls_inputs

    
    def get_llm_model(self):

        try:
            qroq_api_key = self.user_controls_inputs["GROQ_API_KEY"]
            groq_llm_selection = self.user_controls_inputs["selected_groq_model"]

            if qroq_api_key == "" and os.environ["GROQ_API_KEY"] == "":
                st.error("Please Enter a valid API Key")

            llm = ChatGroq(api_key=qroq_api_key, model=groq_llm_selection)
        except Exception as e:
            raise ValueError("Error occurred with Exception: {e}")
        return llm





        