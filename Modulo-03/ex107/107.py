import moeda

preso = float(input('Digite um preço: '))
print(f'O dobro de {preso} é R$ {moeda.dobro(preso)}')
print(f'A metade de {preso} é R$ {moeda.metade(preso)}')
print(f'Almentando 10% de {preso} é R$ {moeda.almentar(preso, 10)}')
print(f'Desconto de 10% {preso} é R$ {moeda.diminuir(preso, 10)}')
