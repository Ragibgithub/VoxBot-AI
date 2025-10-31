def apply_operation(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

def calculate_expression(expression):
    # Remove white spaces from the expression
    expression = expression.replace(' ', '')

    # Operator precedence (BODMAS)
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1}

    operators = []
    operands = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '.':
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            operands.append(float(expression[i:j]))
            i = j
        elif expression[i] in precedence:
            while (operators and precedence[operators[-1]] >= precedence[expression[i]]):
                b = operands.pop()
                a = operands.pop()
                op = operators.pop()
                operands.append(apply_operation(op, a, b))
            operators.append(expression[i])
            i += 1
        else:
            i += 1

    while operators:
        b = operands.pop()
        a = operands.pop()
        op = operators.pop()
        operands.append(apply_operation(op, a, b))

    return operands[0] if operands else None

def calculate(text):
    expression = text
    result = calculate_expression(expression)
    return result

