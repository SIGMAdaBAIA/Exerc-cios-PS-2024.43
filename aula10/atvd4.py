matriz = [[0,0,0,],
          [0,0,0,],
          [0,0,0,]]

maior = 0
linha = 0
coluna = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = (int(input("Esvreva 9 números: ")))
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j
print("O maior número e",maior,"Ele esta na posição",linha,coluna)