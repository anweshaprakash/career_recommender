import os
import streamlit as st
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Career Path Advisor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #2b313e;
    }
    .chat-message.assistant {
        background-color: #475063;
    }
    .chat-message .avatar {
        width: 20%;
    }
    .chat-message .message {
        width: 80%;
        padding: 0 1.5rem;
    }
    .stTextInput>div>div>input {
        background-color: #2b313e;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize LangChain Groq
llm = ChatGroq(
    model='meta-llama/llama-4-scout-17b-16e-instruct',
    temperature=0.1,
    api_key=os.getenv('GROQ_API_KEY'),
    streaming=True
)

# Career path categories and their descriptions
CAREER_PATHS = {
    "STEM": {
        "description": "Science, Technology, Engineering, and Mathematics",
        "subcategories": ["Computer Science", "Engineering", "Mathematics", "Physics", "Chemistry", "Biology"],
        "icon": "🔬"
    },
    "Arts": {
        "description": "Creative and Visual Arts",
        "subcategories": ["Fine Arts", "Design", "Music", "Theater", "Film", "Digital Arts"],
        "icon": "🎨"
    },
    "Business": {
        "description": "Business and Management",
        "subcategories": ["Finance", "Marketing", "Management", "Entrepreneurship", "Economics"],
        "icon": "💼"
    },
    "Healthcare": {
        "description": "Medical and Healthcare",
        "subcategories": ["Medicine", "Nursing", "Pharmacy", "Public Health", "Mental Health"],
        "icon": "🏥"
    },
    "Humanities": {
        "description": "Humanities and Social Sciences",
        "subcategories": ["Psychology", "Sociology", "History", "Philosophy", "Political Science"],
        "icon": "📚"
    }
}

def get_career_advisor_response(messages):
    """Generate response from career advisor based on conversation history."""
    
    system_prompt = """
    You are a friendly and knowledgeable career guidance expert. Your role is to:
    1. Understand the user's interests, skills, and preferences through natural conversation
    2. Ask relevant clarifying questions when needed
    3. Provide personalized career recommendations
    4. Explain why certain career paths might be suitable
    5. Consider the user's background, interests, and values
    
    Guidelines for your responses:
    - Keep responses concise but informative
    - Maintain a conversational and encouraging tone
    - Ask specific questions when you need more information
    - Provide direct, clear answers without showing your thinking process
    - Never use phrases like "Let me think", "I'm considering", or show internal reasoning
    - Never use markdown formatting or special characters
    - Never show your thinking process or use <think> tags
    - Focus on providing actionable career advice and recommendations
    """
    
    # Format conversation history
    conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "Conversation History:\n{history}\n\nProvide your response as a career advisor.")
    ])
    
    chain = prompt | llm
    return chain.stream({"history": conversation_history})

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I'm your career advisor. I'd love to help you explore potential career paths. Could you tell me about your interests, skills, and what you enjoy doing?"
            }
        ]

def display_career_categories():
    """Display career categories in the sidebar."""
    st.sidebar.title("Career Categories")
    for category, info in CAREER_PATHS.items():
        with st.sidebar.expander(f"{info['icon']} {category}"):
            st.write(info['description'])
            st.write("**Subcategories:**")
            for subcategory in info['subcategories']:
                st.write(f"- {subcategory}")

def main():
    # Sidebar
    with st.sidebar:
        st.title("Career Path Advisor")
        st.markdown("---")
        display_career_categories()
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        This AI-powered career advisor helps you explore potential career paths based on your interests, skills, and preferences.
        
        Simply chat with the advisor to get personalized career recommendations!
        """)
    
    # Main chat interface
    st.markdown("## 💬 Chat with Career Advisor")
    
    # Initialize session state
    initialize_session_state()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Get and display assistant response with streaming
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Stream the response
            for chunk in get_career_advisor_response(st.session_state.messages):
                if chunk.content:
                    full_response += chunk.content
                    message_placeholder.write(full_response)
            
            # Add the complete response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
