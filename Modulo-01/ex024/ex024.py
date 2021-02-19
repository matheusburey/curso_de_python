nome = str(input('Dogite o nome de sua cidade: ')).lower().strip()
city = nome.split()
print('Sua cidade começa com santos?')
print("santo" in city[0])
