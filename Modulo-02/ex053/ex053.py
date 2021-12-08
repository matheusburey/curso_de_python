frase = str(input('Digite uma frase: ')).strip().split()
junto = ''.join(frase).upper()
inverso = junto[::-1]

print(f'A frase {junto}')
print(f'Ivertida e {inverso}')

if inverso == junto:
    print(f'A frase digitada é um palindromo')
else:
    print('A frase não e um palindromo')
