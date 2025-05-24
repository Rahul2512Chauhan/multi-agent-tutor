import re #regular expression module check if a string looks like a math expression (like "2 + 3").
import os
import ast #Abstract Syntax Trees – used to safely evaluate math expressions (instead of using eval(), which is dangerous).
           #eval() takes a string and executes it as Python code. That gives it full access to your system
import operator
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class MathAgent:
    def __init__(self, model_name="gemini-1.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def _is_math_expression(self, prompt: str) -> bool:
        # Basic regex(regular expression) to detect math expressions like "2 + 3 * 4"
        return bool(re.search(r'^\s*[\d\.\+\-\*/\s\(\)]+\s*$', prompt.strip()))
        #r' -> raw-string literal, which tells Python to treat backslashes as literal characters

    def _calculate(self, expression: str) -> float:
        try:
            # Safely evaluate math expressions using AST
            expr_ast = ast.parse(expression, mode='eval')
            return self._eval_ast(expr_ast.body)
        except Exception:
            raise ValueError("Invalid characters or structure in expression.")

    def _eval_ast(self, node):
        # Only allow basic math operations
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.USub: operator.neg
        }

        if isinstance(node, ast.BinOp):
            left = self._eval_ast(node.left)
            right = self._eval_ast(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = self._eval_ast(node.operand)
            return operators[type(node.op)](operand)
        elif isinstance(node, ast.Num):  # For Python < 3.8
            return node.n
        elif isinstance(node, ast.Constant):  # For Python >= 3.8
            return node.value
        else:
            raise ValueError("Unsupported expression")

    def generate_response(self, prompt: str) -> str:
        if self._is_math_expression(prompt):
            try:
                result = self._calculate(prompt)
                return f"The result of your expression is: {result}"
            except ValueError as e:
                return str(e)
        else:
            response = self.model.generate_content(prompt)
            return response.text


# Test 
if __name__ == "__main__":
    math_agent = MathAgent()
    print(math_agent.generate_response("What is 2 + 2?"))
    print(math_agent.generate_response("Solve 3 + 4 * 2"))
    print(math_agent.generate_response("Can you explain the Pythagorean theorem?"))
