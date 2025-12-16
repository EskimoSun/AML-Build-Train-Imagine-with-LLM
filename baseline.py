from llm import call_llm
from runner import run_in_sandbox

def run_baseline(prompt, tests, entry_point):
    code = call_llm(
        """
You are a coding assistant.
Return ONLY valid Python code.
No explanations.
""",
        prompt
    )
    return run_in_sandbox(code, tests, entry_point)
