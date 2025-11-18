#1

# Operações
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: division by zero!")
        return None
    return a / b

# Seleçcão
def calculate(a, b, operation):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        print("Unknown operation.")
        return None # equivalente a null em outras linguagens

# Execução
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

result = calculate(a, b, operation)

if result is not None:
    print("Result =", result)


##################################################

# 2

# mapa
rooms = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]


position = (1, 1) 

# Sala atual
def describe_room(pos):
    x, y = pos
    print("\nYou are in room", rooms[y][x])

# mover o jogador e devolver a nova posição
def move(pos, direction):
    x, y = pos
    if direction == "north":
        if y > 0:
            y -= 1
        else:
            print("You can't move north!")
    elif direction == "south":
        if y < len(rooms) - 1:
            y += 1
        else:
            print("You can't move south!")
    elif direction == "west":
        if x > 0:
            x -= 1
        else:
            print("You can't move west!")
    elif direction == "east":
        if x < len(rooms[0]) - 1:
            x += 1
        else:
            print("You can't move east!")
    else:
        print("Invalid direction.")
    return (x, y)


def game_loop():
    global position
    while True:
        describe_room(position)
        command = input("Choose direction (north, south, east, west) or 'exit': ").lower()
        if command == "exit":
            print("Game over.")
            break
        position = move(position, command)


game_loop()

