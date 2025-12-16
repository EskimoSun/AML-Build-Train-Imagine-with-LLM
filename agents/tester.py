from agents.base import Agent
from runner import run_in_sandbox
import json

class TesterAgent(Agent):
    def run(self, code, tests, entry_point):
        raw = run_in_sandbox(code, tests, entry_point)
        try:
            parsed = json.loads(raw["stdout"])
        except Exception:
            parsed = {"passed": False, "error": raw["stdout"]}

        return {
            "passed": parsed.get("passed", False),
            "raw": raw,
            "parsed": parsed
        }
