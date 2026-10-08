from pathlib import Path

from backend.schema_cache import (
    get_cached_schema,
    get_cached_relationships
)


def load_sql_prompt(question: str):
    """
    Load the SQL prompt and inject cached schema,
    relationships and user question.
    """

    # Read prompt template
    prompt_path = Path("prompts/sql_prompt.txt")
    prompt = prompt_path.read_text()

    # Get cached schema
    schema_text = get_cached_schema()

    # Get cached relationships
    relationship_text = get_cached_relationships()

    # Replace placeholders
    prompt = prompt.replace(
        "<DATABASE_SCHEMA>",
        schema_text
    )

    prompt = prompt.replace(
        "<DATABASE_RELATIONSHIPS>",
        relationship_text
    )

    prompt = prompt.replace(
        "<USER_QUESTION>",
        question
    )

    return prompt


if __name__ == "__main__":

    from backend.schema_cache import load_schema_cache

    # Load cache for standalone testing
    load_schema_cache()

    question = "Show customer names and product names."

    print(load_sql_prompt(question))