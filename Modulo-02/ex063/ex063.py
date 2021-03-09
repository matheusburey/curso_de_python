print('=' * 22)
print('SEQUENCIA DE FIBONACCI')
print('=' * 22)
termo = int(input('Quantos termos voce deseja mostrar?? '))
valor1 = 0
valor2 = 1

while termo > 0:
    print(valor1, end=' -> ')
    res = valor1 + valor2
    valor1 = valor2
    valor2 = res
    termo -= 1
print('FIM!')
