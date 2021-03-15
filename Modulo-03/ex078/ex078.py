num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite o {c + 1}º valor: ')))
    if c == 0:
        maior = menor = num[0]
    elif num[c] > maior:
        maior = num[c]
    elif num[c] < menor:
        menor = num[c]
print(f'Voce digitou os valores: {num}')
print(f'O maior valor é {maior} na posição', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(i, end=' ')
print(f'\nO menor valor é {menor} na posição', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(i, end=' ')
