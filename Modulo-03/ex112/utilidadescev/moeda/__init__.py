def almentar(preco, taxa, formato=False):
    res = preco + preco * taxa / 100
    return res if not formato else moeda(res)


def diminuir(preco, taxa, formato=False):
    res = preco - preco * taxa / 100
    return res if not formato else moeda(res)


def dobro(preco, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco):
    return f'R$ {preco:.2f}'.replace('.', ',')

def resumo(preco, taxadim, taxaalm):
    print('-' * 35)
    print(f"{'RESUMO DO VALOR':^35}")
    print('-' * 35)
    print(f'Preço analizao: \t{moeda(preco)}')
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'A metade do preço: \t{metade(preco, True)}')
    print(f'{taxaalm}% de almentando: \t{almentar(preco, taxaalm, True)}')
    print(f'{taxadim}% de desconto: \t{diminuir(preco, taxadim, True)}')
    print('-' * 35)
