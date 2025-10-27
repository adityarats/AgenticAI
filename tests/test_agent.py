"""
Unit tests for BaseAgent
"""

import unittest
from agentic_ai.agent import BaseAgent, AgentConfig
from agentic_ai.tools import CalculatorTool


class TestBaseAgent(unittest.TestCase):
    """Test cases for BaseAgent class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = BaseAgent(
            name="TestAgent",
            role="Test agent for unit tests"
        )
    
    def test_agent_initialization(self):
        """Test agent is initialized correctly"""
        self.assertEqual(self.agent.name, "TestAgent")
        self.assertEqual(self.agent.role, "Test agent for unit tests")
        self.assertEqual(len(self.agent.tools), 0)
        self.assertIsNone(self.agent.memory)
    
    def test_agent_with_tools(self):
        """Test agent with tools"""
        tool = CalculatorTool()
        agent = BaseAgent(
            name="ToolAgent",
            role="Agent with tools",
            tools=[tool]
        )
        self.assertEqual(len(agent.tools), 1)
        self.assertEqual(agent.tools[0].name, "Calculator")
    
    def test_agent_execute(self):
        """Test agent task execution"""
        result = self.agent.execute("Test task")
        self.assertIn("status", result)
        self.assertEqual(result["status"], "completed")
        self.assertIn("plan", result)
        self.assertIn("results", result)
    
    def test_agent_planning(self):
        """Test agent planning"""
        plan = self.agent._plan("Test task")
        self.assertIsInstance(plan, list)
        self.assertGreater(len(plan), 0)
    
    def test_agent_get_state(self):
        """Test getting agent state"""
        state = self.agent.get_state()
        self.assertEqual(state["name"], "TestAgent")
        self.assertEqual(state["role"], "Test agent for unit tests")
        self.assertIn("tools", state)
        self.assertIn("conversation_length", state)
    
    def test_agent_reset(self):
        """Test resetting agent"""
        self.agent.execute("Task 1")
        self.assertEqual(len(self.agent.conversation_history), 2)
        self.agent.reset()
        self.assertEqual(len(self.agent.conversation_history), 0)
    
    def test_agent_config(self):
        """Test agent with configuration"""
        config = AgentConfig(
            name="ConfigAgent",
            role="Configured agent",
            model="gpt-4",
            temperature=0.5
        )
        agent = BaseAgent(
            name="ConfigAgent",
            role="Configured agent",
            config=config
        )
        self.assertEqual(agent.config.temperature, 0.5)
        self.assertEqual(agent.config.model, "gpt-4")


if __name__ == "__main__":
    unittest.main()
