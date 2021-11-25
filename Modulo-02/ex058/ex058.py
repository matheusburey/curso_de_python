from random import randint
print('=-' * 15)
print('ADIVINHE EM QUE NUMERO ESTOU PENÇANDO')
print('=-' * 15)

pc = randint(0, 10)
num = 11
cont = 0

while pc != num:

    num = int(input('Sera que voce consegue acertar o numero que pensei, entre 0, 10: '))
    if num == pc:
        print('PARABES!!! VOCE ACERTOU')
    else:
        if num < pc:
            print('Mais...', end=' ')
        else:
            print('Menos...', end=' ')
        print('Tente novamente')
        print('-' * 20)
    cont += 1
print(f'Voce tentou {cont} vezes para acertar')
