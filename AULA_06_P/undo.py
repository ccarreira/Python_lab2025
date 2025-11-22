from collections import deque

undo_stack = deque()
redo_stack = deque()

def do_action(action):
    action.execute()
    undo_stack.append(action)   # guarda no topo (direita)

def undo():
    if undo_stack:
        action = undo_stack.pop() # retira do topo (direita)
        action.undo()
        redo_stack.append(action)

def redo():
    if redo_stack:
        action = redo_stack.pop()
        action.execute()
        undo_stack.append(action)


# Ex action

class Action:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError

# addNumber extende Action    

class AddNumber(Action):
    def __init__(self, stack, value):
        self.stack = stack
        self.value = value

    def execute(self):
        self.stack.append(self.value)

    def undo(self):
        self.stack.pop()

# Move

class Move(Action):
    def __init__(self, character, dx, dy):
        self.character = character
        self.dx = dx
        self.dy = dy

    def execute(self):
        self.character.x += self.dx
        self.character.y += self.dy

    def undo(self):
        self.character.x -= self.dx
        self.character.y -= self.dy


class Character:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def move_north(char):
    return Move(char, 0, -1)

def move_south(char):
    return Move(char, 0, 1)

def move_west(char):
    return Move(char, -1, 0)

def move_east(char):
    return Move(char, 1, 0)


# Exemplo
"""
hero = Character(5, 5)

action = move_north(hero)
action.execute()
undo_stack.append(action)

print(hero.x, hero.y)      # 5, 4

undo_stack.pop().undo()

print(hero.x, hero.y)      # 5, 5
"""