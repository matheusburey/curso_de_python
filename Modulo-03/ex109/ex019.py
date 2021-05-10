import moeda

preco = float(input('Digite um preço:R$ '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'Almentando 10% de {moeda.moeda(preco)} é {moeda.almentar(preco, 10, True)}')
print(f'Desconto de 10% {moeda.moeda(preco)} é {moeda.diminuir(preco, 10, True)}')
