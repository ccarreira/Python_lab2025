#queue_process

from collections import deque

queue_palavras = deque()

lista_palavras = input().split()

for p in lista_palavras:
    queue_palavras.appendleft(p)

print(queue_palavras)

for _ in range(len(queue_palavras)):
    palavra = queue_palavras.pop()
    if "a" in palavra: print(palavra)