
from langgraph.graph import StateGraph,START, END
from src.langgraphagenticai.State.state import State
from src.langgraphagenticai.Nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):

        """
        Creates a basic chatbot graph usinf Langgraph.
        This method initialized a chatbot node using the BasicChatbotNode class.
        And integrates it into the graph. The chatbot node is set as both the entry 
        and exit of the graph 
        """

        # Initialuze an object of the BasicChatbotNode class using the self.llm as the model
        self.basic_chtabot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chtabot_node.basic_chatbot)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def select_graph(self, usecase:str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()
        
        
