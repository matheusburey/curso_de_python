print('=' * 30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('=' * 30)
'''cont50 = cont20 = cont10 = cont1 = 0
num = int(input('Qual valor deseja sacar: R$ '))

while True:
    if num >= 50:
        num -= 50
        cont50 += 1
    elif num >= 20:
        num -= 20
        cont20 += 1
    elif num >= 10:
        num -= 10
        cont10 += 1
    elif num >= 1:
        num -= 1
        cont1 += 1
    elif num == 0:
        break
print(fVoce recebeu:
{cont50} notas de R$ 50
{cont20} notas de R$ 20
{cont10} notas de R$ 10
{cont1} notass de R$ 1
Volte sempre!!!)
minha resposta'''
#resposta do professor
num = int(input('Qual valor deseja sacar: R$ '))
total = num
ced = 50
tot = 0
while True:
    if ced <= total:
        total -= ced
        tot += 1
    else:
        print(f'Total de {tot} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if total == 0:
            break


