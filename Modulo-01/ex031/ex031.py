valor = float(input('Qual é a distancia da viajem: Km '))
passgem = valor * .50 if valor <= 200 else valor * 0.45
print(f'O valor da passagem sera de R${passgem:.2f}')
