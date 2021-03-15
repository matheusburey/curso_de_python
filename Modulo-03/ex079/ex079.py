num = list()
while True:
    r = ' '
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado...')
    elif n in num:
        print('Valor duplicado! Não sera adicionado')
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ')).upper()
    if r == 'N':
        break
print('-' * 20)
num.sort()
print(f'Voce digitou os valore {num}')
