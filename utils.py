import json

def safe_json_loads(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start == -1 or end == -1:
            raise
        return json.loads(text[start:end])
