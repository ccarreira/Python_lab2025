"""
1 Cria um programa que mantém o registo de caças e pilotos da Rebelião.
• Adiciona um novo piloto "Luke Skywalker" com o caça "X-Wing".
• "Luke Skywalker" também pilotou um "Snowspeeder".
• Mostra todos os caças pilotados por "Poe Dameron".
• Mostra os caças em comum entre "Luke Skywalker" e "Wedge Antilles".

#5 Mostra os caças que "Red Leader" pilotou mas "Poe Dameron" nunca usou.
#6 Cria um conjunto all_ships com todos os caças únicos usados por todos os pilotos.
• Mostra a lista completa dos caças usados pela Rebelião, sem repetições
"""

fleet = {
    "Red Leader": {"X-Wing", "A-Wing"},
    "Wedge Antilles": {"X-Wing"},
    "Poe Dameron": {"X-Wing", "T-70", "Black One"}
}
#1
fleet["Luke Skywalker"] = {"X-Wing"}
#2
fleet["Luke Skywalker"].add("Snowspeeder")
print(fleet)
#3
print("Caças pilotados por Dameron: ", fleet["Poe Dameron"])

print("Caças pilotados por Dameron:")
for c in fleet["Poe Dameron"]:
    print(c)

#4 "Luke Skywalker" e "Wedge Antilles".
emcomum = []
for c in fleet["Luke Skywalker"]:
    if c in fleet["Wedge Antilles"]:
        emcomum.append(c)
print("Em comum:", emcomum)

#5
unicos = []
for c in fleet["Red Leader"]:
    if c not in fleet["Poe Dameron"]:
        unicos.append(c)
print("unicos:", unicos)

#6
all_ships = set()

#METODO A
for piloto in fleet:
    print("Piloto:", piloto)
    for ship in fleet[piloto]:
        if ship not in all_ships:
            all_ships.add(ship)
print(all_ships)

#METODO B

for piloto, naves in fleet.items():
    print("Piloto:", piloto)
    for ship in naves:
        all_ships.add(ship)
        print(ship)
print(all_ships)



"""
2. Cria um programa que gere recompensas imperiais sobre alvos procurados.
• Adiciona um novo caçador "IG-88" com um set vazio de alvos.
• Atribui-lhe o alvo "Han Solo".
• Mostra todos os alvos de "Boba Fett".
• Mostra os alvos que "Boba Fett" e "Bossk" têm em comum.
• Mostra os alvos que "Cad Bane" persegue mas "Bossk" não.
• Calcula o valor total da recompensa de Boba Fett, somando os
valores de cada alvo usando o dicionário reward_values.
• Cria um set com todos os alvos únicos procurados pelo Império.

    """

bounties = {
    "Boba Fett": {"Han Solo", "Chewbacca"},
    "Cad Bane": {"Ahsoka Tano", "Fennec Shand"},
    "Bossk": {"Han Solo", "Leia Organa"}
}

reward_values = {
    "Han Solo": 50000,
    "Chewbacca": 40000,
    "Leia Organa": 60000,
    "Ahsoka Tano": 80000,
    "Fennec Shand": 45000
}
