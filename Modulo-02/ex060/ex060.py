print('FATORIAL COM WHILE')
num = int(input('Digite um numero: '))
total = 1
print(f'Fatorial de {num}! =', end=' ')
while num > 0:
    if num == 1:
        print(f'{num} = {total}')
        num -= 1
    else:
        print(num, end=' x ')
        total *= num
        num -=1
print('-' * 60)


print('FATORIAL COM FOR')
num = int(input('Digite um valor: '))
print(f'Fatorial {num}! = ', end='')
total = 1
for c in range(num ,0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    total *= c
print(total)
