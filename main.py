from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from chunk import split_text

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Assignment 3 API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Assignment 3 FastAPI Application!"
    }


class ChunkRequest(BaseModel):
    text: str = Field(..., min_length=1)
    chunk_size: int = Field(default=50, gt=0)
    chunk_overlap: int = Field(default=10, ge=0)


@app.post("/chunk")
def chunk_endpoint(data: ChunkRequest):

    if data.chunk_overlap >= data.chunk_size:
        raise HTTPException(
            status_code=400,
            detail="chunk_overlap must be smaller than chunk_size"
        )

    try:
        chunks = split_text(
            text=data.text,
            chunk_size=data.chunk_size,
            chunk_overlap=data.chunk_overlap
        )

        return {
            "chunks": chunks,
            "total_chunks": len(chunks)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


class QueryRequest(BaseModel):
    query: str


@app.post("/llm-query")
def llm_query(data: QueryRequest):

    try:
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": data.query
                }
            ]
        )

        return {
            "query": data.query,
            "response": response.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
