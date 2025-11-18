


"""

evaluation = lambda grade: "passed" if grade >= 9.5 else "failed"

clientes = [("none", 100), ("normal", 100), ("premium", 100), ("vip", 100)]
      def desconto(tipo):
          if tipo == "normal":
              return lambda valor: valor * 0.95
          elif tipo == "premium":
return lambda valor: valor * 0.90 elif tipo == "vip":
              return lambda valor: valor * 0.80
          else:
              return lambda valor: valor
for tipo, preco in clientes:
print("Cliente:", tipo, "| Valor final:", desconto(tipo)(preco))

"""

"""
Cria um dicionário de lambdas que calcula o dano final de acordo com o tipo de ataque.
• Variável → dano_base = 40
• Todas as armas têm um multiplier. Espada (1.2), Arco (1.1), Magia (1.5)

2. Cria um lambda que receba os pontos de vida e devolva "vivo" se forem maiores que 0, ou "morto" caso contrário.
• Lista: vida = [50, 10, 0, -5]
3. Cria uma função pontuacao(tipo) que devolve uma lambda diferente dependendo do tipo de evento.
• Usa essa função para calcular pontuação
• Usa uma lista de tuplos para as acções e valores: acoes = [("inimigo", 50), ("chefe", 100), ("missao", 20)]
• Cada lambda tem também pontuação extra -> Inimigo *2; Chefe *5, Missão +100; Outro + 0.
• Imprime a pontução final
"""

average_mult = lambda dano_base : dano_base * 1.2
low_mult = lambda dano_base : dano_base * 1.1
high_mult = lambda dano_base : dano_base * 1.5

weapon_multipliers = {
    "espada" : average_mult,
    "arco" : low_mult,
    "magia" : high_mult
}

def attack(weapon, damage):
    if weapon in weapon_multipliers:
        final_damage = weapon_multipliers[weapon](damage)
        print("damage: ", final_damage)


attack("magia", int(100))