"""
Base Tool class for AgenticAI
"""

from abc import ABC, abstractmethod
from typing import Dict, Any
from pydantic import BaseModel


class ToolConfig(BaseModel):
    """Configuration for a tool"""
    name: str
    description: str
    enabled: bool = True


class BaseTool(ABC):
    """
    Base class for all tools that agents can use.
    
    Tools provide specific capabilities to agents, such as:
    - Web search
    - Code execution
    - File operations
    - API calls
    - Calculations
    """
    
    def __init__(self, config: ToolConfig):
        """
        Initialize the tool.
        
        Args:
            config: Tool configuration
        """
        self.config = config
        self.name = config.name
        self.description = config.description
    
    @abstractmethod
    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Execute the tool's functionality.
        
        Args:
            input_data: Input for the tool
            
        Returns:
            Dictionary containing execution results
        """
        pass
    
    def can_handle(self, task: str) -> bool:
        """
        Check if this tool can handle the given task.
        
        Args:
            task: Task description
            
        Returns:
            True if the tool can handle this task
        """
        # Simple keyword matching - can be overridden
        keywords = self.description.lower().split()
        task_lower = task.lower()
        return any(keyword in task_lower for keyword in keywords)
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate the input data.
        
        Args:
            input_data: Input to validate
            
        Returns:
            True if input is valid
        """
        return True
    
    def get_info(self) -> Dict[str, str]:
        """
        Get information about this tool.
        
        Returns:
            Dictionary with tool information
        """
        return {
            "name": self.name,
            "description": self.description,
            "enabled": str(self.config.enabled)
        }
