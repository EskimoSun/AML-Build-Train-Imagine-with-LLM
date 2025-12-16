import json
from agents.base import Agent
from llm import call_llm
from utils import safe_json_loads

class ManagerAgent(Agent):
    SYSTEM_PROMPT = """
You MUST follow the output format exactly.
If you violate the format, your output will be discarded.
Do not include markdown, explanations, or extra text.

You are a software project manager.

Your job:
- Decide the next high-level step to implement the task and fix the code.
- Stop the process only when all tests pass.

STRICT RULES:
- NEVER write code.
- NEVER mention implementation details.
- NEVER mention Docker, entry_point, sandbox, or test harness internals.
- NEVER return empty output.
- ALWAYS return valid JSON.
- Do NOT include markdown or explanations.

Output format (JSON only):
{
  "step_goal": "<one concrete action to improve the code>",
  "done": <true | false>
}

"""

    def run(self, task, iteration, test_summary=None):
        prompt = f"""
TASK:
{task}

CURRENT ITERATION:
{iteration}

LATEST TEST RESULT:
{test_summary}

Decide the next step.
"""
        return safe_json_loads(call_llm(self.SYSTEM_PROMPT, prompt))
