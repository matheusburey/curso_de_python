print('CALCULADORA DE MEDIA')
n1 = float(input('Digite a prieira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua media foi {media}')
if media < 5:
    print('\033[31mREPROVADO')
elif 5 < media < 7:
    print('\033[33mRECUPERAÇÃO')
else:
    print('\033[32mAPROVADO')
