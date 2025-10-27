"""
Simple example demonstrating the Agentic AI Space framework.

This example shows how to:
1. Create a workspace
2. Add agents to the workspace
3. Execute tasks with agents
4. View workspace status

Note: Run this example from the repository root using:
    python examples/simple_example.py
Or install the package first with:
    pip install -e .
"""

import sys
import os

# For development: add src to path when running from repository
# In production, use: pip install -e .
if __name__ == "__main__":
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from agentic_ai import Workspace, Agent, AgentConfig


def main():
    """Run the simple agent example."""
    
    print("=" * 60)
    print("Agentic AI Space - Simple Example")
    print("=" * 60)
    print()
    
    # Create a workspace
    workspace = Workspace(name="Research Lab")
    print(f"Created workspace: '{workspace.name}'")
    print()
    
    # Create agents in the workspace
    researcher = workspace.create_agent(
        name="Researcher",
        description="An agent that conducts research"
    )
    print(f"Created agent: '{researcher.config.name}'")
    
    analyst = workspace.create_agent(
        name="Analyst",
        description="An agent that analyzes data"
    )
    print(f"Created agent: '{analyst.config.name}'")
    print()
    
    # List all agents
    print(f"Agents in workspace: {workspace.list_agents()}")
    print()
    
    # Execute tasks
    print("Executing tasks...")
    print("-" * 60)
    
    task1 = "Research the latest developments in AI"
    result1 = workspace.execute_task("Researcher", task1)
    print(f"Task: {task1}")
    print(f"Result: {result1['output']}")
    print()
    
    task2 = "Analyze market trends"
    result2 = workspace.execute_task("Analyst", task2)
    print(f"Task: {task2}")
    print(f"Result: {result2['output']}")
    print()
    
    # Get workspace status
    print("-" * 60)
    print("Workspace Status:")
    status = workspace.get_status()
    print(f"  Name: {status['name']}")
    print(f"  Agent Count: {status['agent_count']}")
    print(f"  Agents:")
    for agent_info in status['agents']:
        print(f"    - {agent_info['name']}: {agent_info['state']}")
    print()
    
    print("=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
