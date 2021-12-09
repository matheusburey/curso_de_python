lighter_person = []
heavy_person = []
registration_list = list()
print('-' * 20)
print(f'{"CADASTRO DE PESSOAS":^20}')
print('-' * 20)

while True:
    name = str(input('Nome: '))
    weight = float(input('Peso: '))
    registration_list.append([name, weight])

    if len(registration_list) == 1:
        lighter_person = [name, weight]
        heavy_person = [name, weight]
    elif weight > heavy_person[1]:
        heavy_person = [name, weight]
    elif lighter_person[1] > weight:
        lighter_person = [name, weight]
    choice = str(input('Deseja continuar?[S/N] ')).upper()
    if choice != 'S':
        break

print('-' * 20)
print(f'Voce cadastrou {len(registration_list)} pessoas')
print(f'O maior peso foi de {heavy_person[0]} de {heavy_person[1]} kg')
print(f'O menor peso foi de {lighter_person[0]} de {lighter_person[1]} kg')
