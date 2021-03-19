gols = []
jogador = {'nome': str(input('Nome do jogador: '))}
total = int(input(f'Quantos partidas {jogador["nome"]} jogol: '))
for c in range(0, total):
    gols.append(int(input(f'Quantos gosl na partida {c + 1}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'- {k} = {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {total} partidas')
for c in range(0, total):
    print(f'    => Na partida {c + 1}, fez {jogador["gols"][c]} gols    ')
print(f'No total ele fez {jogador["total"]} gols    ')
