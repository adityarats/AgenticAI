"""
Core Agent implementation for the Agentic AI framework.
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Optional, Callable


@dataclass
class AgentConfig:
    """Configuration for an Agent."""
    name: str
    description: str = ""
    max_iterations: int = 10


class Agent:
    """
    Base Agent class for autonomous AI agents.
    
    An Agent is an autonomous entity that can:
    - Execute tasks
    - Maintain state
    - Interact with tools
    - Make decisions
    """
    
    def __init__(self, config: AgentConfig):
        """
        Initialize an Agent.
        
        Args:
            config: Agent configuration
        """
        self.config = config
        self.state: Dict[str, Any] = {}
        self.tools: List[Callable] = []
        
    def add_tool(self, tool: Callable) -> None:
        """
        Add a tool that the agent can use.
        
        Args:
            tool: A callable function that the agent can invoke
        """
        self.tools.append(tool)
        
    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a task.
        
        Args:
            task: The task description
            
        Returns:
            A dictionary containing the execution results
        """
        result = {
            "agent": self.config.name,
            "task": task,
            "status": "completed",
            "iterations": 1,
            "output": f"Agent '{self.config.name}' processed task: {task}"
        }
        
        # Update agent state
        self.state["last_task"] = task
        self.state["execution_count"] = self.state.get("execution_count", 0) + 1
        
        return result
        
    def get_state(self) -> Dict[str, Any]:
        """
        Get the current agent state.
        
        Returns:
            Current state dictionary
        """
        return self.state.copy()
        
    def reset(self) -> None:
        """Reset the agent state."""
        self.state.clear()
