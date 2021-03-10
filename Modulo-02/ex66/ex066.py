cont = total = 0
while True:
    num = int(input('Digite um valor[999 para parar]: '))
    if num == 999:
        break
    cont += 1
    total += num
print(f'Foram digitados {cont} numeros e a soma entre eles é {total}')
