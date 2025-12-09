"""
1. EQUAÇÃO DO 2.º GRAU
Desenvolva um programa que calcule as raízes de uma equação do 2.º grau 
na forma ax² + bx + c = 0. 
Recorde que o discriminante é Δ = b² – 4ac, 
e que as raízes são: r = (–b ± √ Δ ) / (2a).
"""
import math

def delta(a,b,c):
    return (b**2) - (4*a*c)  

def raizes(a,b,c):
    d = delta(a, b, c)
    if d < 0:
        print("sem raízes reais")
        return None

    if d == 0:
        r = -b / (2*a)
        return (r, r)

    raiz_delta = math.sqrt(d)
    r1 = (-b + raiz_delta) / (2*a)
    r2 = (-b - raiz_delta) / (2*a)
    return (r1, r2)

#print(raizes(0,0,0))

"""
2. DISTÂNCIA ENTRE DOIS PONTOS EM 3D
Leia as coordenadas de dois pontos no espaço tridimensional 
e calcule a distância entre eles.
"""

v1 = (4,4)
v2 = (4,3)

dist = math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)

#print(dist)
#d=raizquadrada( (x2​−x1​)^2+(y2​−y1​)^2)

"""
3. VALOR TOTAL DE PRODUTOS COM DESCONTO
Para cada produto informado (nome, preço e quantidade), 
apresente o nome e o valor total após aplicar o 
desconto:
•Até 10 unidades: sem desconto
•11 a 20 unidades: 10%
•21 a 50 unidades: 20%
•Mais de 50 unidades: 25%
"""

class produto():
    nome = ""
    preco = 0

    def __init__(self, nome="", preco=0):
        self.nome = nome
        self.preco = preco

def get_desconto(quantidade):
    if quantidade > 50: return 0.25
    elif quantidade > 20: return 0.20
    elif quantidade > 10: return 0.10
    else: return 0 

def get_preco(produto):
    for p in DB:
        if p.nome == produto:
            return p.preco
    print("produto nao encontrado")
    return 0

def prod_exist(produto):
    for p in DB:
        if p.nome == produto:
            return True
    return False
    
def comprar(produto, quantidade):
    try:
        if not prod_exist("produto"): 
            print("Produto inexistente")
            raise ValueError
    except ValueError:
        pass
    preco_base = get_preco(produto)
    desconto = get_desconto(quantidade)
    preco_final = preco_base - (preco_base * desconto)
    print(produto, ": x", quantidade, " custa ", preco_final)
    return preco_final


DB = []
DB.append(produto("camisola", 100))
DB.append(produto("calças", 300))
DB.append(produto("sapatos", 400))

#print(comprar("camisola", 4))


"""
4. TABELA DE MULTIPLICAÇÃO
Construa e apresente a tabela de multiplicação dos números de 1 a 10.
"""

for n1 in range(1,11):
    for n2 in range(1,11):
        pass
        #print(n1, "x", n2, "=", n1*n2)



"""
5. SÉRIE DE FIBONACCI
Leia um número inteiro não negativo e apresente os 
primeiros n termos da sequência de Fibonacci.
"""

num = int(input("coloque numero inteiro positivo: "))

def fibonacci(num):
    a, b = 0, 1
    seq = []

    for _ in range(num):
        seq.append(a)
        a, b = b, a + b

    return seq

print(fibonacci(num))

"""
6. JOGO DO GALO – MELHOR JOGADA
Leia uma matriz 3×3 representando um tabuleiro e indique a jogada que permite ganhar ou, caso não seja 
possível, evitar perder.
7. ORDENAÇÃO DE UM VETOR
Gere automaticamente um vetor com 100 números inteiros e ordene-o.
8. COMBINAÇÃO DE DOIS VETORES ORDENADOS
Crie dois vetores de 50 posições com valores aleatórios, ordene-os e combine-os num vetor de 100 posições 
já ordenado.
9. MÉDIA E ESTATUTO DO ALUNO
Crie um método que calcule a média final e outro que indique o estatuto do aluno:
•Nota > 10   Aprovado→
•Nota 4–6   Verificação Suplementar→
•Nota < 4   Reprovado→
10. CONVERSÃO DE SEGUNDOS PARA HORAS, MINUTOS E SEGUNDOS
Leia um tempo em segundos e apresente-o em horas, minutos e segundos, usando cinco métodos distintos.
11. NÚMERO DECIMAL PARA NUMERAÇÃO ROMANA
Leia um número até 3 dígitos e escreva o seu equivalente em algarismos romanos, usando métodos e vetores 
de conversão.
12. NÚMEROS POR EXTENSO ATÉ 9 DÍGITOS
Leia um número inteiro de até 9 dígitos e escreva-o por extenso usando métodos e vetores de strings.
13. SISTEMA DE GESTÃO DE PEDIDOS DO SUPERMERCADO
Identifique as classes e implemente um programa que modele produtos, pedidos, itens e formas de 
pagamento (dinheiro, cheque, cartão).
14. AGENDA TELEFÓNICA
Implemente um programa com as classes Agenda e Contacto, permitindo registar e gerir contactos.
"""