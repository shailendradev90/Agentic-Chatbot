from langgraph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph, START, END 
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    """
    GraphBuilder is responsible for building the StateGraph for the LangGraph AgenticAI application.
    It defines the structure of the graph, including the nodes and edges, and how they interact with each other.
    """

    def __init__(self, model):
        self.llm=model
        self.graph_builder=StateGraph(State)


    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph using Langgraph.
        This method initializes a chatbot node using 'BasicChatbotNode' class
        and integrates it into the graph. 
        The Chatbot node is set to both as entry and exit point of the graph.
        The chatbot node is designed to handle basic conversational interactions with users.

        """

        basic_chatbot_node=BasicChatbotNode(self.llm)


        self.graph_builder.add_node("chatbot_node", basic_chatbot_node.process)
        self.graph_builder.add_edge("START", "chatbot_node")
        self.graph_builder.add_edge("chatbot_node", "END")
        