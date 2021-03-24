def area(a, b):
    soma = a * b
    print(f'A area de um terreno {a} X {b} é de {soma}')


print('Controle de terreno')
print(f'-' * 20)
largura = float(input('Digite a largura (m): '))
altura = float(input('Digite a largua (m): '))
area(largura, altura)
