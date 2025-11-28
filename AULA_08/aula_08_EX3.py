"""
3. Sistema de quests com estados
• Cria uma classe Quest com:
Exemplos de execução
  • Title, description, status (string que pode ser "locked", "active" ou "completed") • Construtor recebe title e description e inicia o status como "locked".
• Métodos:
• unlock() → se status for "locked", passa a "active“
• complete() → se status for "active", passa a "completed“
• log() → imprime título e estado atual
• Programa principal:
• Cria uma lista com 3 Quest:
• Quest("Speak with villagers", "Talk to the people in the village.")
• Quest("Clear dungeon", "Defeat all enemies in the old dungeon.")
• Quest("Defeat area boss", "Kill the boss that controls the region.")
• Usa input para Desbloquear a primeira quest e depois marca-a como completa.
• Quando uma quest ficar "completed", desbloqueia automaticamente a próxima.
• Imprime o estado de todas as quests em três momentos:
• antes de qualquer alteração
• depois de completar uma quest
• No final, imprime o log e sai do loop se todas as quests estiverem
completas ou o input for quit
"""