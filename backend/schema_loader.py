from sqlalchemy import text

from backend.db import engine


def get_database_schema():
    """
    Fetch all tables and columns from PostgreSQL.
    """

    query = """
    SELECT
        table_name,
        column_name
    FROM information_schema.columns
    WHERE table_schema='public'
    ORDER BY table_name, ordinal_position;
    """

    with engine.connect() as connection:

        result = connection.execute(text(query))

        rows = result.fetchall()

    schema = {}

    for table_name, column_name in rows:

        if table_name not in schema:
            schema[table_name] = []

        schema[table_name].append(column_name)

    return schema


def schema_to_text(schema: dict):
    """
    Convert schema dictionary into readable text.
    """

    schema_text = ""

    for table, columns in schema.items():

        schema_text += f"\nTable: {table}\n"

        schema_text += "Columns:\n"

        for column in columns:

            schema_text += f"- {column}\n"

    return schema_text


def get_relationships():
    """
    Fetch all foreign key relationships from PostgreSQL.
    """

    query = """
    SELECT
        tc.table_name AS source_table,
        kcu.column_name AS source_column,
        ccu.table_name AS target_table,
        ccu.column_name AS target_column
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage ccu
        ON ccu.constraint_name = tc.constraint_name
    WHERE tc.constraint_type = 'FOREIGN KEY'
    ORDER BY source_table;
    """

    with engine.connect() as connection:

        result = connection.execute(text(query))

        relationships = result.fetchall()

    return relationships


def relationships_to_text(relationships):
    """
    Convert relationships into readable text.
    """

    relationship_text = "\nRelationships:\n"

    for source_table, source_column, target_table, target_column in relationships:

        relationship_text += (
            f"- {source_table}.{source_column}"
            f" -> "
            f"{target_table}.{target_column}\n"
        )

    return relationship_text


if __name__ == "__main__":

    # Display database schema
    schema = get_database_schema()

    print("=" * 60)
    print("DATABASE SCHEMA")
    print("=" * 60)

    print(schema_to_text(schema))

    # Display relationships
    relationships = get_relationships()

    print("=" * 60)
    print("DATABASE RELATIONSHIPS")
    print("=" * 60)

    print(relationships_to_text(relationships))