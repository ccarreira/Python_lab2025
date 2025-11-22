#call_stack

from collections import deque

stack_numeros = deque()

lista_numeros = input().split()

for n in lista_numeros:
    stack_numeros.append(int(n))

print(stack_numeros)

for _ in range(len(stack_numeros)):
    num = stack_numeros.pop()
    print(num*2)