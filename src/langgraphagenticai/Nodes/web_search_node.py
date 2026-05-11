from src.langgraphagenticai.State.state import State

class ChatbotToolNode:

    """
    Creates a node object of an llm with integrated tools.
    Returns the responses of this node to the State Graph
    """

    def __init__(self, model, tools):
        self.llm = model
        self.tools = tools

    def llm_with_tool_node(self, state:State):
        llm_with_tools = self.llm.bind_tools(self.tools)

        return {"messages": llm_with_tools.invoke(state["messages"])}
    

