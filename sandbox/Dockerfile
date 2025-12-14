FROM python:3.10-slim

WORKDIR /app

COPY sandbox/run_code.py /app/run_code.py
COPY humaneval /app/humaneval

CMD ["python", "run_code.py"]