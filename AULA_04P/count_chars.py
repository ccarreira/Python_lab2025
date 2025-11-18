# Solicita uma frase e depois imprime um dicionario
# palavra, caracteres dessa palavra
# Quantos Orangotangos?
#{'quantos': 7, 'orangtangos': 12, '?': 1}
#


frase = input().split()
dicionario = {}

"""
# enumerate substitui isto:

for i in range(len(frase)):
    palavra = frase[i]
"""
for i, palavra in enumerate(frase):
    dicionario[palavra] = len(palavra)

print(dicionario)