from time import sleep


def maior(*n):
    con = mai = 0
    print('Analizando os valores informados...')
    for c in n:
        print(c, end=' ')
        sleep(0.3)
        if c > mai:
            mai = c
        con += 1
    print(f'Foram informados {con} valores e os maior valor foi {mai}')
    print('-_' * 20)


maior(2, 9, 4, 5, 7, 2)
maior(5, 7, 9, 4, 5, 8)
maior(4, 7, 0)
maior(6)
maior()
