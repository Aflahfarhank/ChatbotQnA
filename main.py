# # app.py
# import streamlit as st
# from langchain.chains import LLMChain
# from langchain.agents import Tool, initialize_agent
# from langchain.llms.base import LLM
# import ollama
# from transformers import pipeline
# import torch
#
# # -------------------------------
# # Check GPU availability
# # -------------------------------
# device = 0 if torch.cuda.is_available() else -1
#
#
# # -------------------------------
# # Transformers Pipelines
# # -------------------------------
# @st.cache_resource
# def load_summarizer():
#     return pipeline("summarization", model="facebook/bart-large-cnn", device=device)
#
#
# @st.cache_resource
# def load_classifier():
#     return pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=device)
#
#
# summarizer = load_summarizer()
# classifier = load_classifier()
#
#
# # -------------------------------
# # Ollama wrapper for LangChain
# # -------------------------------
# class OllamaLLM(LLM):
#     @property
#     def _llm_type(self):
#         return "ollama"
#
#     def _call(self, prompt, stop=None):
#         response = ollama.chat(
#             model="llama2",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response['message']['content']
#
#
# ollama_llm = OllamaLLM()
#
# # -------------------------------
# # Define Tools
# # -------------------------------
# tools = [
#     Tool(
#         name="Summarize Text",
#         func=lambda text: summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text'],
#         description="Summarizes any text into a concise summary."
#     ),
#     Tool(
#         name="Classify Text",
#         func=lambda text: classifier(text, candidate_labels=["politics", "science", "sports"])['labels'][0],
#         description="Classifies text into categories like politics, science, sports."
#     ),
#     Tool(
#         name="Q&A Ollama",
#         func=lambda question: ollama_llm(question),
#         description="Answer any general question using Ollama LLaMA model."
#     )
# ]
#
# # -------------------------------
# # Initialize LangChain Agent
# # -------------------------------
# agent = initialize_agent(tools, ollama_llm, agent="zero-shot-react-description", verbose=False)
#
# # -------------------------------
# # Streamlit UI
# # -------------------------------
# st.set_page_config(page_title="Hybrid AI Chatbot", page_icon="🤖", layout="wide")
# st.title("🤖 Hybrid AI Chatbot with LangChain")
#
# st.markdown(
#     """
#     **Instructions:**
#     - Type your question normally → Ollama answers general questions
#     - `Summarize: <your text>` → Summarizes text
#     - `Classify: <your text>` → Classifies text into categories (politics, science, sports)
#     """
# )
#
# user_input = st.text_area("Enter your query here:")
#
# if st.button("Submit") and user_input:
#     with st.spinner("Processing..."):
#         try:
#             response = agent.run(user_input)
#             st.success("✅ Done!")
#             st.write(response)
#         except Exception as e:
#             st.error(f"Error: {e}")
