import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except ValueError:
    print('O site pudin esta indisponivel')
else:
    print('O site pudin esta disponivel')
