import re


def validate_question(question: str):
    """
    Validate user input question.
    """

    # Check None
    if question is None:
        return False, "Question cannot be empty."

    # Remove leading/trailing spaces
    question = question.strip()

    # Empty question
    if question == "":
        return False, "Question cannot be empty."

    # Too short
    if len(question) < 3:
        return False, "Please enter a meaningful question."

    # Too long
    if len(question) > 500:
        return False, "Question is too long."

    # Allow alphabets, numbers and at least one meaningful character
    if not re.search(r"[A-Za-z0-9]", question):
        return False, "Question contains only special characters."

    return True, "Valid question."


# -------------------------
# Testing
# -------------------------
if __name__ == "__main__":

    tests = [
        "",
        "   ",
        "///",
        "@@@@@",
        "Top 2 customer by orders",
        "Show customer 101",
        "Revenue in 2025",
        "Laptop",
        "?"
    ]

    for t in tests:

        valid, message = validate_question(t)

        print(f"{t!r} -> {valid} : {message}")