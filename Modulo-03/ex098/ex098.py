from time import sleep


def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f, p):
        print(c, end=' -> ')
        sleep(0.3)
    print('Fim')
    print('=' * 50)


contador(1, 11, 1)
contador(10, -1, -2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio > fim:
    passo = passo * -1
contador(inicio, fim + 1, passo)
