"""
Unit tests for AgentOrchestrator
"""

import unittest
from agentic_ai.agent import BaseAgent
from agentic_ai.orchestrator import AgentOrchestrator


class TestAgentOrchestrator(unittest.TestCase):
    """Test cases for AgentOrchestrator"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.orchestrator = AgentOrchestrator()
        self.agent1 = BaseAgent(name="Agent1", role="First agent")
        self.agent2 = BaseAgent(name="Agent2", role="Second agent")
    
    def test_orchestrator_initialization(self):
        """Test orchestrator is initialized correctly"""
        self.assertEqual(len(self.orchestrator.get_agents()), 0)
    
    def test_register_agent(self):
        """Test registering agents"""
        self.orchestrator.register_agent(self.agent1)
        self.assertEqual(len(self.orchestrator.get_agents()), 1)
        self.assertIn("Agent1", self.orchestrator.get_agents())
    
    def test_register_multiple_agents(self):
        """Test registering multiple agents"""
        self.orchestrator.register_agent(self.agent1)
        self.orchestrator.register_agent(self.agent2)
        self.assertEqual(len(self.orchestrator.get_agents()), 2)
    
    def test_unregister_agent(self):
        """Test unregistering agents"""
        self.orchestrator.register_agent(self.agent1)
        self.orchestrator.register_agent(self.agent2)
        
        self.orchestrator.unregister_agent("Agent1")
        self.assertEqual(len(self.orchestrator.get_agents()), 1)
        self.assertNotIn("Agent1", self.orchestrator.get_agents())
    
    def test_execute_task(self):
        """Test executing task with specific agent"""
        self.orchestrator.register_agent(self.agent1)
        result = self.orchestrator.execute_task("Test task", "Agent1")
        
        self.assertIn("status", result)
        self.assertEqual(result["status"], "completed")
    
    def test_execute_task_unknown_agent(self):
        """Test executing task with unknown agent"""
        result = self.orchestrator.execute_task("Test task", "UnknownAgent")
        self.assertFalse(result["success"])
        self.assertIn("error", result)
    
    def test_collaborate(self):
        """Test multi-agent collaboration"""
        self.orchestrator.register_agent(self.agent1)
        self.orchestrator.register_agent(self.agent2)
        
        result = self.orchestrator.collaborate(
            "Collaborative task",
            ["Agent1", "Agent2"]
        )
        
        self.assertIn("individual_results", result)
        self.assertEqual(len(result["individual_results"]), 2)
    
    def test_execution_history(self):
        """Test execution history tracking"""
        self.orchestrator.register_agent(self.agent1)
        self.orchestrator.execute_task("Task 1", "Agent1")
        self.orchestrator.execute_task("Task 2", "Agent1")
        
        history = self.orchestrator.get_history()
        self.assertEqual(len(history), 2)


if __name__ == "__main__":
    unittest.main()
