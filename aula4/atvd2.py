sexo = input("Informe seu sexo: ")

match sexo:
    case "m":
        print("Masculino")
    case "f":
        print("Feminino")
    case _:
        print("Sexo não definido")