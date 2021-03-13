num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezpito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um numero de 0 a 20: '))
    if 0 <= n < 21:
        break
    print('Comando invalido, tente novamente', end=' ')

print(f'O numer digitado por extenso é {num[n]}')
