velo = float(input('Qual sua velocidade: '))
if velo >80:
    print(f'VOCE FOI MULTADO, o valor da multa é {(velo - 80)*7:.2f}')
else:
    print('Voce esta dentro da velociade, Boa viagem!!')
