"""
Calculator Tool implementation
"""

from typing import Dict, Any
from agentic_ai.tools.base_tool import BaseTool, ToolConfig
import re


class CalculatorTool(BaseTool):
    """
    A tool for performing mathematical calculations.
    """
    
    def __init__(self):
        config = ToolConfig(
            name="Calculator",
            description="calculate perform mathematical calculations arithmetic math"
        )
        super().__init__(config)
    
    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Execute a mathematical calculation.
        
        Args:
            input_data: Mathematical expression as string
            
        Returns:
            Dictionary with calculation result
        """
        try:
            # Extract numbers and operators
            expression = str(input_data)
            
            # Basic safety: only allow numbers, operators, and parentheses
            if not re.match(r'^[\d\s\+\-\*/\(\)\.]+$', expression):
                return {
                    "success": False,
                    "error": "Invalid expression. Only numbers and basic operators allowed."
                }
            
            # Evaluate the expression
            result = eval(expression)
            
            return {
                "success": True,
                "expression": expression,
                "result": result
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
