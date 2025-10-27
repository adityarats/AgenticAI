"""
Simple Agent Example

This example demonstrates how to create and use a basic autonomous agent.
"""

from agentic_ai.agent import BaseAgent
from agentic_ai.tools import CalculatorTool, WebSearchTool
from agentic_ai.memory import Memory


def main():
    print("=== Simple Agent Example ===\n")
    
    # Create an agent with tools and memory
    agent = BaseAgent(
        name="Assistant",
        role="General purpose assistant",
        tools=[CalculatorTool(), WebSearchTool()],
        memory=Memory()
    )
    
    print(f"Created agent: {agent.name}")
    print(f"Role: {agent.role}")
    print(f"Tools: {[tool.name for tool in agent.tools]}\n")
    
    # Execute a simple task
    print("Executing task: Perform a calculation...")
    result1 = agent.execute("Calculate 15 * 23 + 100")
    print(f"Result: {result1}\n")
    
    # Execute another task
    print("Executing task: Research information...")
    result2 = agent.execute("Search for information about AI agents")
    print(f"Result: {result2}\n")
    
    # Check agent state
    state = agent.get_state()
    print(f"Agent state: {state}")


if __name__ == "__main__":
    main()
