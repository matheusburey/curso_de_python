maior = homen = mulheres = 0

while True:
    print('-' * 20)
    print('CADASTRO DE PESSOA')
    print('-' * 20)
    sexo = opcao = ' '
    idade = int(input('Qual sua idade: '))

    while sexo not in 'FM':
        sexo = str(input('Qual seu sexo [M/F]: ')).upper()
    if idade > 18:
        maior += 1
    if sexo == 'F' and idade < 21:
        mulheres += 1
    elif sexo == 'M':
        homen += 1
    print('-' * 20)

    while opcao not in 'SN':
        opcao = str(input('Deseja continuar[S/N]: ')).upper()
    if opcao == 'N':
        break

print(f'Foram cadastrados {maior} pesssoas maiores de 18 anos.')
print(f'Foram cadastrados {homen} homens.')
print(f'Foram cadastradas {mulheres} mulheres com menos de 21 anos')
