salario = float(input('Digite o salario: R$ '))
novo = salario + salario * 0.15 if salario <= 1250 else salario + salario * 0.10
print(f'O novo salario é: R$ {novo:.2f}')
