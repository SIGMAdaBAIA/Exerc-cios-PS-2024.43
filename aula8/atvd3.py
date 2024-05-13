nome = input("Informe seu nome: ")
while len(nome)<=2:
    print("invalido")
    nome = input("Informe seu nome novamente: ")

idade = int(input("Informe sua idade: "))
while idade<0 or idade>120:
    print("Invalido")
    idade = int(input("Informe sua idade novamente: "))

salário = int(input("Informe seu sálario: "))
while salário<=0:
    print("Invalido")
    salário = int(input("Informe seu nome: "))

sexo = input("Informe seu sexo: ").upper()
while sexo!="M" and sexo!="F":
    print("Invalido")
    sexo = input("Informe seu sexo: ")

civil = input("Informe seu estado civil: ").upper()
while civil!="S" and  civil!="C" and  civil!="V" and civil!="D":
    print("Invalido")
    civil = input("Informe seu estado civil: ")