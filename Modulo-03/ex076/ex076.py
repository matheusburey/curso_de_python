lista = ('Lapis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Trasferidor', '4.20',
         'Comapasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
print('-' * 40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-' * 40)
for c in range(0, 18):
    if c % 2 == 0:
        print('{:.<25}'.format(lista[c]), end=' ')
    else:
        print('R$ {:>6}'.format(lista[c]))
print('-' * 40)
