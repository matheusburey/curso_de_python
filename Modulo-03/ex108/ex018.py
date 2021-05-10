import moeda

preco = float(input('Digite um preço:R$ '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Almentando 10% de {moeda.moeda(preco)} é {moeda.moeda(moeda.almentar(preco, 10))}')
print(f'Desconto de 10% {moeda.moeda(preco)} é {moeda.moeda(moeda.diminuir(preco, 10))}')
