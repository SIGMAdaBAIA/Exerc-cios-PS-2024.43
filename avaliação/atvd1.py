print("Informe seu sexo abaixo.")
sexo = input(": ")

print("Informe sua altura em metros.")
altura = float(input(": "))

match sexo:
    case "m":
        if altura>=1.70:
           print("Apto")
        elif altura<1.69:
             print("Não apto")
    case "f":
        if altura>=1.60:
            print("Apto")
        elif altura<1.59:
             print("Não apto")
