import json
from humaneval.test_harness import run_test

with open("/app/input.json") as f:
    payload = json.load(f)

code = payload["code"]
tests = payload["tests"]
entry_point = payload["entry_point"]

results = []
for test in tests:
    results.append(run_test(code, test, entry_point))

print(json.dumps(results))
