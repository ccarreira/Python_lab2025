import json

#path = r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/GIT_REP/FPSemana04"

import os
os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/GIT_REP/FPSemana04")

#file = open(path+"data.json", "rt")

file_path="data.json"

class CriticalError(Exception):
    """File Not Found, """

def all_fields_in_data(self, data):
    hasNome = False
    hasIdade = False
    hasLocalizacao = False
    for key in data:
        if key == "nome": hasNome = True
        if key == "idade": hasIdade = True
        if key == "localizacao": hasLocalizacao = True
    return (hasNome and hasIdade and hasLocalizacao)

try:
    file = open(file_path, "rt")
    json_data = file.read()

    if not json_data:
        raise ValueError("Ficheiro Vazio!")

    try:
        player_data = json.loads(json_data)
        print(player_data)
        if (not all_fields_in_data(player_data)): 
            raise ValueError("Campos Obrigatórios em Falta!")
    except json.JSONDecodeError as e:
        raise ValueError("Ficheiro Não Contém JSON Válido!") from e

except FileNotFoundError as e:
    raise CriticalError("Ficheiro Não Encontrado!") from e

except ValueError as e:
    print("Erro:", e)

except CriticalError as e:
    print("Erro:", e)

finally:
    try:
        print("Processo Concluído!")
        file.close()
    except:
        pass


