# Local LLM Assistant

A privacy-focused local AI assistant built with **Python, Streamlit, Ollama, and Llama 3.2**. The application provides a web-based chat interface with real-time response streaming and session-based conversation history.

## Features

- Interactive conversational interface
- Local inference using Llama 3.2
- Real-time streaming responses
- Session-based conversation history
- Local execution through Ollama
- No external AI API required

## Tech Stack

- **Python** — Application logic
- **Streamlit** — Web interface
- **Ollama** — Local LLM runtime
- **Llama 3.2** — Language model

## Project Structure

```text
Local_LLM/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

Make sure the following are installed:

- Python 3.10 or higher
- Ollama
- Llama 3.2

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

## Installation

Clone the repository:

```bash
git clone https://github.com/harinaath7777/Local-LLM-Assistant.git
cd Local-LLM-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## How It Works

```text
User
  ↓
Streamlit Chat Interface
  ↓
Python Application
  ↓
Ollama
  ↓
Llama 3.2
  ↓
Streaming Response
  ↓
Streamlit UI
```

The user enters a prompt through the Streamlit interface. The application sends the prompt to the locally running Ollama service, which uses Llama 3.2 to generate the response. The generated response is streamed back to the interface in real time.

## Privacy

The Llama 3.2 model runs locally through **Ollama**. The application does not require an external AI API key to generate responses.

## Future Improvements

- Persistent conversation history
- PDF and document upload
- Retrieval-Augmented Generation (RAG)
- Multiple model selection
- Improved error handling
- Docker support
- Chat export

## Learning Project

This project was developed to explore the fundamentals of building applications around locally hosted Large Language Models (LLMs).

The initial implementation follows a tutorial-based approach and will be progressively extended with additional AI engineering features.

## License

This project is licensed under the MIT License.
