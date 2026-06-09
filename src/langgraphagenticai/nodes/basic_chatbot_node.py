from src.langgraphagenticai.state.state import State


class BasicChatbotNode(State):
    """
    BasicChatbotNode is a node in the StateGraph that represents a basic chatbot interaction.
    It is designed to handle simple conversational interactions with users, such as greeting, asking for input, and providing responses.
    """
    def __init__(self, model):
        super().__init__()
        self.model = model

    def process(self, state: State)-> dict:
        """
        Execute the chatbot node logic.
        This method processes the input data, generates a response using the language model, and returns the response.

        Args:
            input_data (str): The input data from the user."""
        
        # Generate a response using the language model
        response=self.llm.invoke(state['messages'])

        return {"messages":response }
        
