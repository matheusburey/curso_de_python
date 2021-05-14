def menu():
    print('\033[32m_-' * 20)
    cabecalho('MENU PRINCIPAL', '_-')
    print("""
    \033[35m[ 1 ] \033[36mVer pessoas cadastradas
    \033[35m[ 2 ] \033[36mCadastrar nova pessoa
    \033[35m[ 3 ] \033[36mSair do sistema\033[m""")


def cabecalho(msg, dec='--'):
    print(f'{msg:^40}')
    print(f'{dec}' * 20)
