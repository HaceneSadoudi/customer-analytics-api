from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from script import main

class TextItem(BaseModel):
    text: str

app = FastAPI()


def process_text(text: str) -> dict:
    return main(text)

@app.post("/process/")
async def process_text_endpoint(item: TextItem):
    result = process_text(item.text)
    return result