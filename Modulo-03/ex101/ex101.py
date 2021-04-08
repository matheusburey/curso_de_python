from datetime import date


def voto(ano):
    data = date.today().year
    idade = data - ano
    print(f'Voce tem {idade} e ',end='')
    if idade < 16:
        print('não pode votar')
    elif idade < 18 or idade > 65:
        print('seu voto é opiciopnal!!')
    else:
        print('voce é o brigado a votar')


ano = int(input('Em que ano voce nasceu: '))
voto(ano)