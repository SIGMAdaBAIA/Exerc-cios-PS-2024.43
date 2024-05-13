print("Informe dois números.")
n_1 = int(input(": "))
n_2 = int(input(": "))

print("1. Soma +")
print("2. Soma -")
print("3. Multiplicação *")
print("4. Divisão /")

opções = int(input("informe uma opção"))

match opções:
    case 1:
        print(n_1+n_2)
    case 2:
        print(n_1-n_2)
    case 3:
        print(n_1*n_2)
    case 4:
        print(n_1/n_2)