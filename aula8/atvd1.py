nota_1 = float(input("Informe sua nota: "))
while nota_1>10 or nota_1<0:
    print("Nota invalida. Insira novamente")
    nota_1 = float(input("Informe sua nota novamente: "))

nota_2 = float(input("Informe sua nota: "))
while nota_2>10 or nota_2<0:
    print("Nota invalida. Insira novamente")
    nota_2 = float(input("Informe sua nota novamente: "))

media =(nota_1+nota_2)/2
print("Sua média é",media)