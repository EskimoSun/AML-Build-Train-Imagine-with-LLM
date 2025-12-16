import json
from human_eval.data import read_problems
from loop import solve_problem

problems = read_problems()
problem = list(problems.values())[0]

task = problem["prompt"]
tests = [problem["test"]]
entry_point = problem["entry_point"]

success, final_code, trace = solve_problem(task, tests, entry_point)

print("SUCCESS:", success)
print("FINAL CODE:\n", final_code)

with open("logs/run.json", "w") as f:
    json.dump(trace, f, indent=2)
