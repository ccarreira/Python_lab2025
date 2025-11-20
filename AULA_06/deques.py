from collections import deque

"""
#1
lista_acoes = deque()

while True:
    acao = input("acao: ").strip().lower()
    if acao == "exit":
        print("sai")
        break
    elif acao == "undo":
        #undo
        if (lista_acoes):
            lista_acoes.pop()
            print("retirada", acao)
        else:
            print("nao ha acoes")
        print(lista_acoes)
    else:
        #adiciona
        if acao != "exit":
            lista_acoes.append(acao)
            print(lista_acoes)

print("historico", lista_acoes)
"""

#2
"""
enemies = deque(["Goblin", "Orc", "Troll"])

while enemies:
    e = enemies.pop()
    print("enemy entra:", e)
    print("enemy sai:", e)
"""

#3
"""
    Simula o motor de eventos de um jogo, onde:
• Eventos normais seguem FIFO. Eventos prioritários seguem LIFO. Usando duas listas
• normal_events → ["update player position", "detect collision", "generate particles"]
• priority_events → ["start cutscene", "pause", "boss arrival"]
• Usa uma unica deque para ambas
    
"""

normal_events = ["update player position", "detect collision", "generate particles"]
priority_events = ["start cutscene", "pause", "boss arrival"]

game_engine = deque()

for event in normal_events:
    game_engine.appendleft(event)

for event in priority_events:
    game_engine.append(event)

while game_engine:
    print("processing event: ", game_engine.pop())
