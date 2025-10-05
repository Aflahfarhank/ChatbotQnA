import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


st.set_page_config(
    page_title="LangChain + Ollama Chatbot",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<div class="header">
    <h1>LangChain AI Chatbot</h1>
    <p>Clean bright interface powered by Ollama & Streamlit</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Bright solid background color */
body {
    background-color: #FFFDE7;  /* Light yellow */
}

/* Header styling */
.header {
    background-color: #FFF9C4;  /* Soft pastel header */
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 20px;
}

.header h1 {
    color: #F57F17;  /* Bright orange text */
    margin: 0;
}

.header p {
    color: #F9A825;  /* Slightly darker text */
    margin: 0;
}

</style>
""", unsafe_allow_html=True)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

model = ChatOllama(model="llama2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the friend named Siraj."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory
)

user_input = st.text_input("Ask me anything:")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        response = chain.run(input=user_input)

if st.session_state.memory.chat_memory.messages:
    st.subheader("Chat History")
    for msg in reversed(st.session_state.memory.chat_memory.messages):
        if msg.type == "human":
            st.markdown(f"**You:** {msg.content}")
        elif msg.type == "ai":
            st.markdown(f"**Siraj:** {msg.content}")
