# 🤖 Multi-Agent Tutor Bot

An intelligent multi-agent tutor bot built using FastAPI + Gemini API, capable of answering domain-specific questions from Math, Physics, and Chemistry with subject-specific tools.

## 🚀 Live Demo

👉 [Click here to try the app](https://multi-agent-tutor-production.up.railway.app)

---

## 🧩 Architecture

- **TutorAgent**: Main agent that routes the question to the correct sub-agent.
- **MathAgent**: Answers math-related questions using a calculator tool.
- **PhysicsAgent**: Answers physics-related questions using constants lookup.
- **ChemistryAgent**: Answers chemistry-related questions using a formula lookup.
- **Fallback**: Handles general questions and small talk.

### 🔧 Tools Used

- gemini-1.5-flash (for natural language understanding)
- FastAPI (backend)
- Vanilla HTML + JavaScript (frontend)
- Railway (deployment)

---

## 📁 Folder Structure

multi-agent-tutor/
│
├── agents/
│ ├── tutor_agent.py
│ ├── math_agent.py
│ ├── physics_agent.py
│ └── chemistry_agent.py
│
├── static/
│ └── index.html
│
├── app.py
├── .env.example
├── requirements.txt
├── Procfile
└── README.md


---

## ⚙️ Setup Instructions

### 🔑 Environment Variables

Create a `.env` file based on `.env.example` and add your Gemini API Key:

```env
GEMINI_API_KEY=your_api_key_here



🛠️ Local Development

Clone the repo:

git clone https://github.com/Rahul2512Chauhan/multi-agent-tutor.git

cd multi-agent-tutor


Install dependencies:

pip install -r requirements.txt


Run the app:

uvicorn app:app --reload


Open browser at:

http://127.0.0.1:8000


💡 How it Works

1.User submits a question via the frontend.

2.TutorAgent classifies the subject.

3.Routes to the correct agent: MathAgent, PhysicsAgent, or ChemistryAgent.

4.Agent processes the question using its specialized tool.

5.Response is returned to the user.


✅ Status

1.Working locally

2.Live deployed

3.All agents implemented

4.Gemini API integrated

5.Frontend built


📌 Submission

🔗 GitHub Repo: https://github.com/Rahul2512Chauhan/multi-agent-tutor

🌐 Live App: https://multi-agent-tutor-production.up.railway.app


🙌 Acknowledgements

Thanks to Gemini API, Railway, and FastAPI for making rapid prototyping easy!