vetor = []
print("Informe 10 números")
for i in range(10):
    valor = int(input(": "))
    vetor.append(valor)

indice = 0
while indice < len(vetor):
    if vetor[indice] == 0: 
        vetor.pop(indice)
    else:
        indice += 1

print(vetor)