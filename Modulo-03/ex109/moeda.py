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
