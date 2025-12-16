from agents.base import Agent
from llm import call_llm

class CoderAgent(Agent):
    SYSTEM_PROMPT = """
You are a coding assistant.
Return ONLY valid Python code.
No explanations.
"""

    def run(self, current_code, instruction):
        prompt = f"""
Current code:
{current_code}

Instruction:
{instruction}

Return updated code only.
"""
        return {
            "code": call_llm(self.SYSTEM_PROMPT, prompt, temperature=0.3)
        }
