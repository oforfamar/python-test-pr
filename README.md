# FastAPI Todo List Example

This is a simple FastAPI-based web API for managing a todo list. It demonstrates basic CRUD operations and is suitable for code review exercises.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints

- `GET /todos` - List all todos
- `POST /todos` - Add a new todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

## Notes

- This is a minimal example for interview and review purposes.
