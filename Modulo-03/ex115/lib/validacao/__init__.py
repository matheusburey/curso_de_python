def valida(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[31mErro: digite um numero inteiro entre 1 e 3\033[m')
        else:
            if n < 4:
                print('--' * 20)
                return n
            else:
                print('\033[31mErro: digite um numero inteiro entre 1 e 3\033[m')


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        a = open(nome, 'wt+')
        a.close()
    else:
        return True


def ler_arquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Houve um erro ao abrir arquivo')
    else:
        print(f'{"PESSOAS CADASTRADAS":^40}')
        print(a.readline())
