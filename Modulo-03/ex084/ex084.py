cont = mais = menos = 0
pessoas = list()
cadastro = list()
print('-' * 20)
print(f'{"CADASTRO DE PESSOAS":^20}')
print('-' * 20)
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    cadastro.append(pessoas[:])
    if cont == 0:
        maior = menor = pessoas[1]
    elif pessoas[1] > maior:
        maior = pessoas[1]
    elif pessoas[1] < menor:
        menor = pessoas[1]
    cont += 1
    pessoas.clear()
    escolha = str(input('Deseja continuar?[S/N] ')).upper()
    if escolha == 'N':
        break
print('-' * 20)
print(f'Voce cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior} de ', end='')
for peso in cadastro:
    if peso[1] == maior:
        print(peso[0],end='')
print(f'O menor peso foi de {menor} de ', end='')
for peso in cadastro:
    if peso[1] == menor:
        print(peso[0],end='')
