total = con = 0
for c in range(1, 501 , 2):
    if c % 3 == 0:
        total += c
        con += 1
print(f'A soma de todos {con} os valores é {total}')
