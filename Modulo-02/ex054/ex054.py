from datetime import date
ano = date.today().year
maior = menor = 0
for c in range(1, 8):
    nasci = int(input(f'Digite o ano que a {c}ª pessoa nasceu: '))
    if ano - nasci < 21:
        menor += 1
    else:
        maior += 1
print(f'Foram registradas {maior} maiores de idade e {menor} menor de idade')
