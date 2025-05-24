import os
import google.generativeai as genai
from dotenv import load_dotenv
from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent
from agents.chemistry_agent import ChemistryAgent

load_dotenv()

class TutorAgent:
    def __init__(self, model_name="gemini-1.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

        # Initialize sub-agents
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()
        self.chemistry_agent = ChemistryAgent()

    
    def classify_subject(self, prompt: str) -> str:
        system_prompt = (
            "You are a subject classification assistant. "
            "Classify the following user query into one of these subjects: "
            "'math', 'physics', 'chemistry' or 'general'. If it's unrelated, return 'other'.\n\n"
            f"Query: {prompt}\nSubject:"
        )

        response = self.model.generate_content(system_prompt)
        subject = response.text.strip().lower()
        print(f"Classifying subject: {subject}")  # Now this will print the classified subject
        return subject

    def generate_response(self, prompt: str) -> str:
        subject = self.classify_subject(prompt)
        print(f"The question is classified as {subject}.")

        if subject == "math":
            return self.math_agent.generate_response(prompt)
        elif subject == "physics":
            return self.physics_agent.generate_response(prompt)
        elif subject == "chemistry":
            return self.chemistry_agent.generate_response(prompt)
        else:
            #general falback for casual chat 
            response = self.model.generate_content(prompt)
            return response.text
