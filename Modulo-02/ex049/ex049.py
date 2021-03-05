print('-' * 20)
print('TABUADA')
print('-' * 20)
n = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
