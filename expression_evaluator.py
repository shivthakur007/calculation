import ast
import math
import operator

# Operators Mapping

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow
}

ALLOWED_FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "exp": math.exp
}


def evaluate_expression(expression):

    expression = expression.strip()

    if not expression:
        raise ValueError("Expression cannot be empty")

    def _eval(node):

        if isinstance(node, ast.Constant):

            if isinstance(node.value, (int, float)):
                return node.value
            else:
                raise TypeError("Only numeric values allowed")

        elif isinstance(node, ast.BinOp):

            left = _eval(node.left)
            right = _eval(node.right)

            op_type = type(node.op)

            if op_type in OPERATORS:
                try:
                    return OPERATORS[op_type](left, right)
                except ZeroDivisionError:
                    raise ValueError("Division by zero is not allowed")

            else:
                raise TypeError("Operator not supported")

        elif isinstance(node, ast.UnaryOp):

            operand = _eval(node.operand)

            if isinstance(node.op, ast.USub):
                return -operand

            elif isinstance(node.op, ast.UAdd):
                return operand

            else:
                raise TypeError("Unary operator not supported")

        elif isinstance(node, ast.Call):

            if isinstance(node.func, ast.Name):

                func_name = node.func.id

                if func_name in ALLOWED_FUNCTIONS:

                    args = [_eval(arg) for arg in node.args]

                    return ALLOWED_FUNCTIONS[func_name](*args)

                else:
                    raise TypeError("Function not allowed")

            else:
                raise TypeError("Invalid function call")

        else:
            raise TypeError("Unsupported expression")

    try:
        tree = ast.parse(expression, mode="eval")

    except SyntaxError:
        raise ValueError("Invalid mathematical expression")

    return _eval(tree.body)
