"""

Gestão de diálogos
• Usa o ficheiro dialogos.txt no moodle, e 
faz print de todas as linhas do ficheiro.
• Separa cada linha do ficheiro por nome e fala.
• Constroi um dicionário em que os nomes são as keys e as falar os values.
• Serializa o dicionário num ficheiro JSON – dialogos.json
• Faz um executável do programa que leia um qualquer dialogos.txt e 
o transforme num dialogos.json.
• Esse executável deve pedir ao utilizador um input do ID de um NPC existente e imprimir apenas as falas desse NPC
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
• Cria um merged log com todas lingas dos dois logs, cada linha deve ter a indicação do dia no formato [DAY1] ou [DAY2]
• Conta o total de linhas de cada um dos dias usando o merged log
• Cria um dicionário estátistico que contenha o numero de acções de cada dia e o total de acções de ambos os dias
• Serializa o merged log num log_stats.json
Aula 724/11/2025
~~
"""


#Usa o ficheiro dialogos.txt no moodle, e faz print de todas as linhas do ficheiro.




file = open("dialogos.txt", "rt")


all_lines = file.readlines()
print(all_lines)
for line in all_lines:
    print(line.strip())
file.close()

