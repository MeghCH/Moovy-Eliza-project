# **Moovy Eliza Project**
# Moovy Eliza - Backend Engine

**Moovy Eliza** is an AI-powered movie recommendation agent. It leverages the `strands-agents` framework and **Ollama** for local (or remote) LLM inference, providing a conversational experience through **Discord**.

##  Tech Stack

* **Language:** Python 3
* **Agent Framework:** `strands-agents` (Builder, Tools, and Ollama integration)
* **LLM Engine:** Ollama with differents LLM Open Source Models
* **Communication:** `discord.py`
* **Data Management:** Local JSON caching and custom Python logic

---

##  Project Structure

```text
├── app
│   ├── agent.py            # Agent definition and personality
│   ├── chatbot.py          # Discord bot entry point and event handling
│   └── subfunctions        # Core business logic (Tools)
│       ├── get_preffered.py    # Extracts user movie tastes
│       ├── lookalike.py        # Recommendation & similarity logic
│       ├── moviedb_reader.py   # Database interfacing
│       ├── profile_prompter.py # Dynamic LLM prompt construction
│       └── ...                 # JSON & Text utilities
├── cache                   # Persistent storage
│   ├── json                # User session data
│   └── prompt              # Markdown-based agent personas
└── requirements.txt        # Python dependencies
```

---

##  Getting Started

### 1. Prerequisites
Ensure you have Python 3.12 installed. It is highly recommended to use a virtual environment.

### 2. Installation
```bash
# Clone the repository and navigate to the app folder
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.\.venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory (refer to `app/example.env`):
```env
DISCORD_TOKEN = "YOUR-DISCORD-DEVELOPPER-PORTAL-TOKEN"
OLLAMA_URL = "http://localhost:11434"
MOVIEDB_API = "htpps://example.com"
```

### 4. Running the Bot
```bash
python3 app/chatbot.py
```

---

## Core Logic (Subfunctions)

The `subfunctions` directory acts as the "brain" of the agent, providing specialized tools to process data before it reaches the LLM.

| Module | Technical Description |
| :--- | :--- |
| **`moviedb_reader.py`** | Handles queries to the movie database/registry. |
| **`lookalike.py`** | Implements logic to find movies similar to user references. |
| **`get_preffered.py`** | Parses user input to identify preferred genres. |
| **`profile_prompter.py`** | Merges user history and movie data into a structured prompt for Eliza. |
| **`json_manager`** | (`reader`/`deleter`) Handles CRUD operations on the `/cache/json` folder. |

---

## Agent Workflow

1.  **Input:** A user sends a message on Discord.
2.  **Context:** `chatbot.py` identifies the user intent with an NLP and, if needed, execute some sub agents for a specific task (recommendation, ....)
3.  **Inference:** The processed context is sent to the **Ollama** endpoint.
4.  **Output:** Moovy generates a natural language recommendation and sends it back to Discord.

---

## Key Features

* **Stateful Memory:** Uses local JSON files to remember user preferences across different Discord sessions.
* **Modular Toolset:** Logic is decoupled from the agent framework, making it easy to swap the movie source or the similarity algorithm.
