import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


st.set_page_config(page_title="LangChain + Ollama Chatbot")
st.title("Chatbot")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)


model = ChatOllama(model="llama2")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and friendly AI assistant."),
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
    for msg in st.session_state.memory.chat_memory.messages:
        if msg.type == "human":
            st.markdown(f"**You:** {msg.content}")
        elif msg.type == "ai":
            st.markdown(f"**Siraj:** {msg.content}")
