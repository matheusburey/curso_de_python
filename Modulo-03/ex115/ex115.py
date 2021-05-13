from lib import interface
from lib import validacao
from time import sleep

arq = "lista.txt"
validacao.arquivo_existe(arq)

while True:
    interface.interface()
    sleep(0.3)
    escolha = validacao.valida('\033[33mSua opção: \033[m')
    sleep(0.5)
    if escolha == 1:
        validacao.ler_arquivo(arq)
    elif escolha == 2:
        print('2')
    else:
        print(f'{"SAINDO DO SISTEMA":^40}')
        print('/-' * 20)
        sleep(0.5)
        break
