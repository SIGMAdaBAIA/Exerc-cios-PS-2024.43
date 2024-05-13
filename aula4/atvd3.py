print("Informe uma das opções abaixo:")
print("1. Fazer Check-in")
print("2. Chamar serviço de quarto")
print("3. Fazer pedido")
print("4. Fazer Check-out")

pergunta = int(input(": "))

match pergunta:
    case 1:
        print("Fazer Check-in")
    case 2:
        print("Chamar serviço de quarto")
    case 3:
        print("Fazer pedido")
    case 4:
        print("Fazer Check-out")
    case _:
        print("Opção ínvalida")
