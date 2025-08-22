import pytest
from app.models import Todo
from app.repository import TodoRepository


def test_add_and_list():
    repo = TodoRepository()
    todo = Todo(id=1, title="Test", completed=False)
    repo.add(todo)
    assert len(repo.list()) == 1
    assert repo.list()[0].title == "Test"


def test_mark_complete():
    repo = TodoRepository()
    todo = Todo(id=2, title="Test2", completed=False)
    repo.add(todo)
    repo.mark_complete(2)
    assert repo.list()[0].completed is True


# Incomplete: no tests for update, delete, or due_date parsing
# Misleading: does not test error cases
