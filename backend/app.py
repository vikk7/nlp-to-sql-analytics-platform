from fastapi import FastAPI

from backend.models import UserQuery
from backend.db import run_query
from backend.prompt_loader import load_sql_prompt
from backend.llm import generate_sql
from backend.validator import validate_sql
from backend.retry import retry_sql
from backend.input_validator import validate_question
from backend.schema_cache import (
    load_schema_cache
)

# Initialize FastAPI application
app = FastAPI()

# Load schema cache on application startup
load_schema_cache()

@app.get("/")
def home():
    """
    Home endpoint.
    """
    return {
        "message": "Welcome to NLP-to-SQL Analytics Platform 🚀"
    }


@app.get("/customers")
def get_customers():
    """
    Fetch all customers.
    """

    query = "SELECT * FROM customers;"

    # Execute SQL
    result, error = run_query(query)

    # Handle database error
    if error:
        return {
            "status": "error",
            "message": error
        }

    return result.to_dict(orient="records")


@app.post("/query")
def process_query(user_query: UserQuery):
    """
    Generate, validate and execute SQL.
    """
    # Validate user question
    is_valid, message = validate_question(user_query.question)

    if not is_valid:
        return {
            "status": "error",
            "message": message
    }

    # Build AI prompt
    prompt = load_sql_prompt(user_query.question)

    # Generate SQL
    try:

        sql = generate_sql(prompt)

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
    }

    print("\n" + "=" * 60)
    print("Generated SQL:")
    print(sql)
    print("=" * 60)

    # Validate SQL
    is_valid, message = validate_sql(sql)

    if not is_valid:
        return {
            "status": "error",
            "message": message,
            "generated_sql": sql
        }

    # Execute SQL
    result, error = run_query(sql)

    # Retry if database execution fails
    if error:

        print("\nRetrying SQL...\n")

        corrected_sql = retry_sql(
            prompt=prompt,
            failed_sql=sql,
            error=error
        )

        print("=" * 60)
        print("Corrected SQL:")
        print(corrected_sql)
        print("=" * 60)

        # Validate corrected SQL
        is_valid, message = validate_sql(corrected_sql)

        if not is_valid:
            return {
                "status": "error",
                "message": message,
                "generated_sql": corrected_sql
            }

        # Execute corrected SQL
        result, error = run_query(corrected_sql)

        # Retry also failed
        if error:
            return {
                "status": "error",
                "question": user_query.question,
                "generated_sql": corrected_sql,
                "message": error
            }

        # Retry succeeded
        return {
            "status": "success",
            "question": user_query.question,
            "generated_sql": corrected_sql,
            "retried": True,
            "total_records": len(result),
            "data": result.to_dict(orient="records")
        }

    # Original query succeeded
    return {
        "status": "success",
        "question": user_query.question,
        "generated_sql": sql,
        "retried": False,
        "total_records": len(result),
        "data": result.to_dict(orient="records")
    }