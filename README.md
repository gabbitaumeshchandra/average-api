
# Average API

A simple REST API built using Python and Flask. It accepts numbers through a POST request and returns the average of all numbers received since the server started.

## Requirements

- Python 3.10 or newer
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/gabbitaumeshchandra/average-api
cd average-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the API

Start the server:

```bash
python app.py
```

The API runs at:

http://127.0.0.1:5000

## API Usage

### POST /average

This endpoint accepts a JSON number or an object containing a number.

Example request:

```json
10
```

Example response:

```json
{
  "average": 10.0
}
```

Send another request:

```json
20
```

The response will be:

```json
{
  "average": 15.0
}
```

You can also send an object:

```json
{
  "number": 30
}
```

The API calculates the average of all valid numbers submitted since the server started.

### Example using curl

```bash
curl -X POST http://127.0.0.1:5000/average \
  -H "Content-Type: application/json" \
  -d "10"
```

### Error Responses

- `400 Bad Request`: The input is not a valid number.
- `415 Unsupported Media Type`: The request is not sent as JSON.

Invalid requests do not change the stored numbers.

## Run Tests

Run the automated tests using:

```bash
python -m pytest -v
```

## Git Hooks

This project uses a Git commit-message hook to check Conventional Commit messages.

Enable the hook from the project directory:

```bash
git config core.hooksPath .githooks
```

On Git Bash or macOS/Linux, make the hook executable:

```bash
chmod +x .githooks/commit-msg
```

Example of a valid commit message:

```text
feat: add average API
```

The hook must be enabled in each local clone.

## Limitations

- Numbers are stored in memory.
- The numbers are cleared when the server restarts.
- The project is intended for a small assignment and is not configured for production deployment.
