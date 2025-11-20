"""
1. Cria um módulo (game_utils.py) com 5 funções: saudação, classe, ataque, dano, 
e vida do inimigo (100)
• Usa inputs no game loop
• player_class = [“warrior”, “mage”, “archer”]
• Dano base (40) com modifier baseado na classe = [1.3, 1.5, 1.2]
2. Nesse game_loop integra um loot system importado do game_utils.py.
• Modifica o game loop para o jogo correr até o jogador saír
• loot = [“sword”, “shield”, “potion”, “armor”, “ring”]
• Quando o jogador derrota um inimigo, recebe um drop e adiciona ao inventário.
• O inventário deve ser mostrado como stack
3. Integra um sistema aleatório de critical damage na função de dano no game_utils.py
• Um critical hit de dobra o dano causado (base damage + class multiplier)
• Existe 20% de possibilidade um critical hit
4. No game_utils.py cria um sistema de geração de diferentes inimigos
• Lista de inimigos = ["Goblin", "Orc", "Troll", “Skeleton"]
• Eles têm força aleatória entre 5 e 20 (random.randint(a,b)→gera ints aleatórias no intervalo
• Vida aleatória entre 30 e 100
5. Finalmente, no game_utils.py, gera um sistema de player health (100) e um sistema de defesa:
• Se ambos atacam, ambos perdem health. Se um ataca e outro defende damage passa a metade.
• Se o inimigo defende um ataque, o player perde a chance de critical hit
• Fazer check do inventário não termina o turno
• O jogo agora deve correr até o jogador morrer ou saír.

"""

import random

"""
saudação, classe, ataque, dano, 
e vida do inimigo (100)
"""

def saudacao():
    pass

def classe():
    pass

def ataque():
    pass

def get_hero_dano(classe):
    dano_base = 40

    damage_multipliers = {
        "warrior" : lambda dano_base : dano_base * 1.3,
        "mage" : lambda dano_base : dano_base * 1.5,
        "archer" : lambda dano_base : dano_base * 1.2
}

def vida_inimigo(enemy, value):
    enemy[2] = value






#4
"""4. No game_utils.py cria um sistema de geração de diferentes inimigos
• Lista de inimigos = ["Goblin", "Orc", "Troll", “Skeleton"]
• Eles têm força aleatória entre 5 e 20 (random.randint(a,b)→gera ints aleatórias no intervalo
• Vida aleatória entre 30 e 100
"""


def gera_inimigo():

    inimigos_lista = ["Goblin", "Orc", "Troll", "Skeleton"]

    tipo = random.choice(inimigos_lista)
    forca = int(random.uniform(5,20))
    vida = int(random.uniform(30,100))

    inimigo = (tipo, forca, vida)

    print(", ".join(str(x) for x in inimigo))

    return inimigo

gera_inimigo()      