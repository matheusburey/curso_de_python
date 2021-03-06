frase = str(input('Digite uma frase: ')).strip().split()
junto = ''.join(frase).upper()
inverso = ''
for l in range(len(junto) -1, -1, -1):
    inverso += junto[l]
print(f'A frase {junto}')
print(f'Ivertida e {inverso}')
if inverso == junto:
    print(f'A frase digitada é um palindromo')
else:
    print('A frase não e um palindromo')
