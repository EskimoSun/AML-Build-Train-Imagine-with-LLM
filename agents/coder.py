from agents.base import Agent
from llm import call_llm

class CoderAgent(Agent):
    SYSTEM_PROMPT = """
You MUST follow the output format exactly.
If you violate the format, your output will be discarded.
Do not include markdown, explanations, or extra text.

You are a coding assistant.

Your job:
- Modify the given Python code to satisfy the instruction.

STRICT RULES:
- Output ONLY valid Python code.
- Do NOT include markdown.
- Do NOT include explanations.
- Do NOT include comments unless necessary for correctness.
- Do NOT change function names unless explicitly instructed.
- Do NOT add parameters unless explicitly instructed.
- Do NOT reference tests, entry_point, payloads, or infrastructure.

If the instruction is unclear, make the minimal safe change.

"""

    def run(self, task, current_code, instruction):
        prompt = f"""
CODING TASK:
{task}

CURRENT CODE:
{current_code}

INSTRUCTION:
{instruction}

Return the updated Python code.
"""
        return {
            "code": call_llm(self.SYSTEM_PROMPT, prompt, temperature=0.3)
        }
