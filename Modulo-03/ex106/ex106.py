from time import sleep
def formatado(msg, color=0):
    """
    -> Printa linha formatada
    :param msg: Frase que seseja mostrar
    :param color: Cor 0=verde 1=azul 2=vermelho
    :return: sem retorno
    """
    if color == 0:
        m = len(msg) + 4
        print(f"\033[42m{'='* m}")
        print(f'  {msg}')
        print(f"{'=' * m}")
    elif color == 1:
        m = len(msg) + 4
        print(f"\033[44m{'='* m}")
        print(f'  {msg}')
        print(f"{'=' * m}")
    elif color == 2:
        m = len(msg) + 4
        print(f"\033[41m{'='* m}")
        print(f'  {msg}')
        print(f"{'=' * m}")
def pyhelp(msg):
    while True:
        formatado('SISTEMA DE AJUDA PyHELP',color=0)
        sleep(0.3)
        fun = str(input(msg))
        sleep(0.3)
        if fun == 'fim':
            formatado('ate logo', color=2)
            break
        formatado(f"Acessando o manual do comando {fun}",color=1)
        sleep(0.3)
        print('\033[47m ')
        help(fun)
        sleep(0.3)


pyhelp("\033[mFunção ou biblioteca: ")
