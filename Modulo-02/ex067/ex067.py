fator2 = 0
fator1 = int(input('Digite um numero para ver sua tabuada: '))
print('-' * 20)
while True:
    fator2 += 1
    print(f'{fator1} x {fator2:2} = {fator1 * fator2:2}')
    if fator2 == 10:
        print('-' * 20)
        fator1 = int(input('Quer ver outra tabuada?(-1 para parar) '))
        fator2 = 0
        if fator1 < 0:
            break
