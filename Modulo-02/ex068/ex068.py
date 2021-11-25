from random import randint
print('-' * 20)
print('PAR OU IMPAR')
print('-' * 20)
vitoria = 0
while True:
    pess = ' '
    pc = randint(0, 11)
    num = int(input('Digite um valor: '))
    while pess not in 'PI':
        pess = str(input('PAR[P] OU IMPAR [I]: ')).upper()
    total = pc + num
    print(f'Voce escolheu {num} e o computador escolheu {pc} \nO resutado é {total}')
    if pess == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            vitoria += 1
        else:
            print('Voce perdeu!')
            break
    elif pess == 'I':
        if total % 2 == 0:
            print('Voce perdeu')
            break
        else:
            print('Voce veceu!!')
            vitoria += 1
print(f'Voce venceu {vitoria} vezes')
