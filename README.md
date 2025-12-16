# AML-Build-Train-Imagine-with-LLM

A small framework for running LLM-driven code generation and evaluation used in the COMS4995W032 Applied Machine Learning course.

**Quick overview**
- `main.py` — entrypoint to run the iterative solver (`--mode loop`) or the baseline (`--mode baseline`).
- `llm.py` — wraps the OpenAI Python SDK client (uses `openai.OpenAI`).
- `humaneval/` — contains problem data and the simple test harness.
- `sandbox/` — utilities and a `Dockerfile` to run candidate code in an isolated container.

**Prerequisites**
- Python 3.8+ (recommended).
- Git and Docker (optional, only if you want to use the sandbox container).

1) Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

2) Install Python dependencies

```bash
pip install -r requirements.txt
```

3) Configure OpenAI credentials

```bash
export OPENAI_API_KEY="sk-..."
```

4) Run the project

Run the loop solver on problem index 10 (adjust `--index` as needed):

```bash
python main.py --mode loop --index 10
```

Run the baseline solver:

```bash
python main.py --mode baseline --index 10
```

Outputs and logs
- Run traces are written to `logs/run.json` by default.

Docker sandbox (optional)
- To build the sandbox image (used by the tester/runner to execute candidate code):

```bash
docker build -t code-sandbox -f sandbox/Dockerfile .
```

Troubleshooting
- The project currently imports a `human_eval.data` module from `main.py`. The repository includes a `humaneval/` folder (no underscore). If you see an import error like `ModuleNotFoundError: No module named 'human_eval'`, edit `main.py` and change the import to:

```python
from humaneval.test_harness import run_test  # or update `human_eval.data` -> `humaneval` as appropriate
```

- If OpenAI calls fail, ensure `OPENAI_API_KEY` is set and has appropriate access.
