"""

1. Cria um sistema que executa as ações: ataque, defesa, cura, 
abrir inventário e fugir. • Usa uma função para gerir as ações.
2. Usa uma lista actions = [] para guardar as funções executá-las como 
no código do exercício anterior
3. Define uma função que executa a mesma acção duas vezes 
usando o código do exercício anterior
4. Cria uma função que, conforme parametro recebido retorna uma função diferente. Depois, chama a função de return
5. Usando um dicionário. Cria um menu para executar o código todo do exercício usando input do jogador.
• Verifica se a opção existe
• Usa funções de string para limpar o input

"""

def ataque(value="object"):
    return("ataque com "+value)
def defesa(value="object"):
    return("defesa com "+value)
def cura(value="object"):
    return("cura com "+value)
def abrir_inventario(value="object"):
    return("abrir inventario "+value)
def fugir(value="object"):
    return("fugir de "+value)


def execute(fnt, value="None"):
    return(fnt(value))
    #for v in values: 


action = defesa
value = "escudo"

print(execute(action, value))

#2
actions=[ataque, defesa, cura, abrir_inventario, fugir]

for a in actions:
    print(execute(a, "escudo"))


#3

def execute_n(action, value, nTimes=1):
    for n in range(nTimes):
        print(execute(action, value))

execute_n(ataque, "espada", 2)

#4

def attack():
    return "ataca"
def defend():
    return "defende"
def rest():
    return "descansa"

dicionario_de_acoes = {
    "ataque" : attack,
    "defesa" : defend,
    "descansa": rest
}


def do(action):
    print(dicionario_de_acoes[action]())

do("ataque")


#5

dicionario_de_acoes = {
    "ataque" : ataque,
    "defesa" : defesa,
    "cura": cura,
    "inventario" : abrir_inventario,
    "fugir" : fugir,
}


def execute2(action, value="None"):
    action = str(action)
    if action in dicionario_de_acoes:
        print("RESULTADO #5: " + dicionario_de_acoes[action](value))
    else:    
        print("Acao desconhecida_execute", action)


comando = False
while not comando:
    action = input("qual a acao? : ").strip().lower()
    if action in dicionario_de_acoes:
        comando = True
    else:
        print("Acao desconhecida", action)

execute2(action)



