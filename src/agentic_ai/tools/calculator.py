"""
Calculator Tool implementation
"""

from typing import Dict, Any, Union
from agentic_ai.tools.base_tool import BaseTool, ToolConfig
import ast
import operator


class CalculatorTool(BaseTool):
    """
    A tool for performing mathematical calculations.
    """
    
    # Supported operators for safe evaluation
    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
    }
    
    def __init__(self):
        config = ToolConfig(
            name="Calculator",
            description="calculate perform mathematical calculations arithmetic math"
        )
        super().__init__(config)
    
    def _safe_eval(self, node) -> Union[int, float, complex]:
        """
        Safely evaluate a mathematical expression AST node.
        
        Args:
            node: AST node to evaluate
            
        Returns:
            Evaluation result (numeric value)
        """
        if isinstance(node, ast.Constant):  # number (Python 3.8+)
            # Only allow numeric constants
            if not isinstance(node.value, (int, float, complex)):
                raise ValueError(f"Only numeric constants are allowed, got {type(node.value).__name__}")
            return node.value
        elif isinstance(node, ast.BinOp):  # binary operation
            op = self.OPERATORS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op)}")
            left = self._safe_eval(node.left)
            right = self._safe_eval(node.right)
            
            # Check for division by zero (with small epsilon for floating point)
            if isinstance(node.op, ast.Div) and abs(right) < 1e-10:
                raise ZeroDivisionError("Division by zero is not allowed")
            
            return op(left, right)
        elif isinstance(node, ast.UnaryOp):  # unary operation
            op = self.OPERATORS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op)}")
            operand = self._safe_eval(node.operand)
            return op(operand)
        else:
            raise ValueError(f"Unsupported node type: {type(node)}")
    
    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Execute a mathematical calculation.
        
        Args:
            input_data: Mathematical expression as string
            
        Returns:
            Dictionary with calculation result
        """
        try:
            expression = str(input_data).strip()
            
            # Parse the expression into an AST
            tree = ast.parse(expression, mode='eval')
            
            # Safely evaluate the expression
            result = self._safe_eval(tree.body)
            
            return {
                "success": True,
                "expression": expression,
                "result": result
            }
        except SyntaxError:
            return {
                "success": False,
                "error": "Invalid mathematical expression syntax"
            }
        except ZeroDivisionError as e:
            return {
                "success": False,
                "error": str(e)
            }
        except ValueError as e:
            return {
                "success": False,
                "error": str(e)
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Calculation error: {str(e)}"
            }

