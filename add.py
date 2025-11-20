from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    
    a: int
    b: int
    
@app.post("/add")
def add_num(numbers:Number):
    result = numbers.a + numbers.b
    return {"result": result}