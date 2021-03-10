total = mais = men = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: ')).capitalize().strip()
    valor = float(input('Qual o valor do poduto: '))

    total += valor
    cont += 1

    if cont == 1:
        barato = produto
        men = valor
    if men > valor:
        barato = produto
        men = valor

    if valor > 1000:
        mais += 1
    
    opcao = str(input('Deseja cadastrar mais [S/N]: ')).upper()
    while not opcao in 'SN':
        opcao = str(input('Deseja cadastrar mais [S/N]: ')).upper()
    if opcao == 'N':
        break

print(f'Foram gastos no total R$ {total:.2f} na compra de {cont} itens')
print(f'E {mais} itens com valor acima de R$ 1000.00')
print(f'O produto mais barato foi {barato}')