print('-' * 15)
print('\033[35mFinanceira\033[m')
print('-' * 15)
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do seu salario: R$ '))
ano = float(input('Digite quantos anos deseja pagar: '))

porcent = salario * 0.3
parcela = casa / (ano * 12)

if parcela > porcent:
    print(f'\033[33mNão podemos realizar o emprestimo as parcelas serião de {parcela:.2f} e seu salario so permite ate {porcent:.2f}')
else:
    print(f'\033[32mSeu emprestimo foi aprovado o valor da prestação é de R$ {parcela:.2f} em {ano * 12:.0f}X')
