a = float(input('Digite o valor do primeiro segmento: '))
b = float(input('Digite o valor do segundo sgmeno: '))
c = float(input('Digite o valor do terceiro segmento: '))

if a < b + c and b < c + a and c < b + a:
    print('Os valores digitados podem formar um triangulo', end=' ')
    if a == b ==c:
        print('EQUILATERO')
    elif a == b or a == c or b == c:
        print('ISOSCELES')
    else:
        print('ESCALENO')
else:
    print('Os valore não podem formar um triangulo')
