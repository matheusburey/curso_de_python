num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print(f'O valor {num} convertido para BINARIO é {bin(num)[2:]}')
elif escolha == 2:
    print(f'O numero {num} convertido para OCTAL é {oct(num)[2:]}')
elif escolha == 3:
    print(f'O numero {num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção invalida')
