# 🤖 Resume Chat Assistant

A powerful Streamlit application that enables intelligent conversations with resume content using RAG (Retrieval-Augmented Generation) approach. The application processes PDF resumes, creates vector embeddings using ChromaDB, and leverages OpenAI's language models to provide accurate, context-aware responses about the resume content.

## 🌟 Features

- 🤖 **AI-Powered Q&A**: Advanced natural language processing for resume queries
- 📄 **PDF Processing**: Automatic text extraction and chunking from PDF documents
- 🔍 **Semantic Search**: ChromaDB vector database for fast similarity search
- 💬 **Interactive Interface**: Clean, user-friendly Streamlit web interface
- 🔒 **Secure Configuration**: Environment-based API key management
- ⚡ **Real-time Processing**: Instant responses with loading indicators
- 📊 **Persistent Storage**: Vector embeddings saved locally for quick access
- 🎨 **Responsive Design**: Modern UI with emojis and visual feedback

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Streamlit | Web application framework |
| **LLM Framework** | LangChain | Orchestrating language model workflows |
| **Vector Database** | ChromaDB | Storing and retrieving embeddings |
| **Language Model** | OpenAI GPT | Natural language understanding and generation |
| **PDF Processing** | PyPDF | Document parsing and text extraction |
| **Environment Management** | python-dotenv | Configuration management |

## 📋 Prerequisites

- **Python**: Version 3.8 or higher
- **OpenAI API Key**: Required for embeddings and language model access
- **PDF Resume**: Your resume file in PDF format
- **Internet Connection**: For OpenAI API calls

## 🚀 Quick Start

### Step 1: Clone the Repository
```bash
git clone https://github.com/yennares/chat_with_resume.git
cd chat_with_resume
```

### Step 2: Set Up Python Environment (Recommended)
```bash
# Create virtual environment
python -m venv resume_chat_env

# Activate virtual environment
# On Windows:
resume_chat_env\Scripts\activate
# On macOS/Linux:
source resume_chat_env/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Copy the example environment file and add your API key:
```bash
# Copy the example file
cp .env.example .env
```

Then edit the `.env` file and add your OpenAI API key:
```env
# Required: Your OpenAI API Key
OPENAI_API_KEY=your_actual_openai_api_key_here

# Optional: Model configuration
OPENAI_MODEL=gpt-3.5-turbo
TEMPERATURE=0

