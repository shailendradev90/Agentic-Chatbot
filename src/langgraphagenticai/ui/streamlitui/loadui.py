import streamlit as st
import os 
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False


        with st.sidebar:
            # LLM selection
            llm_options = self.config.get_llm_options()
            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM", llm_options
            )

            if self.user_controls["selected_llm"] == "Groq":
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Groq Model", groq_model_options
                )
                self.user_controls["GROQ_API_KEY"] =  st.session_state["GROQ_API_KEY"] = self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "Enter Groq API Key", type="password"
                )
               
               # validate API key
                if self.user_controls["GROQ_API_KEY"]:
                    st.success("Groq API Key entered successfully!")
                else:
                    st.warning("Please enter your Groq API Key to use Groq models.")

            # Usecase selection
            usecase_options = self.config.get_usecase_options()
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecase", usecase_options
            )

            if  self.user_controls["selected_usecase"] == "Chatbot With Web" or  self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.text_input(
                    "Enter Tavily API Key for Web Search", type="password"
                 )
                # validate API key
                if self.user_controls["TAVILY_API_KEY"]:
                    st.success("Tavily API Key entered successfully!")
                else:
                    st.warning("Please enter your Tavily API Key to use the Chatbot With Web usecase.")    


            if  self.user_controls["selected_usecase"] == "AI News" :
                st.subheader("AI News Explorer")

                with st.sidebar:
                  time_frame = st.selectbox(
                      "Select Time Frame",["Daily","Weekly","Montly"],index = 0
                    )
                if st.button("Fetch Latest AI News ", use_container_width = True):
                   st.session_state.IsFetchButtonClicked = True
                   st.session_state.timeframe = time_frame


            return self.user_controls