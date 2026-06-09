from typing_extensions import TypeDict
from langgraph.graph.message import add_messages
from typing import Annotated


class State(TypeDict):
    """
    Represent the structure of state used in Graph
    State is a dictionary that holds the current state of the application, including user controls and messages.
    It is used to manage the state of the application and pass it between different components.
    """
    user_controls: dict
    messages: Annotated[list, add_messages]


