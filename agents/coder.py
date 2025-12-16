from agents.base import Agent
from llm import call_llm

class CoderAgent(Agent):
    SYSTEM_PROMPT = """
You MUST follow the output format exactly.
If you violate the format, your output will be discarded.
Do not include markdown, explanations, or extra text.

You are a coding assistant.

Your job:
- Propose ONE minimal edit to the existing code.

STRICT RULES:
- DO NOT output full code.
- DO NOT include explanations or markdown.
- DO NOT modify unrelated code.
- DO NOT change function names or parameters unless explicitly required.
- DO NOT reference tests or infrastructure.

You MUST return valid JSON ONLY in this format:

{
  "edit_type": "replace",
  "target": "<exact substring from the current code>",
  "replacement": "<new substring>"
}

The target string MUST appear exactly once in the current code.

"""

    SYSTEM_PROMPT_ALTERNATE = """
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

    def run(self, task, current_code, instruction, alternate=False):
        prompt = f"""
CODING TASK:
{task}

CURRENT CODE:
{current_code}

INSTRUCTION:
{instruction}

Propose ONE minimal edit.
"""
        prompt_alternate = f"""
CODING TASK:
{task}

CURRENT CODE:
{current_code}

INSTRUCTION:
{instruction}

Return the updated Python code.
"""
        if alternate:
            return {
                "code": call_llm(self.SYSTEM_PROMPT_ALTERNATE, prompt_alternate, temperature=0.3)
            }

        return {
            "code": call_llm(self.SYSTEM_PROMPT, prompt, temperature=0.3)
        }
