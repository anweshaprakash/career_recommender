# 🎯 Career Path Advisor

Welcome to the **Career Path Advisor**, an AI-powered Streamlit app designed to help users explore personalized career options based on their interests, skills, and preferences.

🔗 **Live App**: [https://careerrecommender.streamlit.app/](https://careerrecommender.streamlit.app/)  
🐙 **GitHub**: [github.com/anweshaprakash/career_recommender](https://github.com/anweshaprakash/career_recommender)  
📽️ **Demo Video (Loom)**: [https://www.loom.com/share/220f1cce01eb45e2b180b8901d365703?sid=853696fb-f1d6-4aa1-ad2f-f29487b3b80d]

---

## 🚀 Features

- 💬 **Conversational AI Chatbot**: Provides career guidance through a friendly chat interface.
- 🧠 **Powered by Meta-LLaMA via Groq**: Utilizes `meta-llama/llama-4-scout-17b-16e-instruct` for fast, intelligent responses.
- 🎨 **Responsive UI**: Clean, centered layout with categorized career options in an expandable sidebar.
- 📂 **Career Categories**: STEM, Arts, Business, Healthcare, Humanities with detailed subfields.
- ✅ **Session State Management**: Maintains chat history across interactions.
- 🛠️ **Built with**: Streamlit, LangChain, Groq API, dotenv for environment config.

---

## 🧠 How It Works

The assistant:
1. Learns about the user's interests, strengths, and goals.
2. Asks targeted questions when more clarity is needed.
3. Recommends career paths and explains why they are suitable.
4. Delivers concise and actionable suggestions with a warm and supportive tone.

---

## 🧰 Tech Stack

- **Frontend/UI**: Streamlit
- **LLM Backend**: `langchain_groq.ChatGroq`
- **Prompting**: `ChatPromptTemplate` with custom career advisory instructions
- **API Key Handling**: `.env` file managed with `python-dotenv`

---

## 📦 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/anweshaprakash/career_recommender.git
    cd career_recommender
    ```

2. **Create a `.env` file**:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```bash
    streamlit run app.py
    ```

---

## 💡 Tips

- Use the sidebar to explore different career domains.
- Provide detailed answers about your interests for better recommendations.
- The AI will guide the conversation and adapt based on your responses.

---

## 📬 Feedback

Have suggestions or feature requests? Open an issue on the [GitHub repo](https://github.com/anweshaprakash/career_recommender/issues) or create a pull request!

---

Built with ❤️ by [Anwesha Prakash](https://github.com/anweshaprakash)
