import random

matriz = []
cols = 4
rows = 4
values =(True, False)

def buid_matrix(rows, cols, matriz):
    for r in range(rows):
        matriz.append([])
        for c in range(cols):
            matriz[r].append(False)
            #matriz[r].append(random.choice(values))
    print(matriz)

buid_matrix(rows, cols, matriz)

def update_matrix(new_value, row, col, matriz):
    matriz[row][col] = new_value
"""    print(matriz[row][col])
    print(matriz)"""

def fill_row(value, row, matriz):
    for c in range(len(matriz[row])):
        matriz[row][c] = value

def fill_col(value, col, matriz):
    for r in range(len(matriz)):
        matriz[r][col] = value

def update(new_value, row, column, matriz):
    if new_value:
        matriz[row][column] = new_value
    print(matriz)

def check_matrix(matriz):
    new_matrix = matriz.copy()
    for r in range(len(matriz)):
         for c in range(len(matriz[r])):
            if matriz[r][c] == True:
                fill_row(True, r, new_matrix)
                fill_col(True, c, new_matrix)
    
    return new_matrix


#fill_row(False, 3, matriz)
#fill_col("RRRRRRRRRR", 3, matriz)

update(True, 2, 2, matriz)
check_matrix(matriz)

#update_matrix("aaaaaaa", 0, 0, matriz)