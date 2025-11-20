room_descriptions = [
    ["A", "B", "C", "D", "E"], 
    ["F", "G", "H", "I", "J"], 
    ["K", "L", "M", "N", "O"], 
    ["P", "Q", "R", "S", "T"], 
    ["U", "V", "W", "X", "Y"]
    ]

room_exits = [
    [(False, False, True, False), (False, True, False, False), (False, True, True, True), (False, True, True, True), (False, False, True, True)], 
    [(True, False, True, False), (False, True, True, False), (True, True, True, True), (True, False, False, True), (True, False, True, False)], 
    [(True, False, True, False), (True, False, False, False), (True, False, True, False), (False, True, False, False), (True, False, True, True)], 
    [(True, False, True, False), (False, True, True, False), (True, True, False, True), (False, False, True, False), (True, False, True, False)], 
    [(True, True, False, False), (True, False, False, True), (False, False, False, False), (True, False, False, False), (True, False, False, False)]
    ]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

position = (2, 2)

while True:
    x, y = position

    print(position, ":", room_descriptions[y][x])

    print("What now?")
    command = input("Choose the direction you want to go north, south, east, west) or exit\n")

    if (command == "north"):
        if room_exits[y][x][NORTH]:
            print("you move north...")
            y += -1
        else:
            print("You can't move " + command + "!")
    elif (command == "south"):
        if room_exits[y][x][SOUTH]:
            print("you move south...")
            y += 1
        else:
            print("You can't move " + command + "!")
    elif (command == "west"):
        if room_exits[y][x][WEST]:
            print("you move west...")
            x += -1
        else:
            print("You can't move " + command + "!")
    elif (command == "east"):
        if room_exits[y][x][EAST]:
            print("you move east...")
            x += 1
        else:
            print("You can't move " + command + "!")
    elif (command == "exit"):
        break
    else:
        print("I don't understand " + command + "!")

    position = (x,y)