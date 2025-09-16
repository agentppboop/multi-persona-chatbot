# Multi-Persona Chatbot Application
# This Streamlit application creates a conversational chatbot with multiple personas
# using LangChain for memory management and Groq API for language model inference

import streamlit as st
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferWindowMemory
from langchain.schema import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain

# Load environment variables from .env file
load_dotenv()

# Check if API key is loaded
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("⚠️ GROQ_API_KEY not found! Please add it to your .env file.")
    st.stop()

# Configure Streamlit page
st.set_page_config(
    page_title="Multi-Persona Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define persona templates
PERSONAS = {
    "Standard": {
        "name": "Standard Assistant",
        "description": "A helpful, friendly, and informative assistant",
        "template": """You are a helpful, friendly, and informative AI assistant. You provide clear, accurate, and useful responses to help users with their questions and tasks. Be conversational and engaging while maintaining professionalism.

Current conversation:
{history}
Human: {input}
Assistant:"""
    },
    "RoastBot": {
        "name": "RoastBot 🔥",
        "description": "Always responds with witty or sarcastic roasts",
        "template": """You are RoastBot, a witty and sarcastic AI that responds to everything with clever roasts and burns. You're playfully mean but never truly hurtful. Use humor, sarcasm, and wit in every response. Keep it fun and entertaining!

Current conversation:
{history}
Human: {input}
RoastBot:"""
    },
    "ShakespeareBot": {
        "name": "ShakespeareBot 🎭",
        "description": "Responds in old-English, Shakespeare-style prose",
        "template": """Thou art ShakespeareBot, a most learned and eloquent assistant who doth speak in the manner of the great Bard himself. Respond to all queries in flowery Elizabethan English, with thee, thou, doth, hath, and other period-appropriate language. Be verbose and poetic in thy responses, as befits a true scholar of the Renaissance.

Current conversation:
{history}
Human: {input}
ShakespeareBot:"""
    },
    "Emoji Translator Bot": {
        "name": "Emoji Translator Bot 😎",
        "description": "Converts everything into emoji-speak",
        "template": """You are the Emoji Translator Bot! You communicate primarily through emojis and convert everything into emoji-speak. Use lots of emojis, emoticons, and symbols to express ideas. When you must use words, keep them short and fun. Make everything visual and expressive! 🎨✨

Current conversation:
{history}
Human: {input}
Emoji Bot:"""
    }
}

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferWindowMemory(
            k=10,  # Keep last 10 exchanges
            return_messages=True,
            memory_key="history"
        )
    
    if "selected_persona" not in st.session_state:
        st.session_state.selected_persona = "Standard"
    
    if "chat_model" not in st.session_state:
        st.session_state.chat_model = None
    
    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = None

def create_conversation_chain(persona_key):
    """Create a conversation chain with the selected persona"""
    try:
        # Initialize the Groq chat model
        chat_model = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.1-8b-instant",  # Currently supported production model
            temperature=0.7,
            max_tokens=1000
        )
        
        # Create prompt template for the selected persona
        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=PERSONAS[persona_key]["template"]
        )
        
        # Create conversation chain with memory
        conversation_chain = ConversationChain(
            llm=chat_model,
            prompt=prompt,
            memory=st.session_state.memory,
            verbose=False
        )
        
        return conversation_chain
    
    except Exception as e:
        st.error(f"Error creating conversation chain: {str(e)}")
        return None

def clear_chat_history():
    """Clear chat history and reset memory"""
    st.session_state.messages = []
    st.session_state.memory.clear()

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # App title and description
    st.title("🤖 Multi-Persona Chatbot")
    st.markdown("Chat with different AI personas! Select a persona from the sidebar and start chatting.")
    
    # Sidebar for persona selection and controls
    with st.sidebar:
        st.header("🎭 Persona Selection")
        
        # Persona selection dropdown
        selected_persona = st.selectbox(
            "Choose your chatbot persona:",
            options=list(PERSONAS.keys()),
            index=list(PERSONAS.keys()).index(st.session_state.selected_persona),
            key="persona_selector"
        )
        
        # Check if persona changed
        if selected_persona != st.session_state.selected_persona:
            st.session_state.selected_persona = selected_persona
            st.session_state.conversation_chain = None  # Reset chain
            st.rerun()
        
        # Display current persona info
        current_persona = PERSONAS[selected_persona]
        st.markdown(f"**Current Persona:** {current_persona['name']}")
        st.markdown(f"*{current_persona['description']}*")
        
        st.divider()
        
        # Chat controls
        st.header("🔧 Chat Controls")
        
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            clear_chat_history()
            st.rerun()
        
        # Display chat statistics
        st.markdown("---")
        st.markdown("📊 **Chat Stats:**")
        st.markdown(f"- Messages: {len(st.session_state.messages)}")
        st.markdown(f"- Memory buffer: {st.session_state.memory.k} exchanges")
    
    # Create or update conversation chain if needed
    if (st.session_state.conversation_chain is None or 
        st.session_state.selected_persona != selected_persona):
        
        with st.spinner("Initializing chatbot..."):
            st.session_state.conversation_chain = create_conversation_chain(selected_persona)
        
        if st.session_state.conversation_chain is None:
            st.error("Failed to initialize chatbot. Please check your API key and try again.")
            st.stop()
    
    # Main chat interface
    st.header(f"💬 Chat with {PERSONAS[selected_persona]['name']}")
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Get response from conversation chain
                    response = st.session_state.conversation_chain.predict(input=prompt)
                    
                    # Display response
                    st.markdown(response)
                    
                    # Add bot response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                
                except Exception as e:
                    error_message = f"Sorry, I encountered an error: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

# Run the application
if __name__ == "__main__":
    main()