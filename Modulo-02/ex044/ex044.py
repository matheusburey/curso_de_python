print('-' * 20)
print('LOJAS AMERICANAS')
print('-' * 20)
valor = float(input('Digite o valor da compra: '))
print('''FORMAS DE PAGAMETO
[ 1 ] A VISTA (dinheiro/cheque)
[ 2 ] A VISTA (cartao)
[ 3 ] 2x NO CATAO
[ 4 ] 3x OU MAIS NO CARTAO''')
escolha = int(input('Qual voce deseja: '))

if escolha == 1:
    print(f'Sua compra recebeu um desconto de 10% de R$ {valor:.2f} ficara R$ {valor - valor * 0.1:.2f}')
elif escolha == 2:
    print(f'Sua compra recebeu um desconto de 5% de RS {valor:.2f} vai ficara R$ {valor - valor * 0.05:.2f}')
elif escolha == 3:
    print(f'Sua compra ficou em 2x de R${valor / 2:.2f} o valor total de R$ {valor:.2f}')
elif escolha == 4:
    vezes = int(input('Em quantas parcelas: '))
    total = valor + valor * 0.2  
    print(f'Em {vezes}x saira R$ {total / vezes:.2f} por mes com o total de {total:.2f}')
else:
    print('Opçao invalida tente novamente')
