
import sys
import json

#import os
#os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/GIT_REP/FPSemana04")
#os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\tt")
#filepath = "data.json"

filepath = sys.argv[1]

def all_fields_in_data(data):
    return (("nome" in data) and ("idade" in data) and ("localização" in data))

try:
    file = open(filepath, "rt", encoding="utf-8")
    json_data = file.read()

    if not json_data:
        raise ValueError("Ficheiro Vazio!")

    try:
        player_data = json.loads(json_data)
        if (not all_fields_in_data(player_data)): 
            raise ValueError("Campos Obrigatórios em Falta!")
        print(player_data)
    except json.JSONDecodeError as e:
        raise ValueError("Ficheiro Não Contém JSON Válido!") from e

except FileNotFoundError as e:
    print("Erro:", "Ficheiro Não Encontrado!")

except ValueError as e:
    print("Erro:", e)

finally:
    print("Processo Concluído!")
    try:
        file.close()
    except:
        pass


