# task1:Simple Multi-Persona ChatBot and task2:image classifier
task2 google colab link:https://colab.research.google.com/drive/1pQeAtBHDyJ2bexpvVV-qSdrXubpWfAQi?usp=sharing
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
# CIFAR-10 Image Classification

## 📌 Overview
This project implements CIFAR-10 image classification using PyTorch.  
We compare two approaches:
- **SimpleCNN** (from scratch)
- **Pre-trained ResNet18** (transfer learning)

We also evaluate the impact of **data augmentation**.

---

## ⚙️ Model Architectures

### 🔹 SimpleCNN
- 3 convolutional blocks (Conv → BatchNorm → ReLU → MaxPool)
- Fully connected layers with Dropout
- Output layer with 10 classes

### 🔹 ResNet18 (Transfer Learning)
- Pretrained on ImageNet
- Backbone frozen
- Final fully connected layer replaced with 10-class output

---

## 📊 Results

| Model                          | Dataset        | Final Accuracy |
|--------------------------------|---------------|----------------|
| CNN from Scratch (No Aug)      | CIFAR-10 Basic | **80.9%** |
| CNN from Scratch (With Aug)    | CIFAR-10 Aug   | ~ (placeholder) |
| Pretrained ResNet18 (No Aug)   | CIFAR-10 Basic | ~ (placeholder) |
| Pretrained ResNet18 (With Aug) | CIFAR-10 Aug   | ~ (placeholder) |

---

## 🔎 Confusion Matrix
Below is the confusion matrix for **SimpleCNN (No Augmentation)** after training:

![Confusion Matrix](confusion_matrix.png)  
*(Insert your screenshot here)*

---

