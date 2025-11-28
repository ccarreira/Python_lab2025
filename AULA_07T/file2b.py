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


"""


#Usa o ficheiro highscore.json do moodle, 

#0 PRE

import os
os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\AULA_07T")
#os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/Python_lab2025/AULA_07T")

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
    try:
        player_data = json.loads(json_data)
        print("Loaded player data:", player_data)
    except json.JSONDecodeError:
        print("json inválido")
file.close()


# com exceptions

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



#versao b

try:
    file = open("highscores.json", "rt")
    json_data = file.read()

    if not json_data:
        raise ValueError("Erro: Ficheiro Vazio!")

    try:
        player_data = json.loads(json_data)
    except json.JSONDecodeError as e:
        raise ValueError("Erro: Ficheiro Não Contém JSON Válido!") from e

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

nome  = str(input("name: "))
score = int(input("score: "))

player_data["highscores"].append({"name": nome, "score": score})
print(player_data)


# • Ordena a lista de highscores por score descrescente 
# (sem usar sort() ou sorted())

highscores = player_data["highscores"]
highscores_ordenado = []

while highscores:
    maior = highscores[0]
    for player in highscores:
        #print("Maior", maior, "Player", player)
        if player["score"] > maior["score"]:
            maior = player
    highscores_ordenado.append(maior)
    highscores.remove(maior)

print("Highscores ordenados:", highscores_ordenado)

#• Mantem apenas os 3 melhores resultados

highscores_top3 = {"highscores": highscores_ordenado[:3]}
print("Highscores top 3:", highscores_top3)

#• Serializa novamente a lista de scores como new_highscores.json

f = open("new_highscores.json", "w", encoding="utf-8")
json.dump(highscores_top3, f, ensure_ascii=False, indent=2)
f.close()

#• No final imprime o novo ranking numerado (1º, 2º e 3º)

for i, p in enumerate(highscores_top3["highscores"], start=1):
    print(str(i)+"º :", p["name"], " : ", p["score"])

"""

i=1
for p in highscores_top3["highscores"]:
    print(str(i)+"º :", p["name"], " : ", p["score"])
    i += 1

"""