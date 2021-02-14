dias = int(input('Quantos dias alugados: '))
rodados = float(input('Quantos Km rodados: '))
vald = dias * 60
valkm = rodados * 0.15
print(f'O total a pagar é de R$ {vald + valkm:.2f}, R${vald} pelos dias e R${valkm} pelos Km rodados')
