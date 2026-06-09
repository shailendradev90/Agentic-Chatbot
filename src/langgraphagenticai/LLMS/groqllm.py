import os 
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def _init_(self,user_controls_input):
        self.user_constrols_input = user_controls_input

    def get_llm_model(self):
         try : 
            groq_api_key = self.user_constrols_input["GROQ_API_KEY"]
            if  groq_api_key == "" and os.environ["GROQ_API_KEY"] == "":
                st.error("Groq API Key is required to use Groq models.")
                return None

            os.environ["GROQ_API_KEY"] = groq_api_key
            selected_groq_model = self.user_constrols_input.get("selected_groq_model")
            if not selected_groq_model:
                st.error("Please select a Groq model.")
                return None
            llm = ChatGroq(key=groq_api_key, model=selected_groq_model)

         except Exception as e:
            st.error(f"Error initializing Groq LLM: {e}")
            return llm





