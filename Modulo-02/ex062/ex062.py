print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
cont = 1
while cont < 11:
    print(num, end=' -> ')
    num += razao
    cont += 1
print('Fim!')
