"""
1. Localização no mapa
Cria uma matriz 3x3 chamada mapa, onde cada célula contém uma string com a
descrição da sala (ex.: "Sala (x,y)"). 
Depois, cria um tuplo posicao = (1, 2) e imprime a descrição correspondente.
2. Usando o mesmo mapa 3x3, define uma posição inicial (1,1) 
e implementa as seguintes regras de movimento: 
"w"→sobe / "s"→desce / "a"→esquerda / "d"→direita
O programa deve:
• Pedir um comando (w, a, s, d),
• Atualizar a posição,
• Mostrar a nova descrição da sala.
• Guardar o histórico da salas onde o jogador esteve e imprimi-la na saída
3. Expande o exercício anterior.
Se o jogador tentar sair do mapa, o programa deve: 
impedir o movimento e mostrar a mensagem: “Não podes sair do mapa!”

"""

rooms = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
        ]

position = (1, 1)

num_rows = len(rooms)
num_columns = len(rooms[0])

historico = []


def get_room(x,y):
    return rooms[y-1][x-1]

def show_position():
    print("Voce está em x:", x, " y:", y)
    print("Na sala: ", get_room(x,y))


def move_player(new_x = 1,new_y= 1):
    global position
    if is_inside_map(new_x, new_y):
        x = new_x
        y = new_y
        position = (x, y)
        return True
    else:
        print("Nao podes sair do mapa!")
        print("***********************")
        return False

def is_inside_map(x, y):
    return 1 <= x <= num_columns and 1 <= y <= num_rows

def get_command():
    new_command = input("Choose North, South, East, West, or Exit: ").strip().lower()
    return new_command


historico.append(get_room( position[0], position[1]))
while True:
    x, y = position
    show_position()
    command = get_command()
    print("command: ", command)
    if command == "exit":
        print("Historico de salas", historico)
        print("FIM")
        break
    elif command == "north":
        new_x = x
        new_y = y-1
    elif command == "south":
        new_x = x
        new_y = y+1
    elif command == "east":
        new_x = x+1
        new_y = y
    elif command == "west":
        new_x = x-1
        new_y = y
    else:
        print("Command invalido")
        continue

    if move_player(new_x, new_y):
        historico.append(get_room(new_x,new_y))
