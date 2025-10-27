"""
Custom Tool Example

This example shows how to create and use custom tools.
"""

from typing import Dict, Any
from agentic_ai.agent import BaseAgent
from agentic_ai.tools import BaseTool, ToolConfig


class TextAnalyzerTool(BaseTool):
    """
    Custom tool for analyzing text.
    """
    
    def __init__(self):
        config = ToolConfig(
            name="TextAnalyzer",
            description="analyze text count words characters"
        )
        super().__init__(config)
    
    def execute(self, input_data: Any) -> Dict[str, Any]:
        """Analyze text and return statistics"""
        text = str(input_data)
        
        return {
            "success": True,
            "text": text,
            "character_count": len(text),
            "word_count": len(text.split()),
            "line_count": len(text.split('\n'))
        }


def main():
    print("=== Custom Tool Example ===\n")
    
    # Create custom tool
    text_tool = TextAnalyzerTool()
    print(f"Created custom tool: {text_tool.name}")
    print(f"Description: {text_tool.description}\n")
    
    # Test the tool directly
    sample_text = "This is a sample text for analysis. It has multiple sentences."
    result = text_tool.execute(sample_text)
    print(f"Direct tool execution:")
    print(f"Text: {result['text']}")
    print(f"Characters: {result['character_count']}")
    print(f"Words: {result['word_count']}")
    print(f"Lines: {result['line_count']}\n")
    
    # Use the tool with an agent
    agent = BaseAgent(
        name="TextAnalyst",
        role="Analyze text content",
        tools=[text_tool]
    )
    
    print(f"Created agent with custom tool")
    task_result = agent.execute("Analyze this text content for statistics")
    print(f"Agent execution result: {task_result}")


if __name__ == "__main__":
    main()
