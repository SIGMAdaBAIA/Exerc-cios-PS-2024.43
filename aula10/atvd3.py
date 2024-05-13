matriz = [[0,0,0,],
          [0,0,0,],
          [0,0,0,]]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = (int(input("Esvreva 9 números: ")))
x = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j]>10:
            x+=1
print(x)