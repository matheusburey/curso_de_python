val1 = int(input('Digite um valor: '))
val2 = int(input('Digite um valor: '))
val3 = int(input('Digite um valor: '))
maior = menor = val1

if maior < val2:
    maior = val2
if maior < val3:
    maior = val3

if menor > val2:
    menor = val2
if menor > val3:
    menor = val3

print('O maior valor é:',maior)
print('O manor valor é:', menor)
