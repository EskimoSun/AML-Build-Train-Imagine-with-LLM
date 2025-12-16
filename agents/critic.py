from agents.base import Agent
from llm import call_llm
from utils import safe_json_loads

class CriticAgent(Agent):
    SYSTEM_PROMPT = """
You are a strict code reviewer.
Given failing tests and tracebacks,
produce a precise fix instruction.
Do NOT write code.
"""

    def run(self, code, test_output):
        prompt = f"""
Code:
{code}

Test output:
{test_output}

Return JSON:
{{"diagnosis": "...", "fix_instruction": "..."}}
"""
        return safe_json_loads(call_llm(self.SYSTEM_PROMPT, prompt))
