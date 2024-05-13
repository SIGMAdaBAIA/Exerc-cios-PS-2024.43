arquivo = int(input("informe o tamanho do arquivo em (B): "))
internet = int(input("informe a velocidade da sua internet em (bps): "))

conversao = arquivo*8
dowanload = conversao*internet
minutos = dowanload/60

print("O download ira demora",minutos,"minutos")