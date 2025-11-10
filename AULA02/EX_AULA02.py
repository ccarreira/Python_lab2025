rooms = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
        ]

position = (1, 1)

num_rows = len(rooms)
num_columns = len(rooms[0])


def show_position():
    print("Voce está em x:", x, " y:", y)
    print("Na sala: ", rooms[y-1][x-1])

def move_player(new_x = 1,new_y= 1):
    global position
    if is_inside_map(new_x, new_y):
        x = new_x
        y = new_y
        position = (x, y)
        return True
    else:
        print("Nao podes sair do mapa")

def is_inside_map(x, y):
    return 1 <= x <= num_columns and 1 <= y <= num_rows

def get_command():
    new_command = input("Choose North, South, East, West, or Exit: ")
    #new_command = input("Choose North, South, East, West, or Exit: ").strip().lower()
    print("new command: ", new_command)
    return new_command



while True:
    x, y = position
    show_position()
    command = get_command()
    print("command: ", command)
    if command == "exit":
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
        new_x = x
        new_y = y
        continue

    move_player(new_x, new_y)





