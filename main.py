from typing import * 
from pydantic import BaseModel 

class Person(BaseModel):
    name: str
    age: int 
    id : int 

obj1 : dict = {
    "name" : "A1",
    "age": 31,
    "id": 1
}

obj2 = {
    "name" : "A2",
    "age": 25, 
    "id": 2 
}

obj3 = {
    "name" : "A3",
    "age": 25, 
    "id": 2 
}

persons : List[Person] = [Person(**obj1), Person(**obj2), Person(**obj3)]

for p in persons: 
    print(p.model_dump())


