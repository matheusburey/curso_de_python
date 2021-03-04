from datetime import date
print('-' * 40)
print('ALISTAMENTO DO EXERCITO BRASILEIRO')
print('-' * 40)
ano = int(input('Que ano você nasceu: '))
atual = date.today().year
idade = atual - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if idade < 18:
   
    print(f'Faltam {saldo} para voce se apresentar no exercito')
    print(f'Seu alistameno sera no ano {atual + saldo}')
elif idade == 18:
    print('voce tem que se apresentar')
else:
    saldo = idade - 18
    print(f'Voce esta atrasou {saldo} anos para se apreentar')
    print(f'Voce deveria ter se alistado no ano {atual - saldo}')
