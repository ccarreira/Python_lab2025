"""
1. Cria um dicionário chamado weapon com as seguintes informações:
• name ->Longsword
• Damage -> 25
• Weight -> 8.5

1. Imprime o nome da arma e o seu dano.

2. Adiciona uma nova chave "durability" com valor 100.
3. Imprime novamente o dicionário completo.
"""

weapon = {
    "Name" : "Longsword", 
    "Damage" : 25, 
    "Weight" : 8.5
     }

print("Nome da arma: ", weapon["Name"], ", Dano: ", weapon["Damage"])

weapon["Durability"] = 100

print(weapon)


"""
2. Cria um dicionário chamado droids com a seguinte informação:
• name ->K-2SO
• Type -> KX
• Stats -> hp = 200, strength = 300, mobility = 50
1. Imprime o valor de hp e mana.
2. Aumenta o hp em 25 e imprime novamente.
3. Mostra todos os detalhes da personagem incluindo stats.
"""

droids = {
    "Name" : "K-2S0",
    "Type" : "KX",
    "Stats" : { "HP" : 200, "Strength" : 300, "Mobility" : 50 } 
    }

print("Name:", droids["Name"])
print("HP:", droids["Stats"]["HP"])

droids["Stats"]["HP"] += 25
print("HP + BONUS:", droids["Stats"]["HP"])

"""
3. Cria um dicionário shop com os seguintes items:
• potion -> price = 10, stock = 5
• elixir -> price = 25, stock = 2
• sword -> price = 100, stock = 1
1. Mostra todos os itens e respetivos preços.
2. Pede ao jogador o nome de um item, e mostra o preço correspondente.
3. se o jogador comprar um item, diminui o valor de "stock".
"""

shop = {
    "Potion" : { "price" : 10, "stock" : 5 },
    "Elixir" : { "price" : 25, "stock" : 2 },
    "Sword" : { "price" : 100, "stock" : 1 }
}

for item, info in shop.items():
    print(item)
    print("Price:", info["price"], "Stock:", info["stock"])

nome_item = input("Nome de item?: ")

if nome_item in shop:
    print("Price:", shop[nome_item]["price"])
    print("Stock:", shop[nome_item]["stock"])
    if shop[nome_item]["stock"] > 0:
        buy = input("Buy? Yes/No :").strip().lower()
        if buy == "y":
            shop[nome_item]["stock"] -= 1
            print("Compra Efectuada")
            print("Price:", shop[nome_item]["price"])
            print("Stock:", shop[nome_item]["stock"])
    else:
        print("Sem stock")
else:
    print("Item not found")

