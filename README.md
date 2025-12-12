# FastAPI Calculator

A simple FastAPI application to add and multiply two numbers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI application for addition:
   ```bash
   uvicorn add:app --reload
   ```
   Or for multiplication:
   ```bash
   uvicorn multiply:app --reload
   ```

2. The application will be running at `http://127.0.0.1:8000`.

## Running Tests

To run the tests, use the following command:
```bash
pytest
```

## API Endpoints

### POST /add

This endpoint adds two numbers together.

**Request Body:**
```json
{
  "a": integer,
  "b": integer
}
```

**Response:**
```json
{
  "result": integer
}
```

### POST /multiply

This endpoint multiplies two numbers together.

**Request Body:**
```json
{
  "a": integer,
  "b": integer
}
```

**Response:**
```json
{
  "result": integer
}
```
