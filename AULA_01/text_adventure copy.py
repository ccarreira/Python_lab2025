
while True:
    print("What now?")
    command = input("Choose the direction you want to go north, south, east, west) or exit\n")

    if (command == "north"):
        print("you move north...")
    elif (command == "south"):
        print("you move south...")
    elif (command == "west"):
        print("you move west...")
    elif (command == "east"):
        print("you move east...")
    elif (command == "exit"):
        break
    else:
        print("I don't understand " + command + "!")