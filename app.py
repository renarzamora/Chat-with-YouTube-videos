import streamlit as st
import asyncio
from agent import ConfigAgent,AskAgent
from autogen_agentchat.messages import ToolCallRequestEvent, ToolCallExecutionEvent

st.title('Chat with YouTube videos')
url = st.text_input('Enter the url of the Youtube video:')
chat_container = st.container()
prompt = st.text_input('Ask a question about the video:')

def ShowMessage(chat_container, message):
    with chat_container:
        if isinstance(message, str):
            if message.startswith('User'):
                with st.chat_message('User'):
                    st.markdown(message)
            else:
                with st.chat_message('assistant'):
                    st.markdown(message)        
        elif isinstance(message, ToolCallRequestEvent):
            with st.expander('Tool call request:'):
                st.markdown(message.to_text())
        elif isinstance(message, ToolCallExecutionEvent):
            with st.expander('Tool call execution'):
                st.markdown(message.to_text())    

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    ShowMessage(chat_container, message)

if prompt and url:
    st.session_state.messages.append(f'User: {prompt}')
    ShowMessage(chat_container, f'User: {prompt}')

    async def main(url, prompt):
        agent = ConfigAgent()
        if 'agent_state' in st.session_state:
            await agent.load_state(st.session_state.agent_state)

        async for message in AskAgent(agent, url, prompt):
            st.session_state.messages.append(message)
            ShowMessage(chat_container, message)
            agent_state = await agent.save_state()
        return agent_state
    
    with st.spinner('Generating response...'):
        agent_state = asyncio.run(main(url, prompt))
        st.session_state.agent_state = agent_state    