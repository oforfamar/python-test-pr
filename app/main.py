from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


todos: List[Todo] = []


@app.get("/todos", response_model=List[Todo])
def list_todos():
    return todos


@app.post("/todos", response_model=Todo)
def add_todo(todo: Todo):
    if any(t.id == todo.id for t in todos):
        raise HTTPException(status_code=400, detail="Todo with this ID already exists.")
    todos.append(todo)
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated: Todo):
    for idx, t in enumerate(todos):
        if t.id == todo_id:
            todos[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found.")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for idx, t in enumerate(todos):
        if t.id == todo_id:
            del todos[idx]
            return {"detail": "Todo deleted."}
    raise HTTPException(status_code=404, detail="Todo not found.")
