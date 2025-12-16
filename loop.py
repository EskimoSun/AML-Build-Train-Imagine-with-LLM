from agents.manager import ManagerAgent
from agents.coder import CoderAgent
from agents.tester import TesterAgent
from agents.critic import CriticAgent
from diff_utils import apply_diff

MAX_ITERS = 10

def solve_problem(task, tests, entry_point, initial_code=""):
    manager = ManagerAgent()
    coder = CoderAgent()
    tester = TesterAgent()
    critic = CriticAgent()

    code = initial_code
    critic_feedback = None
    trace = []

    for i in range(MAX_ITERS):
        plan = manager.run(task, i, trace[-1] if trace else None)

        if plan.get("done"):
            break

        for attempt in range(3):
            diff = coder.run(
            task=task,
            current_code=code,
            instruction=critic_feedback or plan["step_goal"]
            )["code"]

            try:
                code = apply_diff(code, diff)
                break  # Exit the retry loop if successful
            except Exception:
                continue
        else:
            # If all attempts fail, apply the last alternative
            code = coder.run(
            task=task,
            current_code=code,
            instruction=critic_feedback or plan["step_goal"],
            alternate=True
            )["code"]

        test_out = tester.run(code, tests, entry_point)

        trace.append({
            "iteration": i,
            "code": code,
            "test": test_out
        })

        if test_out["passed"]:
            return True, code, trace


        critic_feedback = critic.run(task, code, test_out)["fix_instruction"]

    return False, code, trace
