import random
import json


import os
os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\Algoritmo de Sorting-20251213")
#os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/Python_lab2025/AULA_07T")

# Condições:
# Lista de alunos foi feita por ordem alfabética (primeiro, último nome)
# Foi definido um seed para ser repetível

file = open("alunos.txt", "rt")
alunos = file.readlines()
file.close()

lista = []

for aluno in alunos:
    lista.append(aluno.strip())

random.seed(12345)
random.shuffle(lista)

evaluation = {}

keys = ("Monday 11", "Monday 12", "Tuesday 14", "Tuesday 15", "Tuesday 16", "Wednesday 15", "Wednesday 16", "Friday 14", "Friday 15")
bool1 = False
i = 0
for key in keys:
    if key == random.choice(keys) and not bool1:
        bool1 = True
        evaluation[key] = lista[i:i+4]
        i += 4
        print("a", key)
    elif key == "Friday 15":
        evaluation[key] = lista[i:]
        print("b", key)
    else:
        evaluation[key] = lista[i:i+3]
        i += 3
        print("c", key)
0
#print(evaluation)0


file = open("evaluation_schedule.json", "wt")
json_data = json.dumps(evaluation, indent=4)
file.write(json_data)
file.close()