# SQL keywords that are not allowed
FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
    "MERGE",
    "GRANT",
    "REVOKE"
]


def validate_sql(sql: str):
    """
    Validate that the generated SQL is safe to execute.
    """

    # Remove extra spaces
    sql = sql.strip()

    # Allow only SELECT queries
    if not sql.upper().startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    # Check for forbidden SQL keywords
    upper_sql = sql.upper()

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in upper_sql:
            return False, f"Forbidden SQL keyword detected: {keyword}"

    # Prevent multiple SQL statements
    if sql.count(";") > 1:
        return False, "Multiple SQL statements are not allowed."

    return True, "SQL is valid."


# Test validator
if __name__ == "__main__":

    query = "SELECT * FROM customers;"

    valid, message = validate_sql(query)

    print(valid)
    print(message)