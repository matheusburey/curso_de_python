a = float(input('Digite o valor do primeiro segmento: '))
b = float(input('Digite o valor do segundo sgmeno: '))
c = float(input('Digite o valor do terceiro segmento: '))
if a < b + c and b < c + a and c < b + a:
    print('Os valores digitados podem fazer um triangulo')
else:
    print('Os valore não podem formar um triangulo')
