######### funções como dados ###################


# Poderia ser feito de duas maneiras, usando print ou return da string das funções base

# Esta seria a forma mais simples de resolver conforme o enunciado


#1
def attack():
    print("You attacked the enemy!")

def defend():
    print("You raised your shield!")

def cure():
    print("You gained 10 HP!")

def inventory():
    print("You opened your inventory.")

def flee():
    print("You fled combat!")

def execute_action(action):
    action()

execute_action(attack)
execute_action(defend)
execute_action(cure)
execute_action(inventory)
execute_action(flee)


#2
actions = [attack, defend, cure, inventory, flee]

for act in actions:
    execute_action(act)

#3
def repeat_execution(action, twice):
    if twice:
        execute_action(action)
        execute_action(action)
    else:
        execute_action(action)


repeat_execution(actions[0], True)
repeat_execution(actions[2], False)
repeat_execution(actions[4], True)


#4
def select_action(action):
    global actions
    if(action in actions):
        return action()


#5
menu = {
    "a": attack,
    "d": defend,
    "c": cure,
    "i": inventory,
    "f": flee
}


command = ""

while command != "f":
    command = input("\nSelect command a/d/c/i/f: ").lower().strip()

    if command in menu:
        menu[command]()
    else:
        print("\ninvalid option\n")


################## Lambdas #########################

#1
calcular_dano = {
    "espada": lambda base: base * 1.2,
    "arco": lambda base: base * 1.1,
    "magia": lambda base: base * 1.5
}

ataques = ["espada","arco", "magia"]
dano_base = 40


for ataque in ataques:
    print("Arma:", ataque, "| Dano final:", calcular_dano[ataque](dano_base))



#2
estado = lambda hp: "vivo" if hp > 0 else "morto"
vida = [50, 10, 0, -5]

for v in vida:
    print("HP:", v, "->", estado(v))



#3
def pontuacao(tipo):
    if tipo == "inimigo":
        return lambda x: x * 2
    elif tipo == "chefe":
        return lambda x: x * 5
    elif tipo == "missao":
        return lambda x: x + 100
    else:
        return lambda x: x

acoes = [("inimigo", 50), ("chefe", 100), ("missao", 20), ("objetivo", 10)]

for tipo, valor in acoes:
    resultado = pontuacao(tipo)(valor)
    print("Ação:", tipo, "| Valor base:", valor, "| Pontuação final:", resultado)

