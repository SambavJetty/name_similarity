# 🌟 FastAPI Gemini Name Similarity API

A FastAPI backend that finds similar names using Google Gemini generative AI model. The API uses the `google-generativeai` Python package for embeddings and similarity search to provide intelligent name matching capabilities.

## 📋 Features

- **AI-Powered Name Matching**: Uses Google Gemini AI for intelligent name similarity detection
- **RESTful API**: Clean FastAPI endpoints for easy integration
- **Configurable Results**: Adjustable top-k results for flexible matching
- **High Performance**: Fast similarity search with numerical scoring

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key

### 📦 Installation

1. **Clone the Repository**
   \`\`\`
   git clone <your-repo-url>
   \`\`\`

2. **Create Virtual Environment**

   **macOS/Linux:**
   \`\`\`
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`

   **Windows:**
   \`\`\`
   python -m venv venv
   venv\Scripts\activate
   \`\`\`

3. **Install Dependencies**
   \`\`\`
   pip install fastapi uvicorn google-generativeai numpy
   \`\`\`

4. **Configure API Key**
   
   Open `main.py` and update the following line with your Gemini API key:
   \`\`\`python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   \`\`\`

## 🚦 Running the Server

Start the development server:

\`\`\`
uvicorn main:app --reload
\`\`\`

The server will be available at: **http://127.0.0.1:8000**

## 📡 API Documentation

### Find Similar Names

**Endpoint:** `POST /similar-names`

Find the most similar names to a given query using AI-powered matching.

#### Request Body

\`\`\`json
{
  "name": "Githa",
  "top_k": 5
}
\`\`\`

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `name` | string | The name to find similarities for | Required |
| `top_k` | integer | Number of top matches to return | 5 |

#### Response

\`\`\`json
{
  "input": "Githa",
  "best_match": {
    "name": "Githa",
    "score": 1.0
  },
  "ranked_matches": [
    {"name": "Githa", "score": 1.0},
    {"name": "Geetha", "score": 0.8946},
    {"name": "Geeta", "score": 0.8891},
    {"name": "Gita", "score": 0.8712},
    {"name": "Gitu", "score": 0.8577}
  ]
}
