"""
Base Agent module for AgenticAI
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
import json


class AgentConfig(BaseModel):
    """Configuration for an agent"""
    name: str
    role: str
    model: str = "gpt-4"
    temperature: float = 0.7
    max_iterations: int = 10


class BaseAgent:
    """
    Base class for all autonomous agents in the AgenticAI framework.
    
    Agents are autonomous entities that can:
    - Reason about problems
    - Plan sequences of actions
    - Use tools to accomplish tasks
    - Learn from experience
    """
    
    def __init__(
        self,
        name: str,
        role: str,
        tools: Optional[List[Any]] = None,
        memory: Optional[Any] = None,
        config: Optional[AgentConfig] = None
    ):
        """
        Initialize a new agent.
        
        Args:
            name: The agent's name
            role: The agent's role/purpose
            tools: List of tools the agent can use
            memory: Memory system for the agent
            config: Additional configuration
        """
        self.name = name
        self.role = role
        self.tools = tools or []
        self.memory = memory
        self.config = config or AgentConfig(name=name, role=role)
        self.conversation_history: List[Dict[str, str]] = []
    
    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a task autonomously.
        
        Args:
            task: The task description
            
        Returns:
            Dictionary containing the result and metadata
        """
        # Add task to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": task
        })
        
        # Plan the task
        plan = self._plan(task)
        
        # Execute the plan
        result = self._execute_plan(plan)
        
        # Store result in conversation history
        self.conversation_history.append({
            "role": "assistant",
            "content": json.dumps(result)
        })
        
        return result
    
    def _plan(self, task: str) -> List[str]:
        """
        Create a plan to accomplish the task.
        
        Args:
            task: The task to plan for
            
        Returns:
            List of steps to execute
        """
        # Simple planning logic - can be overridden by subclasses
        return [f"Analyze task: {task}", "Execute task", "Validate result"]
    
    def _execute_plan(self, plan: List[str]) -> Dict[str, Any]:
        """
        Execute the planned steps.
        
        Args:
            plan: List of steps to execute
            
        Returns:
            Execution result
        """
        results = []
        for step in plan:
            step_result = self._execute_step(step)
            results.append(step_result)
        
        return {
            "status": "completed",
            "plan": plan,
            "results": results,
            "agent": self.name
        }
    
    def _execute_step(self, step: str) -> Dict[str, Any]:
        """
        Execute a single step.
        
        Args:
            step: The step to execute
            
        Returns:
            Step execution result
        """
        # Check if we can use tools for this step
        for tool in self.tools:
            if tool.can_handle(step):
                return tool.execute(step)
        
        # Default execution
        return {
            "step": step,
            "result": f"Executed: {step}",
            "success": True
        }
    
    def reset(self):
        """Reset the agent's conversation history"""
        self.conversation_history = []
    
    def get_state(self) -> Dict[str, Any]:
        """
        Get the current state of the agent.
        
        Returns:
            Dictionary containing agent state
        """
        return {
            "name": self.name,
            "role": self.role,
            "tools": [tool.__class__.__name__ for tool in self.tools],
            "conversation_length": len(self.conversation_history)
        }