# Optional: Streamlit configuration
STREAMLIT_SERVER_PORT=8501
```

**🔑 Getting an OpenAI API Key:**
1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign up or log in to your account
3. Create a new API key
4. Copy and paste it into your `.env` file

### Step 5: Add Your Resume
Place your resume PDF file in the project root directory and rename it to `resume.pdf`

### Step 6: Run the Application
```bash
streamlit run app.py
```

### Step 7: Access the Application
Open your web browser and navigate to:
```
http://localhost:8501
```

## 📖 Detailed Usage Guide

### First Time Setup
1. **Launch the app** - The application will automatically detect and process your `resume.pdf`
2. **Processing indicator** - You'll see a "🔄 Processing resume..." message
3. **Success confirmation** - Once complete, you'll see "✅ Resume processed successfully!"
4. **Ready to chat** - The text input field will be available for questions

### Asking Questions
The AI assistant is designed to answer questions about the resume content. Here are some example queries:

**📚 Educational Background:**
- "What degrees does the candidate have?"
- "Where did they study?"
- "What was their GPA or academic achievements?"

**💼 Professional Experience:**
- "What companies has the candidate worked for?"
- "What are their key responsibilities in their current role?"
- "How many years of experience do they have?"

**🛠️ Technical Skills:**
- "What programming languages does the candidate know?"
- "What frameworks and tools are they familiar with?"
- "Do they have experience with cloud technologies?"

**🏆 Achievements & Projects:**
- "What are their notable achievements?"
- "Can you describe their key projects?"
- "What certifications do they have?"

**📊 Summary Questions:**
- "Give me a summary of the candidate's profile"
- "What makes this candidate unique?"
- "Are they suitable for a senior developer position?"

### Advanced Features
- **Context Retention**: The app maintains context within the session
- **Precise Answers**: Responses are based solely on resume content
- **Professional Tone**: All responses maintain a professional, positive tone
- **Markdown Formatting**: Answers are formatted for easy readability

## 🗂️ Project Structure

```
RajaChatPDF/
├── 📁 .chromadb/          # Vector database storage (auto-generated)
├── 📄 app.py              # Main Streamlit application
├── 📄 resume.pdf          # Your resume file (not tracked in git)
├── 📄 requirements.txt    # Python dependencies
├── 📄 .env                # Environment variables (not tracked in git)
├── 📄 .env.example        # Example environment file (safe for git)
├── 📄 .gitignore         # Git ignore rules
└── 📄 README.md          # This documentation
```

## ⚙️ Configuration Options

### Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | Required | Your OpenAI API key |
| `OPENAI_MODEL` | `gpt-3.5-turbo` | OpenAI model to use |
| `TEMPERATURE` | `0` | Model creativity (0-1) |
| `STREAMLIT_SERVER_PORT` | `8501` | Port for the web app |

### Customization
You can modify the following in `app.py`:
- **Chunk size**: Adjust document splitting parameters
- **System prompt**: Customize the AI assistant's behavior
- **UI elements**: Modify the Streamlit interface
- **Vector store settings**: Configure ChromaDB parameters

## 🔧 Troubleshooting

### Common Issues

**❌ "OpenAI API key not found" Error:**
- Ensure your `.env` file exists in the project root
- Verify the API key is correctly formatted
- Check that the environment variable name is `OPENAI_API_KEY`

**❌ "Resume file not found" Error:**
- Confirm `resume.pdf` exists in the project root directory
- Check the file name is exactly `resume.pdf` (case-sensitive)
- Ensure the file is a valid PDF format

**❌ ChromaDB Issues:**
- Delete the `.chromadb` folder and restart the app
- Ensure you have write permissions in the project directory

**❌ Package Installation Errors:**
- Update pip: `pip install --upgrade pip`
- Try installing packages individually
- Use Python 3.8+ (some packages require newer Python versions)

**❌ Streamlit Port Issues:**
- Change the port in `.env`: `STREAMLIT_SERVER_PORT=8502`
- Or specify manually: `streamlit run app.py --server.port 8502`

### Performance Optimization
- **Large PDFs**: For resumes longer than 10 pages, consider reducing chunk size
- **API Costs**: Use `gpt-3.5-turbo` instead of `gpt-4` for cost efficiency
- **Processing Speed**: Vector embeddings are cached locally for faster subsequent runs

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Set up the development environment following the installation steps
4. Make your changes
5. Test thoroughly
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 coding standards
- Add comments for complex logic
- Update documentation for new features
- Test with different resume formats
- Ensure environment variables work correctly

## 📚 API Usage & Costs

### OpenAI API Costs
- **Text Embeddings**: ~$0.0001 per 1K tokens
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- **Typical resume processing**: $0.01-0.05 per session

### Rate Limits
- **Free tier**: 3 requests per minute
- **Paid tier**: 3,500 requests per minute
- The app handles rate limiting gracefully

## 🔐 Security & Privacy

- **API Keys**: Never commit `.env` files to version control
- **Data Privacy**: Resume content is processed locally and via OpenAI API
- **No Data Storage**: OpenAI doesn't store your data (as per their policy)
- **Local Processing**: Vector embeddings are stored locally in ChromaDB

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing powerful language models
- **LangChain** for the excellent framework
- **Streamlit** for the intuitive web app framework
- **ChromaDB** for efficient vector storage
- **The open-source community** for inspiration and tools

## 📞 Support

If you encounter any issues or have questions:

1. **Check the troubleshooting section** above
2. **Search existing issues** on GitHub
3. **Create a new issue** with detailed description
4. **Provide logs and error messages** when reporting bugs

---

**⭐ If you find this project helpful, please consider giving it a star on GitHub!**

## Example Questions

- "What is the candidate's work experience?"
- "What programming languages does the candidate know?"
- "Tell me about the candidate's education background"
- "What are the key skills mentioned in the resume?"

## Project Structure

```
RajaChatPDF/
├── app.py              # Main Streamlit application
├── resume.pdf          # Your resume file (not tracked in git)
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Technologies Used

- **Streamlit** - Web application framework
- **LangChain** - LLM application framework
- **ChromaDB** - Vector database for embeddings
- **OpenAI** - Language model and embeddings
- **PyPDF** - PDF processing

## Configuration

You can customize the following in your `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
TEMPERATURE=0
STREAMLIT_SERVER_PORT=8501
```

## Notes

- The ChromaDB vector store is created in the `.chromadb/` directory
- Temporary files are automatically cleaned up
- The app maintains conversation state within the session
- Resume processing happens automatically when the app starts

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).