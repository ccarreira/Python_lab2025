

"""
• Cria uma classe Player com:
• atributos: name, x, y, stamina
• construtor que recebe name, x, y e stamina
• métodos:
• log() → imprime posição e stamina
• move(dx, dy) → altera x e y e reduz stamina em 1
por cada movimento (mesmo que seja diagonal)
• is_exhausted()→devolve True se stamina <= 0,
caso contrário False
"""

class Player:
    name = ""
    x = 0
    y = 0
    stamina = 0

    def __init__(self, name = "Player", x=0, y=0, stamina =100 ):
        self.name = name
        self.x = x
        self.y = y
        self.stamina = stamina

    def log(self):
        print("Position: x=", self.x, " , y:", self.y)
        print("Stamina: ", self.stamina)

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.stamina -=1

    def is_exausted(self):
        return self.stamina <= 0

"""


• Programa principal:
1. Cria um Player na posição (0, 0) com stamina 5. Pede input para o nome
2. Dentro dum while usa o input do player para se movimentar:
• Pode se mover na vertical, horizontal e diagonal
• Usar um dicionário com comandos e lambdas para definir a direcção
3. Para cada movimento:
• Se o jogador não estiver exausto, chama move
• Se já estiver exausto, imprime "Too tired to move" e pára o ciclo
4. No fim, chama log().
Exemplo de execução
"""

p1 = Player("Player", 0, 0, 5)

commands = {
    "N": (0,1),
    "NE": (1,1),
    "NW": (-1,1),
    "S": (0,-1),
    "SE": (1,-1),
    "SW": (-1,-1),
    "E": (1,0),
    "W": (-1,0)
}

p1.name = input("Nome do jogador? ")

while True:
    command = input("Movimento: N, NE, NW, S, SE, SW, E, W, (Q)uit) ").strip().upper()
    if command == "Q": 
        print("fim")
        break
    if command in commands:
        dx, dy = commands[command]
        print(dx, dy)
    else:
        print("Command not found")
        continue
    
    if not p1.is_exausted(): 
        p1.move(dx, dy)
        print(p1.log())
    else:
        print("Too tired to move") 
