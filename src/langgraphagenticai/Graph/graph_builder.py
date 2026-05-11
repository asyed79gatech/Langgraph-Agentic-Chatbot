
from langgraph.graph import StateGraph,START, END
from src.langgraphagenticai.State.state import State
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.Nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.Tools.web_search_tool import ChatbotTools
from src.langgraphagenticai.Nodes.web_search_node import ChatbotToolNode
from src.langgraphagenticai.Nodes.ai_news_node import AINewsNode


class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):

        """
        Creates a basic chatbot graph using Langgraph.
        This method initialized a chatbot node using the BasicChatbotNode class.
        And integrates it into the graph. The chatbot node is set as both the entry 
        and exit of the graph 
        """

        # Initialuze an object of the BasicChatbotNode class using the self.llm as the model
        self.basic_chtabot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chtabot_node.basic_chatbot)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def websearch_build_graph(self):

        """
        Creats a chatbot with webserach capabilities using using Langgraph.
        This method initialized the WebserachNode using the WebSearchNode class
        and itegrated it into the graph.
        """
        # Create an object of the ChatbotTools class
        obj_chatbot_tools = ChatbotTools()

        # Get all the tools available in a list
        tools = obj_chatbot_tools.get_tools()

        # Create a Node of the list of tools available
        tool_node = obj_chatbot_tools.create_tool_node()

        # Create an object of the ChatbotToolNode class 
        obj_chatbot_tool_node = ChatbotToolNode(self.llm, tools)

        

        # Add the nodes to the graph builder
        self.graph_builder.add_node("chatbot", obj_chatbot_tool_node.llm_with_tool_node)
        self.graph_builder.add_node("tools", tool_node)
        
        # Add the edges to the graph builder
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    
    def ai_news_build_graph(self):

        # Initialize the AINewsNode class using the LLM
        ai_news_node = AINewsNode(self.llm)

        # Add all the nodes
        self.graph_builder.add_node("fetch news", ai_news_node.fetch_news)
        self.graph_builder.add_node("summarizer", ai_news_node.summarize_news)
        self.graph_builder.add_node("saver", ai_news_node.save_news)

        # Add Edges
        self.graph_builder.set_entry_point("fetch news")
        self.graph_builder.add_edge("fetch news", "summarizer")
        self.graph_builder.add_edge("summarizer", "saver")
        self.graph_builder.add_edge("saver", END)




    def select_graph(self, usecase:str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Web Search":
            self.websearch_build_graph()
        elif usecase == "AI News":
            self.ai_news_build_graph()
        
        return self.graph_builder.compile()
        
        
