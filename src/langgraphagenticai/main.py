import streamlit as st
from src.langgraphagenticai.ui.streamlitui.load_ui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groq_llm import GroqLLM
from src.langgraphagenticai.Graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

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
    
    if st.session_state.IsFetchButtonPressed == True:
        user_message = st.session_state.time_frame
    else: 
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:

            # Initialize the LLM model using the GroqLLM class
            model_initializer = GroqLLM(user_input)
            model = model_initializer.get_llm_model()
            if not model:
                st.error("Model was unable to load")


            # Extract the selected use case from the user_input
            usecase = user_input["selected_usecase"]
            if not usecase:
                st.error("No usecase selected")
                return

            # Initialize an object of GraphBuilder
            graph_builder = GraphBuilder(model)
            try:
                # Run the approprate graph based on the usecase
                graph = graph_builder.select_graph(usecase=usecase)
                print("Graph created")

                # Return the result of the graph run to the UI
                DisplayResultStreamlit(usecase=usecase, user_message=user_message, graph=graph).display_result_ui()
            except Exception as e:
                st.error(f"Graph failed to set up. Details: {e}")
                
        except Exception as e:
            st.error(f"Graph was unable to execute. Details: {e}")

                    
        except Exception as e:
            raise ValueError(f"Something went wrong. Details: {e}")
