import json

def safe_json_loads(text: str):
    if not text or not text.strip():
        return None

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start == -1 or end == -1:
            return None
        try:
            return json.loads(text[start:end])
        except Exception:
            return None