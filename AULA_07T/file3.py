""" 3.  Merge de game logs
        Usa os dois ficheiro que estão no moodle  day1.log e day2.log """

import os
os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\AULA_07T")
#os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/Python_lab2025/AULA_07T")

import json


# Abre os ficheiro e lê todas as linhas de cada um deles

file1 = open("day1.log", "rt")
file2 = open("day2.log", "rt")

file1_lines = file1.readlines()
file2_lines = file2.readlines()


#• Cria um merged log com todas linhas dos dois logs, 
# cada linha deve ter a indicação do dia no formato [DAY1] ou [DAY2]

merged_log = {}
merged_log["DAY1"] = []
merged_log["DAY2"] = []

for line in file1_lines:
    new_line = "[DAY1] "+line.strip() #strip tira o \n
    merged_log["DAY1"].append(new_line)

for line in file2_lines:
    new_line = "[DAY2] "+line.strip()
    merged_log["DAY2"].append(new_line)


# Conta o total de linhas de cada um dos dias usando o merged log

day1_count = len(merged_log["DAY1"])
day2_count = len(merged_log["DAY2"])

#print(day1_count)
#print(day2_count)

# Cria um dicionário estátistico que contenha o 
# numero de acções de cada dia e o total de acções de ambos os dias

stats_log = {}
stats_log["DAY1"] = day1_count
stats_log["DAY2"] = day2_count
total = 0

for day, valor in stats_log.items():
    if day[:3] == "DAY":
        total += valor

stats_log["Total"] = total
print(stats_log) 

# Serializa o merged log num log_stats.json

f = open("log_stats.json", "w", encoding="utf-8")
json.dump(stats_log, f, ensure_ascii=False, indent=2)
f.close()



