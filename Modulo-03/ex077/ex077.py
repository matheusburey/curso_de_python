lista = ('APRENDER', 'PROGRAMA', 'LINGUAGES', 'PYTHON', 'CURSO',
           'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCAADO',
           'PROGRAMADOR', 'FUTURO')
for palavras in lista:
    print(f'\nNa palavra {palavras} temos: ', end='')
    for vogais in palavras:
        if vogais in 'AEIOU':
            print(vogais, end=' ')



