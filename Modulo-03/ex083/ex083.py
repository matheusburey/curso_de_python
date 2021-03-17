exp = str(input('Digite uma expressão: '))
pilha = []
for v in exp:
    if v == '(':
        pilha.append('(')
    elif v == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('A expressão é valida' if len(pilha) == 0 else 'O expressão não é valida')
