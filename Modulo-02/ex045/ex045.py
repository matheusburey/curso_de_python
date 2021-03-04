from random import randint
print('=-' * 15)
print('\033[1;31mPEDRA, PAPEL E TESOURA\033[m')
print('=-' * 15)

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')

print('''SUAS OPÇOES:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

player = int(input('Qual é sua escolha: '))
pc = randint(0,2)

print('-' * 15)
print(f'O computador escolheu {opcoes[pc]}')
print(f'Voce escolheu {opcoes[player-1]}')
print('-' * 15)

if player == 1:
    if pc == 0:
        print('EMPATOU')
    elif pc == 1:
        print('O COMPUTADOR GANHOU')
    else:
        print('VOCE GANHOU')
elif player == 2:
    if pc == 0:
        print('VOCE GANHOU')
    elif pc == 1:
        print('EMPATOU')
    else:
        print('O COMPUTADOR GANHOU')
elif player == 3:
    if pc == 0:
        print('O COMPUTADOR GANHOU')
    elif pc == 1:
        print('VOCE GANHOU')
    else:
        print('EMPATOU')
else:
    print('\033[1;31mJogada invalida tente novamente')
