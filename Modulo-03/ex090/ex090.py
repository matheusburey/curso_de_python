cadastros = []
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    cadastros.append([nome , [n1, n2], media])
    sn = str(input('Deseja continuar [S/N]: ')).upper()
    if sn == 'N':
        break
print('-=' * 20)
print(f'Nº | {"NOME":<15} | MEDIA')
print('-' * 30)
for num , l in enumerate(cadastros):
    print(f'{num} | {l[0]:<15} | {l[2]:.1f}')
print('-' * 30)
while True:
    aluno = int(input('Mostrar a nota de qual aluno?(999 parar): '))
    if aluno == 999:
        break
    print(f'As notas de {cadastros[aluno][0]} são {cadastros[aluno][1]}')
    print('-' * 30)

