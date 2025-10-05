LangChain + Ollama Chatbot

A bright and friendly AI Chatbot built with LangChain and Ollama, deployed using Streamlit.
The chatbot keeps conversation memory and displays the latest messages on top for a modern chat experience.

Features
AI-powered chatbot using Ollama LLaMA 2 model
Maintains conversation memory using LangChain
Bright and clean Streamlit interface
Latest messages displayed at the top like a chat stack
Easy to deploy on Streamlit Cloud

Installation

Clone the repository:
git clone https://github.com/Aflahfarhank/ChatbotQnA.git
cd ChatbotQnA

Create a virtual environment
python -m venv .venv

Activate the virtual environment:
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the app locally:
streamlit run app.py

Type your question in the input box and click Send
The chatbot will reply using the Ollama model
All previous messages are displayed below, with the latest on top

