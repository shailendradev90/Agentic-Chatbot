import streamlit as st



from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraphagenticai_app():
    """
    Loads the run the LangGraph AgenticAI application with streamlit UI
    This function initializes the Streamlit UI, handle user interactions, and returns the user controls for further processing.

    """
    ui_loader = LoadStreamlitUI()
    user_input = ui_loader.load_streamlit_ui()

    if not user_input:
        st.error("Error: failed to load user input from Streamlit UI.")
        return 
    
    user_message = st.chat_input("Enter your message here...")
    








