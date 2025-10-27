"""
Calculator Tool implementation
"""

from typing import Dict, Any
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
    
    def _safe_eval(self, node):
        """
        Safely evaluate a mathematical expression AST node.
        
        Args:
            node: AST node to evaluate
            
        Returns:
            Evaluation result
        """
        if isinstance(node, ast.Constant):  # number (Python 3.8+)
            return node.value
        elif isinstance(node, ast.BinOp):  # binary operation
            op = self.OPERATORS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op)}")
            left = self._safe_eval(node.left)
            right = self._safe_eval(node.right)
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

