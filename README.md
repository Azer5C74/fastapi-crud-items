# FastAPI RESTful CRUD for Items

This project implements a simple FastAPI-based RESTful CRUD API for managing items. It provides endpoints for creating, reading, updating, and deleting items.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Azer5C74/fastapi-crud-items.git
2. Navigate to the Repo
    ```bash
    cd fastapi-crud-items
3. Install dependencies
    ```bash
    pip3 install fastapi uvicorn

## Usage
1. Run the FastAPI application: 
    ```bash
   python3 -m uvicorn main:app --reload3
   
## API Endpoints
1. Create Item:
`POST /items/: Create a new item.`
2. Read Items:
`GET /items/: Retrieve all items.`
3. Read Item:
`GET /items/{item_id}: Retrieve a specific item.`
4. Update Item:
`PUT /items/{item_id}: Update a specific item.`
5. Delete Item:
`DELETE /items/{item_id}: Delete a specific item.`

## Running Tests
```bash
    pytest
```