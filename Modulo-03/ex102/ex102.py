def fatorial(n, show=False):
    """
    Função para mostrar o fotorial de um numero.
    :param n: Valor a ser calculado.
    :param show: Mostrar a conta.
    :return: O valor de um vatorial de um numero n.
    """
    total = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ' if c > 1 else f'{c} = ',end='')
        total *= c
    print(total)
    return total


fatorial(5, show=True)
