matriz = [[0]*5,
          [0]*5,
          [0]*5,
          [0]*5,
          [0]*5]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if [i] == [j]:
            matriz[i][j] = 1
for i in matriz:
    print(i)