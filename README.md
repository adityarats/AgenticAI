# AgenticAI Space

A minimal framework for building autonomous AI agents and agentic systems.

## Overview

**AgenticAI Space** provides a lightweight, extensible framework for creating and managing autonomous AI agents. The framework enables you to build agentic systems where multiple agents can work independently or collaboratively within a shared workspace.

## Key Concepts

- **Agent**: An autonomous entity that can execute tasks, maintain state, and use tools
- **Workspace**: A managed environment where multiple agents operate and share resources
- **Agentic AI**: AI systems that can act autonomously to achieve goals

## Features

- 🤖 Simple agent creation and management
- 🏢 Workspace-based organization for multiple agents
- 🔧 Tool integration for agent capabilities
- 📊 State management and tracking
- 🎯 Task execution framework
- 🔌 Extensible architecture

## Installation

```bash
# Clone the repository
git clone https://github.com/adityarats/AgenticAI.git
cd AgenticAI

# Install in development mode
pip install -e .
```

## Quick Start

```python
from agentic_ai import Workspace

# Create a workspace
workspace = Workspace(name="My Workspace")

# Create agents
researcher = workspace.create_agent(
    name="Researcher",
    description="Conducts research tasks"
)

analyst = workspace.create_agent(
    name="Analyst", 
    description="Analyzes data and findings"
)

# Execute tasks
result = workspace.execute_task("Researcher", "Research AI trends")
print(result['output'])

# Check workspace status
status = workspace.get_status()
print(f"Workspace has {status['agent_count']} agents")
```

## Examples

Run the simple example:

```bash
python examples/simple_example.py
```

## Project Structure

```
AgenticAI/
├── src/
│   └── agentic_ai/
│       ├── __init__.py
│       ├── agent.py       # Core agent implementation
│       └── workspace.py   # Workspace management
├── examples/
│   └── simple_example.py  # Basic usage example
├── setup.py
├── requirements.txt
└── README.md
```

## Architecture

The framework is built around two main components:

### Agent

The `Agent` class represents an autonomous entity that can:
- Execute tasks independently
- Maintain internal state
- Use tools and capabilities
- Make decisions based on context

### Workspace

The `Workspace` class provides:
- A container for multiple agents
- Shared state management
- Agent lifecycle management
- Task routing and coordination

## Usage

### Creating Agents

```python
from agentic_ai import Agent, AgentConfig

# Configure and create an agent
config = AgentConfig(
    name="Assistant",
    description="A helpful assistant agent",
    max_iterations=10
)
agent = Agent(config)

# Execute a task
result = agent.execute("Complete a task")
print(result)
```

### Using Workspaces

```python
from agentic_ai import Workspace

# Create workspace
workspace = Workspace(name="Production")

# Add multiple agents
workspace.create_agent("Agent1", "First agent")
workspace.create_agent("Agent2", "Second agent")

# List all agents
print(workspace.list_agents())

# Execute tasks with specific agents
workspace.execute_task("Agent1", "Process data")
workspace.execute_task("Agent2", "Generate report")
```

### Adding Tools to Agents

```python
def search_tool(query: str) -> str:
    """A simple search tool."""
    return f"Results for: {query}"

agent.add_tool(search_tool)
```

## Contributing

Contributions are welcome! This is a minimal framework designed to be extended.

## License

This project is open source and available under the MIT License.

## Roadmap

Future enhancements may include:
- Advanced agent communication protocols
- Tool management system
- Memory and context handling
- Multi-agent collaboration patterns
- Integration with LLM APIs
- Persistence and logging
- Performance monitoring

## Support

For issues and questions, please use the GitHub issue tracker.