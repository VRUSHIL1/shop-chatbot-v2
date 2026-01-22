# Gemini Chatbot

A powerful AI chatbot application built with FastAPI and Google's Gemini AI, featuring document processing, vector database integration, and multi-platform messaging support.

## 🚀 Features

- **AI-Powered Conversations**: Integrated with Google Gemini AI for intelligent responses
- **Document Processing**: Upload and process PDF documents with vector storage
- **Session Management**: Persistent chat sessions with message history
- **Vector Database**: ChromaDB integration for document similarity search
- **Multi-Platform Support**: 
  - Web interface
  - Telegram bot integration
  - WhatsApp integration
- **Memory Management**: User memory with Mem0 integration
- **Email Services**: SMTP email functionality
- **MCP (Model Context Protocol)**: Advanced context management

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.12+
- **AI/ML**: Google Gemini AI, OpenAI, LangChain
- **Database**: MySQL, ChromaDB (Vector Database)
- **Frontend**: HTML, CSS, JavaScript
- **Messaging**: Telegram Bot API, WhatsApp API
- **Memory**: Mem0 AI Memory
- **Others**: SQLAlchemy, Pydantic, Uvicorn

## 📋 Prerequisites

- Python 3.12 or higher
- MySQL database
- Google Gemini API key
- OpenAI API key (optional)
- Telegram Bot Token (for Telegram integration)
- Mem0 API key

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd "Gemini chatbot"
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory with the following variables:

```env
# AI API Keys
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

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

# Telegram Bot (Optional)
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
```

### 5. Database Setup
```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE mytest;
```

### 6. Run the Application
```bash
# Navigate to src directory
cd src

# Start the server
python main.py
```

The application will be available at: `http://localhost:8888`

## 📖 Usage

### Web Interface
1. Open your browser and go to `http://localhost:8888`
2. Click "Start New Chat" to begin a conversation
3. Upload documents using the "Document" button
4. Chat with the AI assistant

### API Endpoints

#### Chat
- `POST /ask/{session_id}` - Send a message to the chatbot
- `GET /messages/{session_id}` - Get chat history

#### Sessions
- `GET /sessions/` - List all chat sessions
- `POST /sessions/add/` - Create a new session

#### Documents
- `POST /documents/upload-pdf/` - Upload PDF documents
- `GET /documents/show` - List uploaded documents
- `DELETE /documents/delete/{id}` - Delete a document

#### Telegram
- `POST /telegram/webhook` - Telegram webhook endpoint

### Document Processing
1. Click the "Document" button in the web interface
2. Upload PDF files using the upload button
3. Documents are automatically processed and stored in the vector database
4. Ask questions about uploaded documents in chat

## 🔧 Configuration

### AI Model Settings
Edit `src/config/settings.py` to customize:
- Model parameters (temperature, max tokens)
- Vector search settings
- Memory configuration
- Retry attempts and delays

### Database Models
Database models are defined in `src/model/tableModel.py`

## 📁 Project Structure

```
Gemini chatbot/
├── src/
│   ├── config/          # Configuration files
│   ├── controllers/     # Request controllers
│   ├── model/          # Database models
│   ├── page/           # Frontend files
│   ├── routes/         # API routes
│   ├── services/       # Business logic
│   ├── tools/          # Tool management
│   ├── utils/          # Utility functions
│   ├── validations/    # Data validation schemas
│   └── main.py         # Application entry point
├── chroma_vectors/     # Vector database storage
├── myenv/             # Virtual environment
├── requirements.txt   # Python dependencies
├── pyproject.toml     # Project configuration
└── .env              # Environment variablesRemove-Item -Recurse -Force .git
```

## 🐛 Known Issues

- **Vector Database Refresh**: Page refresh doesn't update vector database (mentioned in original README)
- Ensure proper environment variable configuration for all features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check the console logs for error messages
2. Verify all environment variables are set correctly
3. Ensure all required services (MySQL, APIs) are accessible
4. Check the `requirements.txt` for dependency conflicts

## 🔮 Future Enhancements

- [ ] Fix vector database refresh issue
- [ ] Add user authentication
- [ ] Implement file type support beyond PDF
- [ ] Add conversation export functionality
- [ ] Enhance mobile responsiveness
- [ ] Add voice message support