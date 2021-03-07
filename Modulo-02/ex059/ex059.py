print('=-' * 15)
print('CALCULADORA')
print('=-' * 15)
opcao = 0

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

while not opcao == 5:
    print('-' * 30)
    print('''Qual operação voce deseja realizar:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Sua escloha: '))

    if opcao == 1:
        print(f'Soma: {num1} + {num2} = {num2 + num1}')
    elif opcao == 2:
        print(f'Multiplicaçao: {num1} x {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 < num2:
            maior = num2
            menor = num1
        else:
            maior = num1
            menor = num2
        print(f'O valor {maior} é maior que {menor}')
    elif opcao == 4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
    elif opcao == 5:
        print('Volte sempre!!!')
    else:
        print('Comando invalido, digite novamente')
