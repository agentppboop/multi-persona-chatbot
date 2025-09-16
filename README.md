# Simple Multi-Persona ChatBot

A simple yet powerful chatbot application built with Streamlit and LangChain that features multiple AI personas and conversation memory.

## 🚀 Features

- **Multiple AI Personas**: Switch between 4 distinct chatbot personalities
- **Conversation Memory**: Remembers last 10 exchanges in the conversation
- **Real-time Chat Interface**: Clean and intuitive Streamlit UI
- **Persistent Sessions**: Chat history maintained during the session
- **Easy Persona Switching**: Change personalities mid-conversation

## 🎭 Available Personas

1. **Standard**: Helpful and friendly AI assistant
2. **RoastBot**: Witty and sarcastic responses with humor
3. **Shakespeare**: Responds in eloquent Elizabethan English
4. **Emoji**: Communicates primarily through emojis and symbols

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key (free at [console.groq.com](https://console.groq.com/))

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/simple-chatbot.git
   cd simple-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
simple-chatbot/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🔧 Dependencies

- `streamlit`: Web UI framework
- `langchain`: LLM framework with memory management
- `langchain-groq`: Groq API integration
- `python-dotenv`: Environment variable management

## 🎯 Usage

1. **Start the Application**: Run `streamlit run app.py`
2. **Select Persona**: Use the sidebar dropdown to choose your preferred AI personality
3. **Start Chatting**: Type messages in the chat input at the bottom
4. **Switch Personas**: Change personas anytime during the conversation
5. **Clear History**: Use the "Clear Chat" button to reset the conversation

## 🔑 Getting Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key to your `.env` file

## 🤖 Technical Details

- **Model**: Uses Groq's `llama-3.1-8b-instant` for fast responses
- **Memory**: Maintains conversation context using `ConversationBufferWindowMemory`
- **Session Management**: Streamlit session state prevents conversation loss
- **Error Handling**: Graceful error handling with user-friendly messages

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file exists and contains the correct API key
   - Verify the key is active on Groq console

2. **Module Import Errors**
   - Run `pip install -r requirements.txt` to install all dependencies
   - Check Python version compatibility

3. **Model Deprecation**
   - If you encounter model deprecation errors, update the model name in `app.py`
   - Check [Groq's documentation](https://console.groq.com/docs/models) for current models

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Ensure you're using the latest version

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://langchain.com/)
- Uses [Groq](https://groq.com/) for fast LLM inference

---

**Happy Chatting! 🤖💬**