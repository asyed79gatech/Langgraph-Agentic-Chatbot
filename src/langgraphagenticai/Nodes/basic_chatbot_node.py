
from src.langgraphagenticai.State.state import State

class BasicChatbotNode:
    """
    Creates a chatbot node for a langgraph 
    """

    def __init__(self, model):
        self.llm = model

    def basic_chatbot(self, state:State):
        """
        A chatbot node that retrieves user message from a graph state and returns the LLM generated message into the state
        """

        return {"messages": self.llm.invoke(state["messages"])}

