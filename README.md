# NLP-to-SQL Analytics Platform

AI-powered analytics platform that converts natural-language business questions into SQL queries and returns data-driven insights.

## Features
- Natural language → SQL
- Gemini LLM integration
- PostgreSQL database
- FastAPI backend
- SQL validation
- Dynamic schema handling
- Data analysis and insights
- Interactive charts

## Architecture

User Question
      ↓
Input Validation
      ↓
Schema / Metadata
      ↓
Prompt Builder
      ↓
Gemini LLM
      ↓
SQL Generation
      ↓
SQL Validation
      ↓
PostgreSQL
      ↓
Analysis & Insights
      ↓
Charts / Results

## Tech Stack

Python | FastAPI | PostgreSQL | SQLAlchemy | Gemini | Pandas | Streamlit

## Example Questions

- What is the total revenue?
- Which products have the highest return rate?
- Who are the top 10 customers by spending?
- Which category generated the highest revenue?

## Project Structure

backend/
charts/
frontend/
prompts/

## How to Run

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Configure `.env`
5. Start FastAPI
6. Open Swagger UI

## Future Enhancements

- Multi-database support
- Advanced analytics
- Authentication
- Query caching
- LLM fallback providers
- Production deployment
