def apply_diff(code: str, diff: dict) -> str:
    if diff.get("edit_type") != "replace":
        raise ValueError("Unsupported edit type")

    target = diff.get("target")
    replacement = diff.get("replacement")

    if not target or replacement is None:
        raise ValueError("Invalid diff format")

    if code.count(target) != 1:
        raise ValueError("Target must appear exactly once")

    return code.replace(target, replacement, 1)
