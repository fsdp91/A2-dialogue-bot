import streamlit as st
import google.generativeai as genai

# Setup
st.set_page_config(page_title="Shopping Bot A2", page_icon="🛍️")
st.title("🛍️ English Practice: Shopping Bot")

# Use your API Key
genai.configure(api_key="AIzaSyDUMIoTZSp8nYp1RAqmA8f7FsR8LCLL8vM")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initializing Chat
if "messages" not in st.session_state:
    st.session_state.messages = []
    # This is your original app's personality:
    st.session_state.system_prompt = "Act as a shop assistant for A2 students. Use Present Perfect and -ed/-ing adjectives."

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Write your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Gemini
    response = model.generate_content(f"{st.session_state.system_prompt} \n User: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
