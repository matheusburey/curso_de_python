maior = menor = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = menor = peso
    elif maior < peso:
        maior = peso
    elif menor > peso:
        menor = peso
print(f'O maior peso lido é {maior}Kg')
print(f'O menor peso lido é {menor}Kg')
