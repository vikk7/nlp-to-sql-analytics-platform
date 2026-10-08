from backend.schema_loader import (
    get_database_schema,
    get_relationships,
    schema_to_text,
    relationships_to_text
)

# Cache variables
_SCHEMA_TEXT = None
_RELATIONSHIP_TEXT = None


def load_schema_cache():
    """
    Load schema and relationships into memory.
    """

    global _SCHEMA_TEXT
    global _RELATIONSHIP_TEXT

    schema = get_database_schema()

    relationships = get_relationships()

    _SCHEMA_TEXT = schema_to_text(schema)

    _RELATIONSHIP_TEXT = relationships_to_text(relationships)

    print("\n✅ Database schema cached.")


def get_cached_schema():
    """
    Return cached schema.
    """

    return _SCHEMA_TEXT


def get_cached_relationships():
    """
    Return cached relationships.
    """

    return _RELATIONSHIP_TEXT


if __name__ == "__main__":

    load_schema_cache()

    print(get_cached_schema())

    print(get_cached_relationships())