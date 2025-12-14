import traceback

def run_test(code: str, test: str, entry_point: str):
    namespace = {}
    try:
        # Load candidate code
        exec(code, namespace)

        # Load test code (defines check)
        exec(test, namespace)

        # Call check(candidate)
        candidate = namespace[entry_point]
        namespace["check"](candidate)

        return {"passed": True}
    except Exception:
        return {
            "passed": False,
            "traceback": traceback.format_exc()
        }
