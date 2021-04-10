def ficha(nome="<desconhecido>", gols=0):
    """
    Retorna uma ficha com o nome do jogador e os seus gols.
    :param nome: Nome do jogador.
    :param gols: Gols realizados pelo jogador.
    :return: sem retorno.
    """
    print(f'O jogador {nome} fez {gols} gols')


n = str(input('Nome jogador: '))
g = str(input('Numeros de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
