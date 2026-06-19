# Agentic Chatbot - LangGraph AI Application

A powerful AI chatbot application built with LangGraph, LangChain, and Streamlit that provides multiple use cases including basic chatbot functionality, web search capabilities, and AI news aggregation.

## 🌟 Features

- **Basic Chatbot**: Simple conversational AI powered by Groq LLM
- **Chatbot with Web Search**: Enhanced chatbot with real-time web search capabilities using Tavily
- **AI News Aggregator**: Fetch and summarize AI news (daily, weekly, monthly, or yearly)
- **Interactive UI**: Clean and intuitive Streamlit-based user interface
- **Multiple LLM Support**: Configurable LLM models through Groq
- **Graph-based Architecture**: Built on LangGraph for flexible workflow management

## 📋 Prerequisites

Before setting up the project, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- API Keys:
  - **GROQ_API_KEY**: Get from [Groq Console](https://console.groq.com/)
  - **TAVILY_API_KEY**: Get from [Tavily](https://tavily.com/)

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

#### For macOS/Linux:
```bash
chmod +x setup.sh
./setup.sh
```

#### For Windows:
```cmd
setup.bat
```

### Option 2: Manual Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd "Agentic Chatbot"
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**

   - macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   
   - Windows:
   ```cmd
   venv\Scripts\activate
   ```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

   Or set them in your system:
   
   - macOS/Linux:
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   export TAVILY_API_KEY="your_tavily_api_key_here"
   ```
   
   - Windows:
   ```cmd
   set GROQ_API_KEY=your_groq_api_key_here
   set TAVILY_API_KEY=your_tavily_api_key_here
   ```

6. **Run the application**
```bash
streamlit run app.py
```

## 📁 Project Structure

```
Agentic Chatbot/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── setup.sh                        # Setup script for Unix/Linux/macOS
├── setup.bat                       # Setup script for Windows
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore file
├── AINews/                         # AI news summaries storage
│   ├── daily_summary.md
│   └── weekly_summary.md
└── src/
    └── langgraphagenticai/
        ├── main.py                 # Main application logic
        ├── graph/
        │   └── graph_builder.py    # Graph construction logic
        ├── LLMS/
        │   └── groqllm.py         # Groq LLM configuration
        ├── nodes/
        │   ├── ai_news_node.py    # AI news fetching and summarization
        │   ├── basic_chatbot_node.py
        │   └── chatbot_with_Tool_node.py
        ├── state/
        │   └── state.py           # State management
        ├── tools/
        │   └── search_tool.py     # Web search tool integration
        └── ui/
            ├── uiconfigfile.ini   # UI configuration
            ├── uiconfigfile.py    # UI config loader
            └── streamlitui/
                ├── loadui.py      # UI loader
                └── display_result.py
```

## 🎯 Use Cases

### 1. Basic Chatbot
Simple conversational AI that responds to user queries using the configured LLM model.

### 2. Chatbot with Web Search
Enhanced chatbot that can search the web in real-time to provide up-to-date information using Tavily search integration.

### 3. AI News Aggregator
Fetches and summarizes the latest AI news from various sources:
- **Daily**: Last 24 hours of AI news
- **Weekly**: Last 7 days of AI news
- **Monthly**: Last 30 days of AI news
- **Yearly**: Last year of AI news

Summaries are automatically saved in the `AINews/` directory.

## 🔧 Configuration

### UI Configuration
Edit `src/langgraphagenticai/ui/uiconfigfile.ini` to customize:
- Page title
- Available LLM options
- Use case options
- Groq model options

### LLM Models
The application supports multiple Groq models. Configure your preferred model through the UI or in the configuration file.

## 📦 Dependencies

- **langchain**: LangChain framework
- **langgraph**: Graph-based workflow management
- **langchain_community**: Community tools and integrations
- **langchain_core**: Core LangChain functionality
- **langchain_groq**: Groq LLM integration
- **faiss-cpu**: Vector similarity search
- **streamlit**: Web UI framework
- **tavily-python**: Web search API
- **pydantic**: Data validation

## 🛠️ Development

### Running in Development Mode
```bash
streamlit run app.py --server.runOnSave true
```

### Adding New Use Cases
1. Create a new node in `src/langgraphagenticai/nodes/`
2. Update the graph builder in `src/langgraphagenticai/graph/graph_builder.py`
3. Add the use case to the UI configuration

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your API keys are correctly set in environment variables
   - Verify the keys are valid and have appropriate permissions

2. **Module Import Errors**
   - Make sure the virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

3. **Streamlit Port Already in Use**
   - Use a different port: `streamlit run app.py --server.port 8502`

4. **News Fetching Fails**
   - Check your Tavily API key
   - Verify internet connectivity

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue in the repository.

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Powered by [Groq](https://groq.com/)
- Search powered by [Tavily](https://tavily.com/)
- UI built with [Streamlit](https://streamlit.io/)