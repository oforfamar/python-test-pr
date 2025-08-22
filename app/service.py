from typing import List, Optional
from .models import Todo
from .repository import TodoRepository
from .utils import parse_due_date


class TodoService:
    def __init__(self, repo: TodoRepository):
        self.repo = repo

    async def list_todos(self, completed: Optional[bool] = None) -> List[Todo]:
        return self.repo.list(completed)

    async def add_todo(self, todo: Todo):
        # Subtle bug: due_date is not validated
        if todo.due_date:
            todo.due_date = parse_due_date(todo.due_date)
        self.repo.add(todo)

    async def update_todo(self, todo_id: int, updated: Todo):
        self.repo.update(todo_id, updated)

    async def delete_todo(self, todo_id: int):
        self.repo.delete(todo_id)

    async def mark_complete(self, todo_id: int):
        self.repo.mark_complete(todo_id)
