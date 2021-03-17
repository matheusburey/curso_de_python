num = []
impar = []
par = []
while True:
    escolha = ' '

    n = int(input('Digite um numero: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]: ')).upper()
    if escolha in 'Nn':
        break

print(f'Os valores digitados foram {num}')
print(f'Os valores pares sao {par}')
print(f'Os valores impares sao {impar}')
