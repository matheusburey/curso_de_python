from datetime import date
ano = date.today().year
nasc = int(input('Que ano voce nasceu: '))
idade = ano - nasc
print(f'Voce tem {idade} anos sua categoria é:', end = ' ')

if idade <= 9:
    print('MIRIN')
elif idade <= 14:
    print('INFANTOJUVENIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
