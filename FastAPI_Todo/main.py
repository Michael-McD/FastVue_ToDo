from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

from todo.models.models import Todo, Todo_Pydantic, TodoIn_Pydantic

app = FastAPI()

class Status(BaseModel):
    message: str

@app.get("/todos", response_model=List[Todo_Pydantic])
async def get_todos():
    return await Todo_Pydantic.from_queryset(Todo.all())

@app.get("/todos/{todo_id}", response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_todo(todo_id: int):
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=todo_id))

@app.post("/todos", response_model=Todo_Pydantic)
async def create_todo(todo: TodoIn_Pydantic):
    todo_obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(todo_obj)

@app.put("/todos/{todo_id}", response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_todo(todo_id: int, todo: TodoIn_Pydantic):
    await Todo.filter(id=todo_id).update(**todo.dict(exclude={"id"}, exclude_unset=True))
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=todo_id))

@app.delete("/todos/{todo_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_todo(todo_id: int):
    deleted_count = await Todo.filter(id=todo_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")
    return Status(message=f"Deleted todo {todo_id}")

register_tortoise(
    app,
    db_url="postgres://postgres:Hoxton12@localhost:5432/Todo",
    modules={"models":["todo.models.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
