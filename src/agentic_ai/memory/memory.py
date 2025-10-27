"""
Memory system for agents
"""

from typing import List, Dict, Any, Optional
from datetime import datetime


class Memory:
    """
    Memory system for storing and retrieving agent experiences.
    """
    
    def __init__(self, max_size: int = 1000):
        """
        Initialize memory system.
        
        Args:
            max_size: Maximum number of memories to store
        """
        self.max_size = max_size
        self.memories: List[Dict[str, Any]] = []
    
    def add(self, content: str, metadata: Optional[Dict[str, Any]] = None):
        """
        Add a new memory.
        
        Args:
            content: Memory content
            metadata: Additional metadata
        """
        memory = {
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self.memories.append(memory)
        
        # Keep memory size under limit
        if len(self.memories) > self.max_size:
            self.memories.pop(0)
    
    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search memories by query.
        
        Args:
            query: Search query
            limit: Maximum number of results
            
        Returns:
            List of matching memories
        """
        # Simple keyword-based search
        query_lower = query.lower()
        matches = []
        
        for memory in reversed(self.memories):
            if query_lower in memory["content"].lower():
                matches.append(memory)
                if len(matches) >= limit:
                    break
        
        return matches
    
    def get_recent(self, count: int = 10) -> List[Dict[str, Any]]:
        """
        Get the most recent memories.
        
        Args:
            count: Number of memories to retrieve
            
        Returns:
            List of recent memories
        """
        return self.memories[-count:]
    
    def clear(self):
        """Clear all memories"""
        self.memories = []
    
    def size(self) -> int:
        """Get the number of stored memories"""
        return len(self.memories)
