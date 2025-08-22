from fastapi import FastAPI, HTTPException, Depends, Query
from typing import List, Optional
from .models import Todo
from .service import TodoService
from .repository import TodoRepository

app = FastAPI()


# Dependency injection
def get_service():
    repo = TodoRepository()
    return TodoService(repo)


@app.get("/todos", response_model=List[Todo])
async def list_todos(
    completed: Optional[bool] = Query(None), service: TodoService = Depends(get_service)
):
    return await service.list_todos(completed)


@app.post("/todos", response_model=Todo)
async def add_todo(todo: Todo, service: TodoService = Depends(get_service)):
    try:
        await service.add_todo(todo)
        return todo
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int, updated: Todo, service: TodoService = Depends(get_service)
):
    try:
        await service.update_todo(todo_id, updated)
        return updated
    except KeyError:
        raise HTTPException(status_code=404, detail="Todo not found.")


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, service: TodoService = Depends(get_service)):
    try:
        await service.delete_todo(todo_id)
        return {"detail": "Todo deleted."}
    except KeyError:
        raise HTTPException(status_code=404, detail="Todo not found.")


@app.patch("/todos/{todo_id}/complete", response_model=Todo)
async def complete_todo(todo_id: int, service: TodoService = Depends(get_service)):
    try:
        await service.mark_complete(todo_id)
        # Subtle issue: returns the first matching todo, not necessarily the updated one
        return (await service.list_todos())[0]
    except KeyError:
        raise HTTPException(status_code=404, detail="Todo not found.")
