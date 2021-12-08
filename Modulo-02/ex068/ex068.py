from random import randint

print('-' * 20)
print('PAR OU IMPAR')
print('-' * 20)

vitoria = 0

while True:
    pc = randint(0, 11)
    num = int(input('Digite um valor: '))
    pess = str(input('PAR[P] OU IMPAR [I]: '))[0].upper()
    total = pc + num

    print(f'Voce escolheu {num} e o computador escolheu {pc} \nO resutado é {total}')

    if pess == 'P' and total % 2 ==0:
        print('Voce venceu!')
        vitoria += 1
    if pess == 'I' and total % 2 !=0:
        print('Voce venceu!')
        vitoria += 1
    else :
        print('Voce perdeu')
        break

print(f'Voce venceu {vitoria} vezes')
