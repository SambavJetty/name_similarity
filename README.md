📂 Project Structure
project-root/
│
├── main.py               # FastAPI app
├── venv/                 # Python virtual environment (ignored in git)
├── requirements.txt      # Project dependencies
└── README.md             # You're reading this!

📦 Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>

2️⃣ Create and Activate a Virtual Environment
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install fastapi uvicorn google-generativeai numpy

4️⃣ Configure Gemini API Key

Open main.py and update the following line with your Gemini API key:

genai.configure(api_key="YOUR_API_KEY_HERE")


You can get your API key from 👉 Google MakerSuite
.

🚦 Running the Server
uvicorn main:app --reload


Runs on: http://127.0.0.1:8000

📡 API Endpoints
🔍 POST /similar-names

Finds names most similar to a given input name using Gemini Flash Lite.

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
