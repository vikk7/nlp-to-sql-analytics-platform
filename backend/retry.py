from backend.llm import generate_sql


def retry_sql(prompt: str, failed_sql: str, error: str):
    """
    Ask Gemini to fix a failed SQL query.
    """

    retry_prompt = f"""
The following SQL query failed.

Original Prompt:

{prompt}

Generated SQL:

{failed_sql}

Database Error:

{error}

Please generate a corrected PostgreSQL SQL query.

Return SQL only.
"""

    corrected_sql = generate_sql(retry_prompt)

    return corrected_sql


if __name__ == "__main__":

    prompt = "Show customer names."

    sql = """
    SELECT name
    FROM customer;
    """

    error = """
    relation 'customer' does not exist
    """

    print(
        retry_sql(
            prompt,
            sql,
            error
        )
    )
