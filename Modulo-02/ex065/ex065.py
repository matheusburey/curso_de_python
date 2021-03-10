sn = 'S'
con = total = maior = menor = 0
while sn != 'N':
    num = int(input('Digite um numero: '))
    sn = str(input('Deseja continuar: ')).strip().upper()
    if con == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    con += 1
    total += num

print(f'Voce digitou {con} valores e a media deles foi {total / con:.2f}')
print(f'O maior valor foi o {maior} e o menor valor foi o {menor}')
