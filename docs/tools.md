# Tool Creation Guide

## Introduction

Tools extend agent capabilities by providing specific functionality. This guide covers creating custom tools.

## Basic Tool Structure

All tools inherit from `BaseTool`:

```python
from agentic_ai.tools import BaseTool, ToolConfig
from typing import Dict, Any

class MyTool(BaseTool):
    def __init__(self):
        config = ToolConfig(
            name="MyTool",
            description="what the tool does keywords"
        )
        super().__init__(config)
    
    def execute(self, input_data: Any) -> Dict[str, Any]:
        # Tool implementation
        return {
            "success": True,
            "result": "tool output"
        }
```

## Tool Configuration

The `ToolConfig` includes:
- `name`: Tool identifier
- `description`: What the tool does (used for matching)
- `enabled`: Whether the tool is active

## Implementing execute()

The `execute` method should:
1. Validate input
2. Perform the tool's function
3. Return a result dictionary

```python
def execute(self, input_data: Any) -> Dict[str, Any]:
    try:
        # Validate
        if not self.validate_input(input_data):
            return {"success": False, "error": "Invalid input"}
        
        # Execute
        result = self.perform_action(input_data)
        
        # Return
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

## Tool Matching

Override `can_handle()` for custom matching logic:

```python
def can_handle(self, task: str) -> bool:
    # Custom logic to determine if tool can handle task
    keywords = ["specific", "keywords"]
    return any(kw in task.lower() for kw in keywords)
```

## Input Validation

Implement `validate_input()` for safety:

```python
def validate_input(self, input_data: Any) -> bool:
    if not isinstance(input_data, str):
        return False
    if len(input_data) > 10000:
        return False
    return True
```

## Example: File Reader Tool

```python
class FileReaderTool(BaseTool):
    def __init__(self):
        config = ToolConfig(
            name="FileReader",
            description="read file content open load"
        )
        super().__init__(config)
    
    def execute(self, input_data: Any) -> Dict[str, Any]:
        filepath = str(input_data)
        
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            return {
                "success": True,
                "filepath": filepath,
                "content": content,
                "size": len(content)
            }
        except FileNotFoundError:
            return {
                "success": False,
                "error": f"File not found: {filepath}"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
```

## Best Practices

1. **Clear Names**: Use descriptive tool names
2. **Rich Descriptions**: Include keywords for matching
3. **Error Handling**: Always handle exceptions
4. **Input Validation**: Validate before processing
5. **Consistent Returns**: Always return a dictionary
6. **Documentation**: Document expected inputs/outputs

## Built-in Tools

AgenticAI includes these built-in tools:
- `CalculatorTool`: Mathematical calculations
- `WebSearchTool`: Web search (mock implementation)

## Next Steps

- See [agent development guide](agent_development.md)
- Check [examples](../examples/custom_tool.py) for implementations
- Review the [architecture](architecture.md)
