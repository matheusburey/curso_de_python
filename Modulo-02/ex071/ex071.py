print('\033[33m', '=' * 30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('=' * 30)
'''
minha resposta

cont50 = cont20 = cont10 = cont1 = 0
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

resposta do professor
num = int(input('\033[32mQual valor deseja sacar: R$ \033[m'))
total = num
ced = 50
tot = 0
while True:
    if ced <= total:
        total -= ced
        tot += 1
    else:
        if tot > 0:
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
print('-' * 30)
print('Volte sempre!!')
'''

# Minha Nova resposta
valor = int(input('\033[32mQual valor deseja sacar: R$ \033[m'))
cedulas = (50, 20, 10, 1)
i = total_cedulas = 0

while True:
    cedula = cedulas[i]
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    else:
        print(f'Total de {total_cedulas} cedulas de R$ {cedula}')
        i += 1
        total_cedulas = 0
        if valor == 0:
            break

print('-' * 30)
print('Volte sempre!!')
