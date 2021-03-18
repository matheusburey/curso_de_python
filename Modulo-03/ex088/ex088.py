from random import randint
from  time import sleep
jogos = []
tempo = []
print('-'* 30)
print(f'{"JOGOS DA MEGA SENA":^30}')
print('-'* 30)
while True:
    num = int(input('Quantos jogos: '))
    for j in range(0, num):
        cont = 0
        while True:
            num = randint(0, 60)
            if num not in tempo:
                tempo.append(num)
                cont += 1
            if cont == 6:
                break
        tempo.sort()
        jogos.append(tempo[:])
        tempo.clear()
    print('-' * 30)
    for c, l in enumerate(jogos):
        print(f'Jogo {c+1}: {l}')
        sleep(0.5)
    print('-' * 30)
    jogos.clear()
    escolha = str(input('Deseja continuar [S/N]:')).upper()
    if escolha == 'N':
        break
