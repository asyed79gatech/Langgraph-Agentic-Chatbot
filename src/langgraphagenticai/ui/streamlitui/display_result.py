import json
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import streamlit as st

class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            for event in graph.stream({"messages": ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value["messages"])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)


        elif usecase == "Chatbot with Web Search":
            initial_state = self.user_message
            res = graph.invoke(initial_state)
            for msg in res["messages"]:
                if type(msg) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(msg.content)
                elif type(msg) == ToolMessage:
                    with st.chat_message("AI"):
                        st.write("Tool call Start")
                        st.write(msg.content)
                        st.write("Tool Call End")
                elif type(msg) == AIMessage and msg.content:
                    with st.chat_message("Assistant"):
                        st.write(msg.content)



        elif usecase == "AI News":
            frequency = self.user_message
            print(frequency)
            res = graph.invoke({"messages": frequency})
            try:
                # Read the markdown file from the save location
                AI_NEWS_PATH = f"./AI News/{frequency}_summary.md"
                with open(AI_NEWS_PATH, "r") as f:
                    markdown_content = f.read()

                # Display the markdown content on streamlit ui
                st.markdown(markdown_content, unsafe_allow_html=True)
            except FileNotFoundError:
                st.error(f"News not generated or file not found {AI_NEWS_PATH}")

            except Exception as e:
                st.error(f"An error occurred. Details: {e}")




