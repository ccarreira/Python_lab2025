"""
solicita duas palavras e em seguida imprime a intersecao dos caracteres presentes nas palavras
por ordem alfabetica, maiusculas e minusculas sao caracteres diferentes
Utilize a logica de sets

Input:
Orangotangos
Ornitorrinco

Output:
nOort

"""
palavra1 = input()
palavra2 = input()

letras_em_comum = set()
_lista_chars = set()
_lista_chars2 = set()


for char in palavra1:
    _lista_chars.add(char)
#print(_lista_chars)

for char in palavra2:
    _lista_chars2.add(char)
#print(_lista_chars2)

letras_em_comum = _lista_chars.intersection(_lista_chars2)

lista = sorted(letras_em_comum, key=lambda c: (c.lower(), c))

# Faz string
letras_em_comum_print = ""
for char in lista:
    letras_em_comum_print += char

print(letras_em_comum_print)