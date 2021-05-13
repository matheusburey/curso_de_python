def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um numero inteiro valido.\033[m')
            continue
        else:
            return n


def leiaflo(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um numero real valido.\033[m')
            continue
        else:
            return f


numero = leiaint('Digite um numero inteiro: ')
real = leiaflo('Digite um valor real: ')
print(f'O valor inteiro digitado foi {numero} e o valor real foi {real}')
