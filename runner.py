import json
import subprocess
import tempfile
import os

def run_in_sandbox(code, tests, entry_point, timeout=10):
    with tempfile.TemporaryDirectory() as tmp:
        input_path = os.path.join(tmp, "input.json")

        with open(input_path, "w") as f:
            json.dump(
                {
                    "code": code,
                    "tests": tests,
                    "entry_point": entry_point,
                },
                f
            )

        result = subprocess.run(
            [
                "docker", "run", "--rm",
                "-v", f"{input_path}:/app/input.json",
                "code-sandbox"
            ],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
