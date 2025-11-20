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


def move_player(direction_text, direction_index, y_inc, x_inc):
    global position



    x, y = position
    if command == direction_text:
        if room_exits[y][x][direction_index]:
            y += y_inc
            x += x_inc
            position = (x, y)
            print("You move " + direction_text + " to room " + room_descriptions[y][x])
        else:
            print("You can't move " + direction_text + "!")
        return True
    return False


while True:
    x, y = position
    print(position, ":", room_descriptions[y][x])
    print("What now?")

    command = input("Choose the direction you want to go north, south, east, west) or exit\n")

    if command == "exit":
        print("Exiting game...")
        break
    elif move_player("north", NORTH, -1, 0):
        pass
    elif move_player("south", SOUTH, 1, 0):
        pass
    elif move_player("east", EAST, 0, 1):
        pass
    elif move_player("west", WEST, 0, -1):
        pass
    else:
        print("I don't understand " + command + "!")