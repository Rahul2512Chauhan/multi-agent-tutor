from fastapi import FastAPI , Request
from pydantic import BaseModel
from agents.tutor_agent import TutorAgent
import os
from dotenv import load_dotenv

load_dotenv()   

app = FastAPI()
agent = TutorAgent()    #initialize the TutorAgent  

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(data: Question):
    response = agent.generate_response(data.question)
    return {"response": response}

from fastapi.responses import FileResponse

@app.get("/")
async def serve_homepage():
    return FileResponse("static/index.html")
