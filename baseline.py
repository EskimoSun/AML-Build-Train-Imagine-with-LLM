from llm import call_llm
from agents.tester import TesterAgent

def run_baseline(prompt, tests, entry_point):
    code = call_llm(
        """
You are a coding assistant.
Return ONLY valid Python code.
No explanations.

STRICT RULES:
- Output ONLY valid Python code.
- Do NOT include markdown.
- Do NOT include explanations.
- Do NOT include comments unless necessary for correctness.
- Do NOT change function names unless explicitly instructed.
- Do NOT add parameters unless explicitly instructed.
- Do NOT reference tests, entry_point, payloads, or infrastructure.
""",
        prompt
    )
    tester = TesterAgent()
    test_out = tester.run(code, tests, entry_point)

    trace = [{
        "iteration": 0,
        "code": code,
        "test": test_out
    }]

    success = bool(test_out.get("passed", False))

    return success, code, trace
