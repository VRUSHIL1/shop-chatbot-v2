# Gemini Chatbot 🤖

A powerful, extensible AI chatbot built with FastAPI and Google Gemini, featuring document-based question answering, vector search, persistent memory, and multi-platform messaging support.

This project is designed for developers who want a production-ready AI assistant with advanced context management and tool integration.

## ✨ Features

- **AI-Powered Conversations** using Google Gemini
- **Document Q&A** with PDF upload and vector search
- **Persistent Chat Sessions** with message history
- **Vector Database Integration** using ChromaDB
- **Multi-Platform Support**
  - Web UI
  - Telegram Bot
  - WhatsApp Integration
- **User Memory** powered by Mem0
- **Email Sending** via SMTP
- **Model Context Protocol (MCP)** for advanced tool orchestration

## 🧰 Tech Stack

**Backend**
- FastAPI
- Python 3.12+
- SQLAlchemy
- Pydantic
- Uvicorn

**AI / ML**
- Google Gemini
- OpenAI (optional)
- LangChain

**Databases**
- MySQL (relational data)
- ChromaDB (vector storage)

**Frontend**
- HTML, CSS, JavaScript

**Messaging**
- Telegram Bot API
- WhatsApp API

**Memory**
- Mem0 AI Memory

## 📋 Prerequisites

**Required**
- Python 3.12+
- MySQL database
- Google Gemini API key

**Optional**
- OpenAI API key
- Telegram Bot credentials
- Mem0 API key
- WhatsApp API credentials

## ⚡ Quick Start

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd gemini-chatbot
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv myenv
```

**Activate it:**

**Windows**
```bash
myenv\Scripts\activate
```

**macOS / Linux**
```bash
source myenv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Configuration

Create a `.env` file in the project root.

⚠️ **Never commit your .env file**  
Make sure `.env` is included in `.gitignore`.

```env
# AI API Keys
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key  # optional

# Database Configuration
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=mytest
DB_PORT=3306

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# Memory Service
MEM0_KEY=your_mem0_api_key

# Telegram (Optional)
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
```

### 5️⃣ Database Setup
```sql
CREATE DATABASE mytest;
```

### 6️⃣ Run the Application
```bash
cd src
python main.py
```

**The server will start at:**
```
http://localhost:8888
```

## 📖 Usage

### 🌐 Web Interface

1. Open `http://localhost:8888`
2. Start a new chat session
3. Upload PDF documents
4. Ask questions based on uploaded documents

### 🔌 API Endpoints

**Chat**
- `POST /ask/{session_id}` — Send a message
- `GET /messages/{session_id}` — Retrieve chat history

**Sessions**
- `GET /sessions/` — List sessions
- `POST /sessions/add/` — Create new session

**Documents**
- `POST /documents/upload-pdf/` — Upload PDF
- `GET /documents/show` — List documents
- `DELETE /documents/delete/{id}` — Delete document

**Telegram**
- `POST /telegram/webhook` — Telegram webhook

### 📄 Document Processing Workflow

1. Upload PDF via web interface
2. Text is extracted and embedded
3. Stored in ChromaDB
4. Ask natural language questions
5. Relevant context is retrieved automatically

## 🔧 Configuration

### AI & System Settings

**Edit:**
```
src/config/settings.py
```

**You can customize:**
- Model parameters (temperature, max tokens)
- Vector search behavior
- Memory configuration
- Retry logic

### Database Models
Database models are defined in `src/model/tableModel.py`

## 📁 Project Structure

```
gemini-chatbot/
├── src/
│   ├── config/          # Configuration
│   ├── controllers/     # Request handlers
│   ├── model/           # Database models
│   ├── page/            # Frontend files
│   ├── routes/          # API routes
│   ├── services/        # Business logic
│   ├── tools/           # Tool handlers
│   ├── utils/           # Utilities
│   ├── validations/     # Schemas
│   └── main.py          # App entry point
├── chroma_vectors/      # Vector database
├── requirements.txt
├── pyproject.toml
├── .env                 # Environment variables
└── README.md
```

## 🧠 Model Context Protocol (MCP)

This project implements MCP for dynamic tool discovery and execution.

### Built-in Tools

- **Email Tool** (SMTP)
- **Weather Tool**
- **PDF Q&A Tool**

### External MCP Servers

- **Database MCP**
- **YouTube MCP**
- **WhatsApp MCP**
- **Telegram MCP**

### MCP Server Configuration

```json
{
  "mcpServers": {
    "example-server": {
      "command": "python",
      "args": ["path/to/server.py"],
      "is_active": true
    }
  }
}
```

### Running MCP

```bash
python mcp_server.py
python mcp_client.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit changes
4. Push to your fork
5. Open a Pull Request

## 📝 License

Licensed under the MIT License.

## 🆘 Support & Troubleshooting

If you face issues:

- Check application logs
- Verify `.env` values
- Ensure MySQL is running
- Confirm API keys are valid
- Check dependency versions

## 🔮 Roadmap

- [ ] User authentication
- [ ] Support more file formats
- [ ] Chat export (PDF / TXT)
- [ ] Mobile-friendly UI
- [ ] Voice input & output