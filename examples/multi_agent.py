"""
Multi-Agent Collaboration Example

This example shows how to use the orchestrator to coordinate multiple agents.
"""

from agentic_ai.agent import BaseAgent
from agentic_ai.orchestrator import AgentOrchestrator
from agentic_ai.tools import CalculatorTool, WebSearchTool


def main():
    print("=== Multi-Agent Collaboration Example ===\n")
    
    # Create multiple specialized agents
    research_agent = BaseAgent(
        name="Researcher",
        role="Research and gather information",
        tools=[WebSearchTool()]
    )
    
    analyst_agent = BaseAgent(
        name="Analyst",
        role="Analyze data and perform calculations",
        tools=[CalculatorTool()]
    )
    
    # Create orchestrator and register agents
    orchestrator = AgentOrchestrator()
    orchestrator.register_agent(research_agent)
    orchestrator.register_agent(analyst_agent)
    
    print(f"Registered agents: {orchestrator.get_agents()}\n")
    
    # Execute tasks with different agents
    print("Task 1: Research with Researcher agent")
    result1 = orchestrator.execute_task(
        "Find information about machine learning",
        "Researcher"
    )
    print(f"Result: {result1}\n")
    
    print("Task 2: Calculate with Analyst agent")
    result2 = orchestrator.execute_task(
        "Calculate the sum of 100 and 250",
        "Analyst"
    )
    print(f"Result: {result2}\n")
    
    # Collaborative task
    print("Task 3: Collaboration between agents")
    collab_result = orchestrator.collaborate(
        "Research AI and calculate market size",
        ["Researcher", "Analyst"]
    )
    print(f"Collaboration result: {collab_result}\n")
    
    # View execution history
    history = orchestrator.get_history()
    print(f"Execution history ({len(history)} entries)")


if __name__ == "__main__":
    main()
