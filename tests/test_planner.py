"""
Unit tests for TaskPlanner
"""

import unittest
from agentic_ai.planner import TaskPlanner


class TestTaskPlanner(unittest.TestCase):
    """Test cases for TaskPlanner"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.planner = TaskPlanner()
    
    def test_planner_initialization(self):
        """Test planner is initialized correctly"""
        self.assertEqual(len(self.planner.planning_history), 0)
    
    def test_simple_plan(self):
        """Test creating a simple plan"""
        plan = self.planner.plan("Simple task")
        self.assertIsInstance(plan, list)
        self.assertGreater(len(plan), 0)
    
    def test_research_plan(self):
        """Test creating a research plan"""
        plan = self.planner.plan("Research AI developments")
        self.assertIn("Gather relevant information", plan)
        self.assertIn("Analyze findings", plan)
    
    def test_build_plan(self):
        """Test creating a build plan"""
        plan = self.planner.plan("Build a new system")
        self.assertIn("Design solution approach", plan)
        self.assertIn("Implement solution", plan)
    
    def test_test_plan(self):
        """Test creating a test plan"""
        plan = self.planner.plan("Test the application")
        self.assertIn("Execute tests", plan)
        self.assertIn("Validate results", plan)
    
    def test_decompose_simple_task(self):
        """Test decomposing a simple task"""
        result = self.planner.decompose("Simple task")
        self.assertIn("task", result)
        self.assertIn("subtasks", result)
    
    def test_decompose_complex_task(self):
        """Test decomposing a complex task"""
        complex_task = "Research the latest AI developments and create a comprehensive report with analysis"
        result = self.planner.decompose(complex_task, max_depth=2)
        self.assertEqual(result["task"], complex_task)
        self.assertIsInstance(result["subtasks"], list)
    
    def test_planning_history(self):
        """Test planning history tracking"""
        self.planner.plan("Task 1")
        self.planner.plan("Task 2")
        self.planner.plan("Task 3")
        
        history = self.planner.get_history()
        self.assertEqual(len(history), 3)
    
    def test_plan_with_context(self):
        """Test planning with context"""
        context = {"priority": "high", "deadline": "today"}
        plan = self.planner.plan("Urgent task", context)
        
        history = self.planner.get_history(limit=1)
        self.assertEqual(history[0]["context"], context)


if __name__ == "__main__":
    unittest.main()
