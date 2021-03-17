num = []
while True:
    escolha = ' '
    num.append(int(input('Digite um valor: ')))
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]: ')).upper()
    if escolha == 'N':
        break
print(f'Voce digitou {len(num)} valores')
num.sort(reverse=True)
print(f'Os valores em ordem decressente são {num}')
print('O valor 5 faz parte da lista' if 5 in num else 'A lista não contem o valor 5')
