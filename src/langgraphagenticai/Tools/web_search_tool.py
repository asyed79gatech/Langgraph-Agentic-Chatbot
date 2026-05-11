from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools.tavily_search import TavilySearchResults
import os
import streamlit as st

class ChatbotTools:

    def __init__(self):
        pass


    def get_tools(self):
        """
        Creates a list of available tools that can be integrated with the chatbot LLM 
        """

        # Creating a tavily search tool
        try:
            tavily_api_key = os.environ["TAVILY_API_KEY"]
            if os.environ["TAVILY_API_KEY"] == "":
                st.error("Enter a valid Tavily API Key")

            tavily_search_tool = TavilySearchResults(max_results = 2)
        except Exception as e:
            raise ValueError(f"Tavily tool failed to load. Details: {e}")
        

        # Creating a list of all the tool
        self.tools = [tavily_search_tool]

        return self.tools
    

    def create_tool_node(self):
        """
        Creates a node of all the available tools to be integrated in a LangGraph
        """

        return ToolNode(self.tools)
 
            

