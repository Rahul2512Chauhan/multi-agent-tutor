import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class ChemistryAgent:
    def __init__(self, model_name="gemini-1.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

        # Tool: Common compound name/formula lookup
        self.chemical_dict = {
            "salt": "NaCl (Sodium Chloride)",
            "water": "H₂O",
            "carbon dioxide": "CO₂",
            "ammonia": "NH₃",
            "glucose": "C₆H₁₂O₆",
            "ethanol": "C₂H₅OH",
            "hydrochloric acid": "HCl"
        }

    def _lookup_chemical_formula(self, prompt: str) -> str:
        for name, formula in self.chemical_dict.items():
            if name.lower() in prompt.lower():
                return f"The chemical formula of {name} is {formula}."
        return None

    def generate_response(self, prompt: str) -> str:
        tool_response = self._lookup_chemical_formula(prompt)
        if tool_response:
            return tool_response
        else:
            response = self.model.generate_content(prompt)
            return response.text

#Test
if __name__ == "__main__":
    chem_agent = ChemistryAgent()
    print(chem_agent.generate_response("What is the chemical formula of water?"))
    print(chem_agent.generate_response("Explain what an acid is."))
