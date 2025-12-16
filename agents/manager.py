import json
from agents.base import Agent
from llm import call_llm
from utils import safe_json_loads

class ManagerAgent(Agent):
    SYSTEM_PROMPT = """
You are a software project manager.
You plan the next step based on test results.
You NEVER write code.
"""

    def run(self, task, iteration, test_summary=None):
        prompt = f"""
Task:
{task}

Iteration: {iteration}

Test summary:
{test_summary}

Return JSON:
{{"step_goal": "...", "done": false}}
"""
        return safe_json_loads(call_llm(self.SYSTEM_PROMPT, prompt))
