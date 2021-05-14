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
        for lista in a:
            pessoa = lista.split(';')
            pessoa[1] = pessoa[1].replace('\n', '')
            print(f'  {pessoa[0]:<15}{pessoa[1]}')
        a.close()


def add_pessoa(arq):
    try:
        a = open(arq, 'at')
        nome: str = (input('Nome: '))
        idade = int(input('Idade: '))
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print('\033[32mPessoa registrada com sucesso\033[m')
