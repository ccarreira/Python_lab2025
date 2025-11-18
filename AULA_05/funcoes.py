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


execute_fnt = defesa
value = "escudo"

print(execute(execute_fnt, value))

#2
actions=[ataque, defesa, cura, abrir_inventario, fugir]

for a in actions:
    print(execute(a, ""))


#3

def execute_n(action, nTimes=1):
    for n in range(nTimes):
        print(execute(action))

execute_n(ataque, 3)