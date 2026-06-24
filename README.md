# Assignment 3 - FastAPI Text Chunking API

## Overview

This project is a FastAPI application that provides:

* Welcome endpoint
* Text chunking using LangChain's RecursiveCharacterTextSplitter
* Custom chunk size and overlap support
* LLM query endpoint using Groq API
* Input validation and error handling

---

## Features

### 1. Welcome Endpoint

**GET /**

Returns a welcome message.

Example Response:

```json
{
  "message": "Welcome to Assignment 3 FastAPI Application!"
}
```

---

### 2. Text Chunking Endpoint

**POST /chunk**

Splits large text into smaller chunks using RecursiveCharacterTextSplitter.

#### Request Body

```json
{
  "text": "Your large text here",
  "chunk_size": 50,
  "chunk_overlap": 10
}
```

#### Response

```json
{
  "chunks": [
    "chunk 1",
    "chunk 2"
  ],
  "total_chunks": 2
}
```

---

### 3. LLM Query Endpoint

**POST /llm-query**

Uses Groq API to answer user queries.

#### Request Body

```json
{
  "query": "Explain FastAPI"
}
```

#### Response

```json
{
  "query": "Explain FastAPI",
  "response": "FastAPI is..."
}
```

---

## Project Structure

```text
assignment_3/
│
├── main.py
├── chunk.py
├── requirements.txt
├── .env
├── Dockerfile
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-link>
cd assignment_3
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

```bash
uvicorn main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Dependencies

* FastAPI
* Uvicorn
* LangChain Text Splitters
* Pydantic
* Groq
* Python Dotenv

---

## Deployment

The application can be deployed on:

* Render
* Hugging Face Spaces
* FastAPI Cloud

---

## Author

Name: Shrushti

Assignment 3 Submission
