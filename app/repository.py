from typing import List, Optional
from threading import Lock
from .models import Todo


class TodoRepository:
    def __init__(self):
        self._todos: List[Todo] = []
        self._lock = Lock()

    def list(self, completed: Optional[bool] = None) -> List[Todo]:
        with self._lock:
            if completed is None:
                return list(self._todos)
            return [t for t in self._todos if t.completed == completed]

    def add(self, todo: Todo):
        with self._lock:
            if any(t.id == todo.id for t in self._todos):
                raise ValueError("Todo with this ID already exists.")
            self._todos.append(todo)

    def update(self, todo_id: int, updated: Todo):
        with self._lock:
            for idx, t in enumerate(self._todos):
                if t.id == todo_id:
                    self._todos[idx] = updated
                    return
            raise KeyError("Todo not found.")

    def delete(self, todo_id: int):
        with self._lock:
            for idx, t in enumerate(self._todos):
                if t.id == todo_id:
                    del self._todos[idx]
                    return
            raise KeyError("Todo not found.")

    def mark_complete(self, todo_id: int):
        with self._lock:
            for t in self._todos:
                if t.id == todo_id:
                    t.completed = True
                    return
            raise KeyError("Todo not found.")
