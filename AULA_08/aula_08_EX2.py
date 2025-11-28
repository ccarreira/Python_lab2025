"""
Itens e Inventário com limite duplo
• Cria uma classe Item com:
• name, weight, value
• Construtor recebe estes três parâmetros.
• Cria uma classe Inventory com:
Exemplo de execução
  • max_items (número máximo de itens), max_weight (peso máximo total), items (lista de Item, começa vazia)
• Métodos de Inventory:
• total_weight() → devolve a soma dos pesos de todos os itens
• total_value() → devolve a soma dos valores de todos os itens
• can_add(item) → devolve True se não exceder nem o número máximo de itens
nem o peso máximo total
• add_item(item) → se can_add(item) for True, adiciona o item; caso contrário,
imprime "Cannot add <nome>: inventory limit reached“
• Programa principal:
1. Cria um inventário com max_items = 4 e max_weight = 15.
2. Cria pelo menos 5 itens diferentes (espada, escudo, poção, ouro, armadura, etc.).
3. Usa o random para teres 3 objectos para escolher e input para apanhares 1 deles.
4. O while corre até o player atingir um dos limites ou fizer quit
5. No fim, imprime todos os nomes dos items no inventário e total_weight() e total_value().
"""