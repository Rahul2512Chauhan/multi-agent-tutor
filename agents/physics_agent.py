import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class PhysicsAgent:
    def __init__(self, model_name="gemini-1.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        
        self.constants = {
            "speed of light": "3.0 x 10^8 m/s",
            "gravitational constant": "6.674 x 10^-11 N·m²/kg²",
            "planck's constant": "6.626 x 10^-34 J·s",
            "elementary charge": "1.602 x 10^-19 C",
            "avogadro's number": "6.022 x 10^23 mol^-1"
        }

    def _lookup_constant(self, prompt: str) -> str:
        prompt = prompt.lower()
        for name, value in self.constants.items():
            if name in prompt:
                return f"The {name} is {value}."
        return None

    def generate_response(self, prompt: str) -> str:
        constant_info = self._lookup_constant(prompt)
        if constant_info:
            return constant_info
        else:
            response = self.model.generate_content(prompt)
            return response.text


#Test 
if __name__ == "__main__":
    agent = PhysicsAgent()
    print(agent.generate_response("What is the speed of light?"))
    print(agent.generate_response("Can you explain Newton's second law?"))
