from math import hypot
b = float(input('Digite o valor do cateto adjacente: '))
c = float(input('Digite o valor do cateto oposto: '))
a = hypot(3,3) # or sqrt(b ** 2 + c ** 2)
print(f'A hipotenusa vale {a:.3f}')
