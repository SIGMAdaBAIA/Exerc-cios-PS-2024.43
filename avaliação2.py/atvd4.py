matriz = [[0]*3,
          [0]*3,
          [0]*3]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = (i + 1) * (j + 1)

for linha in matriz:
    print(linha)