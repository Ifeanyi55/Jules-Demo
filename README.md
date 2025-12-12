# FastAPI Adder

A simple FastAPI application to add two numbers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [API Endpoint](#api-endpoint)

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

1. Start the FastAPI application:
   ```bash
   uvicorn add:app --reload
   ```

2. The application will be running at `http://127.0.0.1:8000`.

## Running Tests

To run the tests, use the following command:
```bash
pytest
```

## API Endpoint

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
