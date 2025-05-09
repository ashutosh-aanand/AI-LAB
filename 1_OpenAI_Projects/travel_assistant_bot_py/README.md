Sure! Here's the updated `README.md` without the `.gitignore` section:

---

# 🧠 AI Chatbot Experiments

This project is a personal learning sandbox where I experiment with **OpenAI's language models** to build and improve a chatbot. The goal is to deepen my understanding of AI concepts through hands-on development.

## 🗂 Project Structure

```
.
├── bot_v1.py     # Basic chatbot with single-turn conversation
├── bot_v2.py     # Chatbot with simple context memory (multi-turn)
├── ...
├── .env          # Stores API key (excluded from version control)
├── README.md     # Project documentation
```

### 🔹 `bot_v1.py`

* First version of the chatbot.
* Sends a single user prompt to the OpenAI API and displays the response.
* No memory or context tracking between turns.

### 🔹 `bot_v2.py`

* Adds basic memory of past conversation.
* Maintains a list of previous messages to send as context with each prompt.
* Demonstrates how to build more coherent multi-turn interactions.



## 🚀 Getting Started

### Prerequisites

* Python 3.11.0
* OpenAI Python SDK
* [`python-dotenv`](https://pypi.org/project/python-dotenv/) for environment variable management

### Installation

1. Clone the repo:

```bash
git clone https://github.com/your-username/ai-chatbot-experiments.git
cd ai-chatbot-experiments
```

2. Install dependencies:

```bash
pip install openai python-dotenv
```

3. Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-api-key-here
```

4. The scripts will automatically load your API key using `dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

## 📚 Goals

* Learn how OpenAI's chat models work
* Explore prompt engineering techniques
* Build increasingly smarter bots through incremental versions

## 🧪 Future Plans

* Add user interface (CLI/GUI or web)
* Incorporate external tools for enhanced responses (e.g. calculator, search)
* Try out different OpenAI models (e.g. `gpt-3.5-turbo`, `gpt-4`)
* Add persistent memory (e.g. using a file or vector database)

## 🤖 Disclaimer

This is an experimental and educational project. Use responsibly and always be mindful of API usage and costs.
