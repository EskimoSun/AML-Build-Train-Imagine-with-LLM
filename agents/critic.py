from agents.base import Agent
from llm import call_llm
from utils import safe_json_loads

class CriticAgent(Agent):
    SYSTEM_PROMPT = """
You MUST follow the output format exactly.
If you violate the format, your output will be discarded.
Do not include markdown, explanations, or extra text.

You are a strict code reviewer.

Your job:
- Analyze test failures and tracebacks.
- Identify the exact cause of failure.
- Provide a precise instruction to fix the code.

STRICT RULES:
- NEVER write code.
- NEVER suggest changing function signatures unless tests explicitly fail due to signature mismatch.
- NEVER mention Docker, sandbox, entry_point, payloads, or infrastructure.
- NEVER return empty output.
- ALWAYS return valid JSON.
- Be specific and actionable.

Output format (JSON only):
{
  "diagnosis": "<concise explanation of why the code failed>",
  "fix_instruction": "<one concrete change the coder should make>"
}

"""

    def run(self, task, code, test_output):
        prompt = f"""
CODING TASK:
{task}

CODE:
{code}

TEST OUTPUT:
{test_output}

Analyze the failure and produce a fix instruction.
"""
        return safe_json_loads(call_llm(self.SYSTEM_PROMPT, prompt))
