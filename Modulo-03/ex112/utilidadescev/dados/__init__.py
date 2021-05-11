def leia_dinheiro(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')

        if entrada.isdecimal() or entrada.isnumeric:
            return float(entrada)
        else:
            print(f'Erro: Valor \"{entrada}\" invalido')
