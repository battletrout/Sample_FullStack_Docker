from typing import List

# Pydantic's base model guarantees the fields that will be output (or inoput?)
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int #= None

DB: List[Person] = [
    Person(id=1, name="John", age=32),
    Person(id=2, name="Jane", age=35),
    Person(id=3, name="paul", age=35),
    Person(id=4, name="vicky", age=21)
]

@app.get("/api")
def read_root():
    return DB
    #return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: List[str] = None):
    return {"item_id": item_id, "q": q}