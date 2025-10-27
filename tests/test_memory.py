"""
Unit tests for Memory
"""

import unittest
from agentic_ai.memory import Memory


class TestMemory(unittest.TestCase):
    """Test cases for Memory class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.memory = Memory(max_size=10)
    
    def test_memory_initialization(self):
        """Test memory is initialized correctly"""
        self.assertEqual(self.memory.max_size, 10)
        self.assertEqual(self.memory.size(), 0)
    
    def test_add_memory(self):
        """Test adding memories"""
        self.memory.add("First memory")
        self.assertEqual(self.memory.size(), 1)
        
        self.memory.add("Second memory")
        self.assertEqual(self.memory.size(), 2)
    
    def test_add_memory_with_metadata(self):
        """Test adding memory with metadata"""
        self.memory.add("Memory with metadata", {"tag": "test"})
        memories = self.memory.get_recent(1)
        self.assertEqual(memories[0]["metadata"]["tag"], "test")
    
    def test_memory_limit(self):
        """Test memory size limit"""
        for i in range(15):
            self.memory.add(f"Memory {i}")
        
        # Should only keep last 10
        self.assertEqual(self.memory.size(), 10)
    
    def test_search_memory(self):
        """Test searching memories"""
        self.memory.add("Python programming")
        self.memory.add("JavaScript coding")
        self.memory.add("Python development")
        
        results = self.memory.search("Python")
        self.assertEqual(len(results), 2)
    
    def test_get_recent(self):
        """Test getting recent memories"""
        for i in range(5):
            self.memory.add(f"Memory {i}")
        
        recent = self.memory.get_recent(3)
        self.assertEqual(len(recent), 3)
        # Most recent should be last
        self.assertIn("Memory 4", recent[-1]["content"])
    
    def test_clear_memory(self):
        """Test clearing memories"""
        self.memory.add("Memory 1")
        self.memory.add("Memory 2")
        self.assertEqual(self.memory.size(), 2)
        
        self.memory.clear()
        self.assertEqual(self.memory.size(), 0)
    
    def test_search_with_limit(self):
        """Test search with result limit"""
        for i in range(10):
            self.memory.add(f"Test memory {i}")
        
        results = self.memory.search("Test", limit=3)
        self.assertEqual(len(results), 3)


if __name__ == "__main__":
    unittest.main()
