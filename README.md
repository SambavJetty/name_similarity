1. Clone the Repository
git clone <url>

2. Create and Activate a Virtual Environment
# Create virtual environment (Linux/macOS)
python3 -m venv venv
source venv/bin/activate

# Or on Windows
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install fastapi uvicorn google-generativeai numpy

4. Configure Gemini API Key

Open main.py and update this line with your Gemini API key:

genai.configure(api_key="YOUR_API_KEY_HERE")


You can get your API key from Google MakerSuite
.

🚦 Running the Server
uvicorn main:app --reload


Then open your browser to:

📍 http://127.0.0.1:8000/similar-names — POST endpoint

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