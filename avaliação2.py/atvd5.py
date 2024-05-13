matriz_1 = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]

matriz_2 = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]

maior1 = 0

for i in range(len(matriz_1)):
    for j in range(len(matriz_1)):
       if matriz_1[i]> maior1:
            maior1 = matriz_1[i]

print (maior1)