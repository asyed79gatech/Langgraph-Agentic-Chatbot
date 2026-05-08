import streamlit as st
from src.langgraphagenticai.ui.streamlitui.uiconfigfile import Config

class LoadStreamlitUI:

    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlitui(self):
        st.set_page_config(page_title="👾 " + self.config.page_title(), layout="wide")
        st.header("👾 " + self.config.page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model", model_options)  
                self.user_controls["GROQ_API_KEY"] = st.session_state['GROQ_API_KEY'] = st.text_input("GROQ API Key", type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ API key to continue")

            usecase_options = self.config.use_case_options()
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options) 

        return self.user_controls