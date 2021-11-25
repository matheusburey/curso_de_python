num = cont = total = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        total += num
        cont += 1
print(f'Voce digitou {cont} numeros e a soma eles foi {total}')
