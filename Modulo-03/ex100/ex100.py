from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista:')
    for c in range(0, 5):
        num = randint(0, 20)
        lista.append(num)
        print(num, end=" ")
        sleep(0.3)
    print('Pronto!!')
def somaPar(lista):
    soma = 0
    par = list()
    for n in lista:
        if n % 2 ==0:
            soma += n
            par.append(n)
    print(f'A soma dos valores pares {par} é {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

