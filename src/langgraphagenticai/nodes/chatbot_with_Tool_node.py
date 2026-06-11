from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot Node with Web Search capabilities
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbot response with web search capabilities.
        """

        user_input = state["messages"][-1] if state["messages"] else "" 
    
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

         #simulate tool-specific logic
        tool_response = f"Simulated web search results for query: '{user_input}'"
        return {"messages": [llm_response,tool_response]}
        
    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node
   
    