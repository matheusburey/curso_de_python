from utilidadescev import moeda
from utilidadescev import dados

valor = dados.leia_dinheiro('Digite o valor: R$ ')
moeda.resumo(valor, 30, 30)
