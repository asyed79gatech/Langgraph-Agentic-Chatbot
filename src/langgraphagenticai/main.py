import streamlit as st
from src.langgraphagenticai.ui.streamlitui.load_ui import LoadStreamlitUI

def load_agenticai_app():

    """
    Loads and runs the agentic ai application with streamlit UI. 
    This function initializes the UI, handles user input, configures the LLM model, sets up
    the graph based on the selected usecase and displays the output while implementing
    exception handling for robustness 
    """

    # Load UI

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlitui()

    if not user_input:
        st.error("Failed to load user input from UI")

        return
    user_message = st.chat_input("Enter your message:")
