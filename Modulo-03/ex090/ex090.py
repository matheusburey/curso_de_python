aluno = dict()
aluno['nome'] = str(input('Nome: ')).capitalize().strip()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
print('-' * 20)
print(f'O nome do aluno é {aluno["nome"]}')
print(f'a media é {aluno["media"]}')
if aluno['media'] >= 7:
    print('APROVADO')
elif aluno['media'] >= 5:
    print('RECUPERÇÃO')
else:
    print('REPROVADO')
