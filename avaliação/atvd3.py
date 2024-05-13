print("Escolha a sua conversão:")
print("  ")
print("1. Converter de °C para °F")
print("2. Converter de °F para °C")
conversao = int(input(": "))


if conversao == 1:
    c = int(input("Informe os Celsius: "))
if conversao == 2:
    f = int(input("Informe os Fahrenheit: "))

match conversao:
    case 1:
        print((c*9/5)+32)
    case 2:
        print((f-32)*5/9)