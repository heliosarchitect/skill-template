# Basic Usage Examples

## Example 1: Simple Execution

```bash
./scripts/example_script.sh "Hello World"
```

**Output:**
```
Running skill with ARG1=Hello World
Result: Example result
```

## Example 2: With Additional Arguments

```bash
./scripts/example_script.sh arg1 arg2
```

## Example 3: Using Python Script

```bash
# Basic usage
./scripts/example_script.py "test input"

# With optional argument
./scripts/example_script.py "test input" --arg2 "additional data"

# JSON output
./scripts/example_script.py "test input" --json
```

**JSON Output:**
```json
{
  "status": "success",
  "arg1": "test input",
  "arg2": null,
  "result": "Example result"
}
```

## Example 4: From OpenClaw

When loaded as a skill, OpenClaw will detect and use it automatically based on context.

You can also invoke it directly:

```
Run the skill-name script with parameter X
```

## Example 5: Error Handling

If required environment variables are missing:

```bash
unset REQUIRED_API_KEY
./scripts/example_script.sh test
```

**Output:**
```
Error: REQUIRED_API_KEY environment variable not set
Set it with: export REQUIRED_API_KEY=your_key_here
```

## Advanced Usage

See the references/ directory for advanced configuration and API documentation.
