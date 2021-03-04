peso = float(input('Qual é o seu peso: Kg '))
altura = float(input('Qual é a sua altura: cm '))
imc = peso / (altura /100) ** 2

print(f'Seu IMC é de {imc:.1f}, voce esta', end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('no PESO IDEAL')
elif imc < 30:
    print('com SOBRE PESO')
elif imc < 40:
    print('com OBESIDADE')
else:
    print('com OBESIDADE MÓRBIDA')
