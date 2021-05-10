def almentar(preco, taxa, formato=False):
    res = preco + preco * taxa / 100
    return res if not formato else moeda(preco)


def diminuir(preco, taxa, formato=False):
    res = preco - preco * taxa / 100
    return res if not formato else moeda(preco)


def dobro(preco, formato=False):
    res = preco * 2
    return res if not formato else moeda(preco)


def metade(preco, formato=False):
    res = preco / 2
    return res if not formato else moeda(preco)


def moeda(preco):
    return f'R$ {preco:.2f}'.replace('.', ',')
