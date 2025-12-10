
"""Uma função é um bloco de código que só é executado quando invocado"""
"""Um dicionário é uma estrutura de dados que associa um valor a outro"""
"""Um set é um agregado de elementos únicos, não ordenados"""
"""Lambdas São também chamados de “funções anónimas” ou “closures”"""
"""Módulos são uma forma de organizar e agrupar código Python"""

"""Herança não serve para criar coisas diferentes. Serve para organizar, reutilizar e especializar funcionalidade"""
"""Polimorfismo é a capacidade de um mesmo objecto ser tratado como vários tipos diferentes."""

"""Serializar significa converter uma estrutra de dados num formato linear e “guardável” em JSON
Desserializar significa o processo inverso, converter um ficheiro JSON numa estrutura de dados em Python"""

"""Excepções permitem separar o código que gere os erros do código que executa normalmente, o que pode fazer o
código ficar mais limpo e fácil de ler"""

"""
Asserções são ferramentas importantes de debugging
permite parar um programa quando um situação que não deveria acontecer, de facto acontece
"""
# ************* FUNCOES

"""
A chamada de uma função também se pode chamar invocação
• Invocar uma função = Executar o código da função
• Funções servem para agregar código e funcionalidade com:
• Melhor leitura
• Mais modularidade
• Mais reaproveitamento de código
• Menos erros
"""

"""Tipos primitivos são passados por valor:
• Números (inteiros, decimais e complexos)
• Strings
• Booleanos
• Tuplos 
Não podem ser alterados pela função
Podem ser alterados pela função
• Tipos complexos são passados por referência:
• Arrays/Listas
• Dicionários
• Objectos...
"""


# ************* STRINGS

"""string = "\"Yes!\", he said."
string = "abcdefgh ijklmnmm"
print(string)
print(string.replace("mn", "xyz"))
print(string.upper())
print(string.lower())
print(string.index("c"))
print(string.count("m"))
print(string.split(" "))
print(string.strip())"""

# ************* DICT

"""test_dic = {}
test_dic[(1,2)] = "Posição (1,2)"
test_dic[(3,4)] = "Posição (3,4)"
test_dic[(5,6)] = "Posição (5,6)"
print(test_dic)"""


"""games = {
    "God Of War" : {
        "release" : 2018, 
        "genre": "Action"} ,
    "Super Mario Bros" : {
        "release" : 1985, 
        "genre": "Platformer" },
    "Asteroids" : {
        "release" : 1979, 
        "genre": "Arcade"
    }
}
for name, details in games.items():
    print(name)
    for key, value in details.items():
        print(key, "=", value)"""


"""release_year = { }
release_year["God of War"] = 2018
release_year["Subnautica"] = 2018
release_year["Asteroids"] = 1979
release_year["Super Mario Bros"] = 1985
for year in release_year.keys():
   print("keys", str(year))
for year in release_year.values():
   print("values",str(year))
for year in release_year.items():
   print("items",str(year))
for year in release_year:
   print("_", str(year))"""


# ************* SETS

#a = { 1, 2, 3 }
"""a = set()
a.add(1)
print(a)
a.add(3)
print(a)
a.add(4)
print(a)
if (3 in a): a.remove(3)
print(a)
"""


# LAMBDAS

"""square = lambda value : value ** 2
print("lambda result:", square(2))

test = lambda value : True if value % 2 == 0 else False
print(test(2))"""

# STACKS


"""
Stacks:
• LIFO → Last In, First Out
• Normalmente tem duas funções → push e pop
Queues:
• FIFO → First In, First Out
• Normalmente tem duas funções → Enqueue e dequeue"""


from collections import deque

"""
stack = deque()
stack.append(5)
stack.append("abc")
print(stack)
value = stack.pop()
print("Removed", value, "from the stack")
print(stack)"""



"""queue = deque()
print(queue)
queue.appendleft(5)
print(queue)
queue.appendleft("abc")
print(queue)

value = queue.pop()
print("Removed " + str(value) + " from queue")
print(queue)"""


# RANDOM

"""import random
random.seed(4)


value = random.uniform(0,1)
print(value)

choices = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
value = random.choice(choices)
print(value)"""



# HERANCAS, POLIMORFISMO

"""class carro():
    
    name = "Carro Normal"

    def faz_barulho(self):
        print("RRRRRRRRR")
    
    def show_name(self):
        print(self.name)

class ferrari(carro):
    
    name = "Ferrari"

    def faz_barulho(self):    
        super().faz_barulho()    
        print("BRAAAAAAAAM")

class mercedes(carro):

    name = "Mercedes"

    def faz_barulho(self):    
        super().faz_barulho()    
        print("MROOOOM")

carros = [ferrari(), mercedes()]

for c in carros:
    c.show_name()
    c.faz_barulho()"""



# FILES
import os
#os.chdir(r"/Users/cesarcarreira/Documents/VIDEOGAMES_AULAS/FP/Python_lab2025/AULA_07T")
os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\AULA_07T")

"""file = open("dialogos.txt", "rt")
all_lines = file.readlines()
for line in all_lines:
    print(line.strip())
    file.close()"""


file = open("dialogos.txt", "rt")
first_line = file.readline()
first_line_no_punctuation = first_line.replace(".", "").replace(",", "")
first_line_list = first_line_no_punctuation.split(" ")
first_line_caps = first_line.upper()
print(first_line)
print(first_line_no_punctuation)
print(first_line_list)
print(first_line_caps)
file.close()