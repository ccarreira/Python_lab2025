"""
2. Sistema de high scores
• Usa o ficheiro highscore.json do moodle, cria um dicionário 
com os dado e imprime. Faz uma verificação para confirmar que 
o ficheiro não está vazio
• Usa o sistema de input para pedir ao utilizador um novo nome 
e score inteiro. Adiciona esses dados aos highscores
• Ordena a lista de highscores por score descrescente (sem usar sort() 
ou sorted())
• Mantem apenas os 3 melhores resultados
• Serializa novamente a lista de scores como new_highscores.json
• No final imprime o novo ranking numerado (1º, 2º e 3º)

3. Merge de game logs
• Usa os dois ficheiro que estão no moodle – day1.log e day2.log
• Abre os ficheiro e lê todas as linhas de cada um deles
• Cria um merged log com todas lingas dos dois logs, 
cada linha deve ter a indicação do dia no formato [DAY1] ou [DAY2]
• Conta o total de linhas de cada um dos dias usando o merged log
• Cria um dicionário estátistico que contenha o 
numero de acções de cada dia e o total de acções de ambos os dias
• Serializa o merged log num log_stats.json

"""


#Usa o ficheiro highscore.json do moodle, 

#0 PRE

import os
#os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\AULA_07T")
os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/Python_lab2025/AULA_07T")

import json

#1 cria um dicionário com os dados e imprime. 
# Faz uma verificação para confirmar que 
# o ficheiro não está vazio

file = open("highscores.json", "rt")

player_data = {}

json_data = file.read()

if not json_data:
    print("Erro: ficheiro vazio")
else:
    player_data = json.loads(json_data)
    print("Loaded player data:", player_data)

file.close()

# com exceptions

import json

try:
    # 1) Open file
    file = open("highscores.json", "rt")

    # 2) Read contents
    json_data = file.read()

    if not json_data:
        raise ValueError("Ficheiro vazio")   # your custom rule

    # 3) Parse JSON
    try:
        player_data = json.loads(json_data)
    except json.JSONDecodeError as e:
        raise ValueError("JSON inválido") from e

except FileNotFoundError:
    print("Erro: ficheiro highscores.json não existe")

except ValueError as e:
    # This handles: empty file OR invalid JSON
    print("Erro:", e)

finally:
    # guaranteed to run if file exists
    try:
        file.close()
    except:
        pass






#2• Usa o sistema de input para pedir ao utilizador um novo nome  
# e score inteiro. Adiciona esses dados aos highscore
"""
nome  = input("nome: ")
score = input("score: ")

player_data["highscores"].append({"nome": nome, "score": score})
print(player_data)
"""

# • Ordena a lista de highscores por score descrescente 
# (sem usar sort() ou sorted())

highscores = player_data["highscores"]
ordenado = []

while highscores:
    maior = highscores[0]
    for player in highscores:
        #print("Maior", maior, "Player", player)
        if player["score"] > maior["score"]:
            maior = player
    ordenado.append(maior)
    highscores.remove(maior)


print("Highscores ordenados:", ordenado)

#• Mantem apenas os 3 melhores resultados