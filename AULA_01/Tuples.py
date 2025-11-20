"""

1. Cria um tuplo hero que contenha: nome, nível, vida, e experiência.
Depois, imprime uma frase no formato: “O herói <nome> está no nível <nível> com <vida> HP e <experiência> XP.”



nome = "king Jon"
nivel = 10
vida = 100
XP = 23000

hero = (nome, nivel, vida, XP)

print("O herói", hero[0], "está no nível", hero[1], "com", hero[2] ,"HP e", hero[3] ,"XP.")


2. Define um tuplo spawn_point com as coordenadas iniciais (0, 0, 0) e imprime cada valor num formato legível.


print("***********************************")

spawn_point = (0, 0, 0)

print("Spawn Point")
print("X:", spawn_point[0])
print("Y:", spawn_point[1])
print("Z:", spawn_point[2])



3. Cria um tuplo npc com um nome, uma idade e uma lista de itens que o NPC vende (3 strings).
Depois imprime apenas o nome e a lista de itens.

"""
print("***********************************")

nome = "Lokas"
idade = 30
items = ["taça", "faca", "capa"]

npc = (nome, idade, items)

print("Nome:", npc[0])

for i in range(len(npc[2])):
    print("item", i, "-", npc[2][i])


"""

4. Cria um tuplo moedas = (5, 10, 2) que representa o número de moedas de ouro,
prata e bronze.Cada moeda tem um valor diferente (5, 3, 1), no final imprime: Moedas de cada tipo; total de moedas,
valor por moedas e valor total
"""

print("***********************************")
moedas = (5, 10, 2)
cotacao = (5, 3, 1)

print("Moedas de ouro:", moedas[0], "de prata:", moedas[1], "de bronze:", moedas[2])
print("Valor das Moedas de ouro:", moedas[0]*cotacao[0], "de prata:", moedas[1]*cotacao[1], "de bronze:", moedas[2]*cotacao[2])

print("total moedas", moedas[0]+moedas[1]+moedas[2])
print("valor total", moedas[0]*cotacao[0]+moedas[1]*cotacao[1]+moedas[2]*cotacao[2])



"""
5. Cria um tuplo scores = ("Ana", "Bruno", "Carla", "David", "Eva")
Atribui as duas primeiras variáveis a uma lista primeiros e guarda o resto na lista outros.
No final imprime as duas listas.

"""

scores = ("Ana", "Bruno", "Carla", "David", "Eva")

primeiros = scores[:2]
outros = scores[2:]

print(primeiros)
print(outros)