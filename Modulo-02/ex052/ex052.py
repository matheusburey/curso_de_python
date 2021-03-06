print('-' * 15)
print('Numeros primos')
print('-' * 15)
n = int(input('Digite um numero: '))
con = a = 0
cor = ('\033[32m','\033[31m' )

for c in range(1, n + 1):
    if n % c == 0:
        con += 1
        a = 0
    else:
        a = 1
    print(f'{cor[a]}{c}\033[m', end=' ')

print(f'\nO numero {n} foi dividido {con} vezes')
if con == 2:
    print(f'O numero {n} É PRIMO')
else:
    print(f'O numero {n} NÃO É PRIMO')
