from datetime import date
print('-' * 10)
print('ALISTAMENTO DO EXERCITO BRASILEIRO')
print('-' * 10)
ano = int(input('Que ano você nasceu: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print(f'Faltam {18 - idade} para voce se apresentar no exercito')
elif idade == 18:
    print('voce tem que se apresentar')
else:
    print(f'Voce esta atrasou {idade - 18} anos para se apreentar')
