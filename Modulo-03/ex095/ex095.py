time = []
jogador = {}
gols = []
print('=-' * 20)
print(f'{"LISTA DE JOGADORES":^40}')
print('=-' * 20)

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    jogador['partidas'] = int(input(f'Quanas partias {jogador["nome"]} jogou: '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols ele fez na {c + 1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    sn = str(input('Deseja continuar: ')).upper()
    while sn not in 'SN':
        print('Comando invalido...')
        sn = str(input('Deseja continuar: ')).upper()
    print('-' * 30)
    if sn == 'N':
        break

print(f'Nº|{"Nome":<8} |{"gols":<15}| Total')
for c, l in enumerate(time):
    print(f'{c} |{l["nome"]:<8} |{str(l["gols"]):<15}|{l["total"]}')
print('-' * 30)
ver = 0
while ver != 999:
    ver = int(input('Mostrar dados de qual jogador (999 para): '))
    if ver < len(time):
        print(f'Levantamendo do jogador {time[ver]["nome"]}')
        for c, v in enumerate(time[ver]['gols']):
            print(f'    No {c + 1}º jogo fez {v}')
    elif ver != 999:
        print('Comando invalido')
print('<<<< VOLTE SEMPRE >>>.')
