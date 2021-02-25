from random import randint
pc = randint(0,5)

print('-=' * 15)
print('ESTOU PENSANDO EM UM NUMERO')
print('-=' * 15)
player = int(input('ADIVINHE QUAL É DE 0 A 5: '))

if pc == player:
    print('PARABENS VOCCE ACERTOU!!!!')
else:
    print(f'GANHEI!! estava pensando em {pc}')
