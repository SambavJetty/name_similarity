🌟 FastAPI Gemini Name Similarity API

A FastAPI backend that finds similar names using a Google Gemini generative AI model.
The API uses the google-generativeai Python package for embeddings and similarity search.

📦 Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>

3️⃣ Install Dependencies
pip install fastapi uvicorn google-generativeai numpy

#Create virtual env(macos/linux)

python3 -m venv venv 

source venv/bin/activate

#Create virtual env(windows)

python -m venv venv 

venv\Scripts\activate

4️⃣ Configure Gemini API Key

Open main.py and update the below given line with your Gemini API key:

genai.configure(api_key="YOUR_API_KEY_HERE")
.

🚦 Running the Server
uvicorn main:app --reload


The server will run on:

📍 http://127.0.0.1:8000

📡 API Endpoints
POST /similar-names

Find the most similar names to a given query.

✅ Request Body

{
  "name": "Githa",
  "top_k": 5
}


🔁 Response

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
