def escreva(fra):
    esp = len(fra) + 4
    print('-' * esp)
    print(f'  {fra}')
    print('-' * esp)


frase = str(input('digite um frase: '))
escreva(frase)
