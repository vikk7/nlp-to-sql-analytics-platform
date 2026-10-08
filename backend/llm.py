import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def clean_sql(sql: str):
    """
    Remove Markdown formatting.
    """

    if not sql:
        return None

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()

def generate_sql(prompt: str):
    """
    Send prompt to Gemini and return clean SQL.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    sql = clean_sql(response.text)

    if sql is None:
        raise Exception("Gemini did not return any SQL.")

    return sql


if __name__ == "__main__":

    prompt = """
    You are a PostgreSQL expert.

    Generate SQL only.

    Table:
    customers(customer_id, name, city, state)

    User Question:
    Show all customers.
    """

    sql = generate_sql(prompt)

    print(sql)