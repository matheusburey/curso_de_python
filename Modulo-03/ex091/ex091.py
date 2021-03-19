from random import randint
from time import sleep
from operator import itemgetter
jogo = {'1': randint(1, 6), '2': randint(1, 6), '3': randint(1, 6), '4': randint(1, 6)}
ranking = []
print('Valores sorteados')
for c, l in jogo.items():
    print(f'jogadores {c} tirou {l}')
    sleep(0.4)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-' * 20)
print('RAMKING DOS JOGADORES')
for li in ranking:
    print(f'jogadores {li[0]} tirou {li[1]}')
    sleep(0.4)
