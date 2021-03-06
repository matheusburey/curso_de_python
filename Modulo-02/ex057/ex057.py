sexo = str(input('Digite seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
        print('Volor incorreto digite novamente')
print(f'Sexo {sexo} registrado com sucesso')
