def expression_is_valid(expression):
    """Checks whether an expression is correct"""

    opposite = {"}": "{", "]": "[", ")": "("}
    stack = []

    for v in expression:
        if v in ["{", "[", "("]:
            stack.append(v)
        else:
            if opposite.get(v) == stack[-1]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


exp = str(input("Digite uma expressão: "))
valid = expression_is_valid(exp)
print("A expressão é valida" if valid else "O expressão não é valida")
