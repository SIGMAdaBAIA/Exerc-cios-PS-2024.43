print("Insira cinco números ")
valor1 = float(input(": "))


maior = menor = valor1
posicao_maior = posicao_menor = 1

for i in range(2,6):
    valor = float(input(": "))
    if valor > maior:
        maior = valor
        posicao_maior = i
    if valor < menor:
        menor = valor
        posicao_menor = i


print("O maior valor é ",(maior)," e está na posição ",(posicao_maior))
print("O menor valor é" ,(menor) ,"e está na posição ",(posicao_menor))