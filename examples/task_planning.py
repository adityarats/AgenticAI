"""
Task Planning Example

This example demonstrates the task planning capabilities.
"""

from agentic_ai.planner import TaskPlanner


def main():
    print("=== Task Planning Example ===\n")
    
    # Create a planner
    planner = TaskPlanner()
    
    # Plan a simple task
    print("Planning Task 1: Research AI developments")
    task1 = "Research the latest developments in artificial intelligence"
    plan1 = planner.plan(task1)
    print(f"Plan steps:")
    for i, step in enumerate(plan1, 1):
        print(f"  {i}. {step}")
    print()
    
    # Plan a complex task
    print("Planning Task 2: Build and test a system")
    task2 = "Create a new machine learning model and test its performance"
    plan2 = planner.plan(task2)
    print(f"Plan steps:")
    for i, step in enumerate(plan2, 1):
        print(f"  {i}. {step}")
    print()
    
    # Decompose a complex task
    print("Decomposing Task 3:")
    task3 = "Develop a comprehensive AI system that can process natural language and generate insights"
    decomposition = planner.decompose(task3, max_depth=2)
    print(f"Task decomposition:")
    print(f"  Main task: {decomposition['task']}")
    if decomposition['subtasks']:
        print(f"  Subtasks:")
        for subtask in decomposition['subtasks']:
            print(f"    - {subtask['task']}")
    print()
    
    # View planning history
    history = planner.get_history()
    print(f"Planning history: {len(history)} tasks planned")


if __name__ == "__main__":
    main()
