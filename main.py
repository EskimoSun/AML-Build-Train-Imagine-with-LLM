import argparse
import json
from human_eval.data import read_problems
from loop import solve_problem
from baseline import run_baseline


def main():
    parser = argparse.ArgumentParser(description="Run loop solver or baseline")
    parser.add_argument("--mode", choices=["loop", "baseline"], default="loop")
    parser.add_argument("--index", type=int, default=10, help="Problem index to run")
    args = parser.parse_args()

    problems = read_problems()
    problem_list = list(problems.values())
    if args.index < 0 or args.index >= len(problem_list):
        raise IndexError(f"index out of range (0..{len(problem_list)-1})")

    problem = problem_list[args.index]
    task = problem["prompt"]
    tests = [problem["test"]]
    entry_point = problem["entry_point"]

    if args.mode == "loop":
        success, final_code, trace = solve_problem(task, tests, entry_point)

        print("SUCCESS:", success)
        print("FINAL CODE:\n", final_code)

        with open("logs/run.json", "w") as f:
            json.dump(trace, f, indent=2)

    else:  # baseline
        success, final_code, trace = run_baseline(task, tests, entry_point)

        print("SUCCESS:", success)
        print("FINAL CODE:\n", final_code)

        with open("logs/run.json", "w") as f:
            json.dump(trace, f, indent=2)


if __name__ == "__main__":
    main()
