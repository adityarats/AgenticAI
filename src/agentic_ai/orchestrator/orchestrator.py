"""
Agent Orchestrator for coordinating multiple agents
"""

from typing import List, Dict, Any
from agentic_ai.agent.base_agent import BaseAgent


class AgentOrchestrator:
    """
    Orchestrator for managing and coordinating multiple agents.
    """
    
    def __init__(self):
        """Initialize the orchestrator"""
        self.agents: Dict[str, BaseAgent] = {}
        self.execution_history: List[Dict[str, Any]] = []
    
    def register_agent(self, agent: BaseAgent):
        """
        Register an agent with the orchestrator.
        
        Args:
            agent: The agent to register
        """
        self.agents[agent.name] = agent
    
    def unregister_agent(self, agent_name: str):
        """
        Unregister an agent.
        
        Args:
            agent_name: Name of the agent to unregister
        """
        if agent_name in self.agents:
            del self.agents[agent_name]
    
    def execute_task(self, task: str, agent_name: str) -> Dict[str, Any]:
        """
        Execute a task with a specific agent.
        
        Args:
            task: Task description
            agent_name: Name of the agent to use
            
        Returns:
            Task execution result
        """
        if agent_name not in self.agents:
            return {
                "success": False,
                "error": f"Agent '{agent_name}' not found"
            }
        
        agent = self.agents[agent_name]
        result = agent.execute(task)
        
        # Record execution
        self.execution_history.append({
            "task": task,
            "agent": agent_name,
            "result": result
        })
        
        return result
    
    def collaborate(self, task: str, agent_names: List[str]) -> Dict[str, Any]:
        """
        Have multiple agents collaborate on a task.
        
        Args:
            task: Task description
            agent_names: List of agent names to involve
            
        Returns:
            Collaboration result
        """
        results = {}
        
        for agent_name in agent_names:
            if agent_name in self.agents:
                result = self.execute_task(task, agent_name)
                results[agent_name] = result
        
        return {
            "task": task,
            "agents": agent_names,
            "individual_results": results,
            "collaboration": "completed"
        }
    
    def get_agents(self) -> List[str]:
        """
        Get list of registered agents.
        
        Returns:
            List of agent names
        """
        return list(self.agents.keys())
    
    def get_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get execution history.
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of recent executions
        """
        return self.execution_history[-limit:]
