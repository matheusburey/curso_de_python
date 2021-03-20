pessoa = dict()
cadastro = list()
total = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['idade'] = int(input('Idade: '))
    total += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if pessoa['sexo'] not in 'FM':
        print('ERRO, digite apenas F (femenino) e M (masculino)')
        pessoa['sexo'] = str(input('Sexo [M/F]: '))
    cadastro.append(pessoa.copy())
    sn = str(input('Deseja continuar [S/N] ')).upper()
    if sn not in 'SN':
        print('ERRO, apenas S (sim) ou N (não)')
        sn = str(input('Deseja continuar [S/N] ')).upper()
    print('=-' * 20)
    if sn == 'N':
        break
media = total / len(cadastro)
print(f'Foram cadastrados {len(cadastro)} pessoas')
print(f'A media de idades é {media:.2f}')
print('Mullhres cadastradas:')
for v in cadastro:
    if v['sexo'] == 'F':
        print(f'    -{v["nome"]} tem {v["idade"]} anos')
print('Pessoas com a idade acima da media: ')
for v in cadastro:
    if v["idade"] > media:
        print(f'    -{v["nome"]} tem {v["idade"]} anos do sexo {v["sexo"]}')
print('<<<< ENCERRADO >>>>')
