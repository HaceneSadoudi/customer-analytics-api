from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.script import main

class TextItem(BaseModel):
    text: str

app = FastAPI()


def process_text(text: str) -> dict:
    return main(text)

@app.post("/process/")
async def process_text_endpoint(item: TextItem):
    result = process_text(item.text)
    return result

@app.get("/test/")
def test():
    return "Hello, world!"

@app.get("/", tags=["Root"])
async def hello():
    return { "hello": "you success deloy..." }