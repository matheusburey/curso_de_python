from random import randint

print('=-' * 15)
print('\033[1;31m PEDRA, PAPEL E TESOURA \033[m')
print('=-' * 15)

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')

while True:
    player =  int(input('''SUAS OPÇOES:
    [ 1 ] PEDRA.
    [ 2 ] PAPEL.
    [ 3 ] TESOURA.
    [ 0 ] PARAR.
    \nQual é sua escolha: '''))
    pc = randint(0,2)
    text =('\033[1;33m EMPATOU \033[m')

    if player == 0:
        break
    if player == 1:             #player jogou pedra
        if pc == 1:
            text =('\033[1;31m O COMPUTADOR GANHOU \033[m')
        if pc == 2:
            text =('\033[1;32m VOCE GANHOU \033[m')
    if player == 2:           #player jogou papel
        if pc == 0:
            text =('\033[1;32m VOCE GANHOU \033[m')
        if pc == 2:
            text =('\033[1;31m O COMPUTADOR GANHOU \033[m')
    if player == 3:           #player jogou tesoura
        if pc == 0:
            text =('\033[1;31m O COMPUTADOR GANHOU \033[m')
        if pc == 1:
            text =('\033[1;32m VOCE GANHOU \033[m')

    print('-' * 15)
    print(f'Voce escolheu \033[36m {opcoes[player-1]} \033[m')
    print(f'O computador escolheu \033[36m {opcoes[pc]} \033[m')
    print('-' * 15)
    print(text)
    print('=-' * 15)

