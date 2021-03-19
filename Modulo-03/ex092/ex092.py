from datetime import datetime
cadastro = {}

cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de trabalho: '))

if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano da contratação:'))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)
print('-' * 20)
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')
