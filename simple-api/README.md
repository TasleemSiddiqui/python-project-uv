# Random Quotes API

A simple FastAPI application that provides random side hustle ideas and money quotes.

## Features

- Random side hustle ideas endpoint
- Random money quotes endpoint
- Fast and lightweight API

## Prerequisites

- Python 3.8 or higher
- uv (Python package manager)

## Installation

1. First, install uv if you haven't already. You can install it using pip:

```bash
pip install uv
```

2. initialize project:

```bash
uv init  simple-api
cd simple-api
```

3. Create a virtual environment and activate it:

```bash
uv venv
```

4. Activate the virtual environment:

- On Windows:
```bash
.venv\Scripts\activate
```

- On Unix or MacOS:
```bash
source .venv/bin/activate
```

5. Install the required dependencies:

```bash
uv add fastapi[standard]
```

## Running the Application

1. Make sure your virtual environment is activated

2. Start the server using uvicorn:

```bash
uv run fastapi dev
```


3. The API will be available at:
   - Main URL: http://127.0.0.1:8000
   - API Documentation: http://127.0.0.1:8000/docs

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Returns a welcome message
- **Response**: "Hello World, Welcome to random quotes api"

### 2. Side Hustles
- **URL**: `/side_hustles`
- **Method**: GET
- **Description**: Returns a random side hustle idea
- **Response**: A string containing a random side hustle suggestion

### 3. Money Quotes
- **URL**: `/money_quote`
- **Method**: GET
- **Description**: Returns a random money-related quote
- **Response**: A string containing a random money quote

## Development

To add new quotes or side hustle ideas, simply edit the respective lists in `main.py`:

- `side_hustles` list for side hustle ideas
- `money_quotes` list for money quotes

## License

This project is open source and available under the MIT License.
