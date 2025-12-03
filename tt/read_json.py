
import sys
import json

if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = input()

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