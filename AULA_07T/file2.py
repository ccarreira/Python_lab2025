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


#Usa o ficheiro highscore.json do moodle, cria um dicionário 
#com os dado e imprime. Faz uma verificação para confirmar que 
#o ficheiro não está vazio

#0 PRE

import os
#os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\AULA_07T")
os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/Python_lab2025/AULA_07T")


#1
import json

file = open("highscore.json", "rt")

player_data = {}

json_data = file.read()
player_data = json.loads(json_data)
print("loaded player data:", player_data)
file.close()
