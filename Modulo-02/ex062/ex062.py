print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
cont = 0
opcao = 10
while not opcao == 0:
    print(num, end=' -> ')
    num += razao
    cont += 1
    opcao -= 1
    if opcao == 0:
        print('PAUSA')
        opcao = int(input('Quantos termos voce vai querer mostrar mais?? '))
print(f'progueção finalizada com {cont} termos')
