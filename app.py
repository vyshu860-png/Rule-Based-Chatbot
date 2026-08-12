import streamlit  as st
st.set_page_config(page_title="SAM AI TECHNOLIGIES CHATBOT", page_icon=":smiley:", layout="wide")
st.title("SAM AI TECHNOLOGIES CHATBOT")
st.subheader("Rule-Based Chatbot")
st.write("Created by: kunchala naga vaishnavi")
st.write("Welcome!Ask me anything about AI,ML,Python,NLPand more")
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hello","hey","hii"]:
        return "Hello!Welcome to SAM AI TECHNOLOGIES.How can i help you ?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you! How can I assist you today?"

    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines."
    elif "ml" in user_input:
        return "ML stands for Machine Learning, a subset of AI that focuses on building systems that learn from data."
    elif "python" in user_input:
        return "Python is a popular programming language known for its simplicity and versatility."
    elif "nlp" in user_input:
        return "NLP stands for Natural Language Processing, a field of AI that focuses on the interaction between computers and humans through natural language."
    else:
        return "I'm sorry, I don't have an answer for that. Can you please ask something else?"
if "messages" not in st.session_state:
    st.session_state.messages = [] 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 
user_input = st.chat_input("Type your message here...",key="main_chat")
if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    
    