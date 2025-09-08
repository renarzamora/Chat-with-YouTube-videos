# 🎥 Chat with YouTube Videos

Interact with YouTube videos using natural language! This Streamlit-powered app lets you ask questions about any YouTube video and receive intelligent responses based on its transcript.

---

## 🚀 Features

- 🔍 Extracts video title, description, and transcript using `pytubefix` and `youtube_transcript_api`
- 🤖 Uses an AI agent to answer questions about the video content
- 🛠️ Automatically selects tools based on the type of question (e.g., timestamps vs. general content)
- 💬 Streamlit chat interface with support for tool call visualization
- 🧠 Agent state persistence across interactions

---

## 🧰 Requirements

- Python 3.12
- OpenAI API key (stored in `.env`)
- Dependencies listed in `requirements.txt` (see below)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/renarzamora/Chat-with-YouTube-videos
cd chat-with-youtube

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key to a .env file
echo "OPENAI_API_KEY=your_openai_key_here" > .env

---

🖥️ Usage
streamlit run app.py

Enter a YouTube video URL.

Ask a question about the video.

View responses and tool usage in the chat interface.

--- 

## 🧠 Agent Behavior
The assistant agent is configured with two tools:
```
| Tool Name	                      | Purpose                                                     |
|---------------------------------|-------------------------------------------------------------|
|GetvideoTranscript	              | Retrieves title, description, and full transcript           |
|---------------------------------|-------------------------------------------------------------|
|GetVideoTranscriptWithTimeStamps | Retrieves transcript with timestamps for event-based queries|
|---------------------------------|-------------------------------------------------------------|

The agent decides which tool to use based on the nature of the question.

---

📁 Project Structure
```
├── app.py               # Streamlit frontend
├── agent.py             # Agent configuration and tool logic
├── .env                 # API key storage
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

---

## 🧪 Technologies Used
```
| Technology               | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Python 3.12**          | Core programming language                                               |
| **Streamlit**            | Interactive web interface                                               |
| **pytubefix**            | YouTube video metadata extraction                                      |
| **youtube_transcript_api** | Transcript retrieval from YouTube videos                              |
| **Autogen AgentChat**    | Agent framework for streaming responses and tool integration           |
| **OpenAI API**           | Language model backend for intelligent responses                       |
| **dotenv**               | Secure environment variable management                                 |
| **asyncio**              | Asynchronous execution for responsive agent interactions               |

---

🧪 Demo

---

📜 License
This project is open-source and available under the MIT License.

---

🤝 Contributing
Pull requests are welcome! If you’d like to add features, improve documentation, or localize the interface, feel free to fork and submit a PR.

--

I would like(❤️) you enjoy it and find useful!
Watch my profile here: https://www.linkedin.com/in/renar-arnoldo-zamora-54bb9024/
