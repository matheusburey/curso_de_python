media = maisidade = contmul = 0
homen = ''

for c in range(1,5):

    print(f'------{c}ª PESSOA--------')
    nome = str(input('Digite seu nome: ')).upper()
    idade = int(input('digite sua idade: '))
    sexo = str(input('Sexo [M\F]: ')).upper()

    if maisidade < idade and sexo == 'M':
        maisidade = idade
        homen = nome
    elif sexo == 'F' and idade < 20:
        contmul +=1
    media += idade

print(f'A media de idades é {media / 4}')
print(f'O homem mais velho é {homen} com {maisidade} anos')
print(f'Ao todo são {contmul} mulheres com menos de 20 anos')
