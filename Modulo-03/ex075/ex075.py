n = (int(input('Dgite um numero: ')),
     int(input('Dgite outro numero: ')),
     int(input('Dgite outro numero: ')),
     int(input('Dgite outro numero: ')))
print(f'O valor 9 apareu {n.count(9)} vezes' if 9 in n else 'O numero 9 não foi digitado')
print(f'O valor 3 foi digitado na posição {n.index(3) + 1}' if 3 in n else 'O numero 3 não foi digitado')
print('Os valores pares digitados foram', end=' ')
for num in n:
    if num % 2 == 0:
        print(num,  end=' ')
