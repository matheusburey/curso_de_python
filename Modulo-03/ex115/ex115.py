from lib import interface
from lib import validacao
from time import sleep

arq = "lista.txt"
validacao.arquivo_existe(arq)

while True:

    interface.menu()
    sleep(0.3)
    escolha = validacao.valida('\033[33mSua opção: \033[m')
    sleep(0.5)
    if escolha == 1:
        interface.cabecalho('PESSOAS CADASTRADAS')
        validacao.ler_arquivo(arq)
        sleep(0.5)
    elif escolha == 2:
        interface.cabecalho('NOVO CADASTRO')
        validacao.add_pessoa(arq)
        sleep(0.5)
    else:
        interface.cabecalho('SAINDO DO SISTEMA...')
        sleep(0.5)
        break
