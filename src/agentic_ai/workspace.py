"""
Workspace management for organizing multiple agents.
"""

from typing import Dict, List, Optional
from .agent import Agent, AgentConfig


class Workspace:
    """
    A Workspace manages multiple agents and coordinates their activities.
    
    The Workspace serves as the "space" where agentic AI systems operate,
    providing:
    - Agent lifecycle management
    - Communication between agents
    - Shared resources and state
    """
    
    def __init__(self, name: str):
        """
        Initialize a Workspace.
        
        Args:
            name: Name of the workspace
        """
        self.name = name
        self.agents: Dict[str, Agent] = {}
        self.shared_state: Dict[str, any] = {}
        
    def add_agent(self, agent: Agent) -> None:
        """
        Add an agent to the workspace.
        
        Args:
            agent: The agent to add
        """
        self.agents[agent.config.name] = agent
        
    def create_agent(self, name: str, description: str = "") -> Agent:
        """
        Create and add a new agent to the workspace.
        
        Args:
            name: Agent name
            description: Agent description
            
        Returns:
            The created agent
        """
        config = AgentConfig(name=name, description=description)
        agent = Agent(config)
        self.add_agent(agent)
        return agent
        
    def get_agent(self, name: str) -> Optional[Agent]:
        """
        Get an agent by name.
        
        Args:
            name: Agent name
            
        Returns:
            The agent if found, None otherwise
        """
        return self.agents.get(name)
        
    def list_agents(self) -> List[str]:
        """
        List all agents in the workspace.
        
        Returns:
            List of agent names
        """
        return list(self.agents.keys())
        
    def execute_task(self, agent_name: str, task: str) -> Dict:
        """
        Execute a task with a specific agent.
        
        Args:
            agent_name: Name of the agent to use
            task: Task description
            
        Returns:
            Task execution result
            
        Raises:
            ValueError: If agent not found
        """
        agent = self.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in workspace")
            
        return agent.execute(task)
        
    def get_status(self) -> Dict:
        """
        Get workspace status.
        
        Returns:
            Dictionary with workspace information
        """
        return {
            "name": self.name,
            "agent_count": len(self.agents),
            "agents": [
                {
                    "name": name,
                    "state": agent.get_state()
                }
                for name, agent in self.agents.items()
            ]
        }
