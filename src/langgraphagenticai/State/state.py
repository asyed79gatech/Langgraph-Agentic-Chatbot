from pydantic import BaseModel, Field
from typing_extensions import TypedDict, List, Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    """ 
    Represents the structure of the state used in the graph
    """
    # Create a messages object in the state that is a list of messages that can be appended
    messages: Annotated[List, add_messages]