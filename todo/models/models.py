from tortoise import fields, models
from tortoise.contrib.pydantic import base
from tortoise.contrib.pydantic.creator import pydantic_model_creator


class Todo(models.Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    complete = fields.BooleanField()
    
Todo_Pydantic = pydantic_model_creator(Todo, name="Todo")
TodoIn_Pydantic = pydantic_model_creator(Todo, name="TodoIn", exclude_readonly=True)