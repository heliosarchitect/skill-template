# API Reference

Document your skill's API, external dependencies, and architecture here.

## External APIs

If your skill integrates with external services, document them:

### Example API Service

**Base URL:** `https://api.example.com/v1`

**Authentication:** Bearer token in `Authorization` header

**Endpoints:**

#### GET /data
Retrieves data from the service.

**Parameters:**
- `param` (string, required) - Description

**Response:**
```json
{
  "data": "result",
  "status": "success"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $API_KEY" \
  "https://api.example.com/v1/data?param=value"
```

## Internal Functions

Document your scripts' functions and interfaces:

### example_script.sh

#### Functions

**`main()`**
- **Description:** Main entry point
- **Arguments:** 
  - `$1` - First argument
  - `$2` - Second argument (optional)
- **Exit codes:**
  - `0` - Success
  - `1` - Error

### example_script.py

#### Functions

**`do_something(arg1: str, arg2: Optional[str]) -> dict`**
- **Description:** Main processing function
- **Arguments:**
  - `arg1` - Description
  - `arg2` - Optional description
- **Returns:** Dictionary with results
- **Raises:**
  - `ValueError` - If input invalid
  - `RuntimeError` - If API fails

## Data Structures

Document JSON schemas, data formats, etc.

### Example Output Schema

```json
{
  "status": "success",
  "result": {
    "field1": "value",
    "field2": 123
  }
}
```

## Configuration

### Environment Variables

- `REQUIRED_API_KEY` - API authentication token
- `OPTIONAL_SETTING` - Optional configuration (default: "value")

### Config Files

If your skill uses config files, document the format:

```json
{
  "setting1": "value",
  "setting2": 42
}
```

## Error Codes

Document your error codes and what they mean:

- `1` - Missing required environment variable
- `2` - API request failed
- `3` - Invalid input
- `4` - Not found

## Rate Limits

If applicable, document any rate limits or quotas.

## Links

- [External API Documentation](https://docs.example.com)
- [Related Tools](https://example.com/tools)
