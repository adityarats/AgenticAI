"""
Task Planner for breaking down complex tasks
"""

from typing import List, Dict, Any


class TaskPlanner:
    """
    Planner for breaking down complex tasks into executable steps.
    """
    
    def __init__(self):
        """Initialize the planner"""
        self.planning_history: List[Dict[str, Any]] = []
    
    def plan(self, task: str, context: Dict[str, Any] = None) -> List[str]:
        """
        Create a plan for executing a task.
        
        Args:
            task: Task description
            context: Additional context for planning
            
        Returns:
            List of steps to execute
        """
        # Simple rule-based planning
        steps = []
        
        # Analyze the task
        steps.append(f"Analyze requirements: {task}")
        
        # Identify key components
        if "research" in task.lower():
            steps.append("Gather relevant information")
            steps.append("Analyze findings")
        
        if "create" in task.lower() or "build" in task.lower():
            steps.append("Design solution approach")
            steps.append("Implement solution")
        
        if "test" in task.lower():
            steps.append("Execute tests")
            steps.append("Validate results")
        
        # Always add completion step
        steps.append("Complete task and summarize results")
        
        # Record planning
        self.planning_history.append({
            "task": task,
            "steps": steps,
            "context": context
        })
        
        return steps
    
    def decompose(self, task: str, max_depth: int = 3) -> Dict[str, Any]:
        """
        Recursively decompose a task into subtasks.
        
        Args:
            task: Task to decompose
            max_depth: Maximum decomposition depth
            
        Returns:
            Task decomposition tree
        """
        if max_depth == 0:
            return {"task": task, "subtasks": []}
        
        # Simple decomposition based on keywords
        subtasks = []
        
        if len(task.split()) > 10:  # Complex task
            words = task.split()
            mid = len(words) // 2
            subtasks.append(" ".join(words[:mid]))
            subtasks.append(" ".join(words[mid:]))
        
        return {
            "task": task,
            "subtasks": [
                self.decompose(subtask, max_depth - 1) 
                for subtask in subtasks
            ] if subtasks else []
        }
    
    def get_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get planning history.
        
        Args:
            limit: Maximum number of entries
            
        Returns:
            Recent planning history
        """
        return self.planning_history[-limit:]
