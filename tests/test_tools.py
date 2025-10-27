"""
Unit tests for Tools
"""

import unittest
from agentic_ai.tools import CalculatorTool, WebSearchTool, ToolConfig


class TestCalculatorTool(unittest.TestCase):
    """Test cases for CalculatorTool"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.tool = CalculatorTool()
    
    def test_tool_initialization(self):
        """Test tool is initialized correctly"""
        self.assertEqual(self.tool.name, "Calculator")
        self.assertTrue(self.tool.config.enabled)
    
    def test_simple_calculation(self):
        """Test simple calculation"""
        result = self.tool.execute("2 + 2")
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 4)
    
    def test_complex_calculation(self):
        """Test complex calculation"""
        result = self.tool.execute("(10 + 5) * 2 - 3")
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 27)
    
    def test_invalid_expression(self):
        """Test invalid expression handling"""
        result = self.tool.execute("invalid expression")
        self.assertFalse(result["success"])
        self.assertIn("error", result)
    
    def test_can_handle(self):
        """Test task matching"""
        self.assertTrue(self.tool.can_handle("calculate 2 + 2"))
        self.assertTrue(self.tool.can_handle("perform math operation"))
        self.assertFalse(self.tool.can_handle("search the web"))


class TestWebSearchTool(unittest.TestCase):
    """Test cases for WebSearchTool"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.tool = WebSearchTool()
    
    def test_tool_initialization(self):
        """Test tool is initialized correctly"""
        self.assertEqual(self.tool.name, "WebSearch")
        self.assertTrue(self.tool.config.enabled)
    
    def test_search_execution(self):
        """Test search execution"""
        result = self.tool.execute("AI agents")
        self.assertTrue(result["success"])
        self.assertIn("results", result)
        self.assertEqual(result["query"], "AI agents")
    
    def test_can_handle(self):
        """Test task matching"""
        self.assertTrue(self.tool.can_handle("search for information"))
        self.assertTrue(self.tool.can_handle("find research papers"))
        self.assertFalse(self.tool.can_handle("calculate the sum"))


class TestToolConfig(unittest.TestCase):
    """Test cases for ToolConfig"""
    
    def test_config_creation(self):
        """Test creating tool configuration"""
        config = ToolConfig(
            name="TestTool",
            description="A test tool",
            enabled=True
        )
        self.assertEqual(config.name, "TestTool")
        self.assertEqual(config.description, "A test tool")
        self.assertTrue(config.enabled)


if __name__ == "__main__":
    unittest.main()
