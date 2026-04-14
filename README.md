# **Moovy Eliza Project**
# Moovy Eliza - Backend Engine

**Moovy Eliza** is an AI-powered movie recommendation agent. It leverages the `strands-agents` framework and **Ollama** for local (or remote) LLM inference, providing a conversational experience through **Discord**.

##  Tech Stack

* **Language:** Python 3
* **Agent Framework:** `strands-agents` (Builder, Tools, and Ollama integration)
* **LLM Engine:** Ollama (hosted at `https://ollama.wyligr.fr`)
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
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory (refer to `app/example.env`):
```env
DISCORD_TOKEN="your_discord_bot_token"
OLLAMA_URL="https://ollama.wyligr.fr"
```

### 4. Running the Bot
```bash
python app/chatbot.py
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
| **`uniform_text.py`** | Standardizes string inputs (regex cleaning, casing) for better matching. |

---

## Agent Workflow

1.  **Input:** A user sends a message on Discord.
2.  **Context:** `chatbot.py` identifies the user and retrieves their session from `cache/json/`.
3.  **Processing:** The `agent.py` uses `strands-agents` to decide which `subfunctions` to call.
4.  **Inference:** The processed context is sent to the **Ollama** endpoint.
5.  **Output:** Moovy generates a natural language recommendation and sends it back to Discord.

---

## Key Features

* **Stateful Memory:** Uses local JSON files to remember user preferences across different Discord sessions.
* **Modular Toolset:** Logic is decoupled from the agent framework, making it easy to swap the movie source or the similarity algorithm.
* **Custom Personas:** Agent behavior can be tweaked by editing the markdown files in `cache/prompt/`.

