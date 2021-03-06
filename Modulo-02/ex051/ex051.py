print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r + 1
for c in range(t, d, r):
    print(c, end= ' ')
print('Acabou')
