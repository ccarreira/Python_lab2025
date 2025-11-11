"""
Modificar string

print(string.replace("he", "she"))
print(string.upper())
print(string.lower())
print(string.strip())
print(string.index("he"))
print(string.count("e"))
print(string.split(" "))

"""

#0

frase = "The enemy is strong!"
frase = frase.replace("enemy", "friend")

print(frase)

#1

"""
Cria uma variável map_description com o texto
"A dark cave with a small torch on the wall".
Escreve um programa que:
1. Conta quantas vezes aparece a letra "a"
2. Imprime o resultado.
3. Mostra todas as palavras da descrição numa lista.
"""

map_description = "A dark cave with a small torch on the wall"
print(map_description.lower().count("a"))
print(map_description.split())

#2
"""
Cria uma lista com três nomes de NPCs ([“maul", “plagueis", “bane"]).
Escreve um programa que:
1. Escreve cada nome com a primeira letra maíuscula
2. Imprime "Darth [Nome]" para cada um.
"""

NPCs = ["maul", "plagueis", "bane"]

for i in range(len(NPCs)):
    nome = NPCs[i]
    nome = (nome[0:1]).upper()+nome[1:]
    print("Darth "+nome)


#3

"""
Cria um mini-sistema de codificação que:
1. Pede ao jogador uma palavra
2. Substitui todas as vogais por "*"
3. Imprime a versão codificada.
"""

vogais = ["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]
palavra = input("palavra secreta: ")

for vogal in vogais:
    palavra = palavra.replace(vogal, "*")

print(palavra)

