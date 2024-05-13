login = input("Imforme seu login: ")
senha = input("Informe sua senha: ")

while senha == login:
    print("Senha invalida.")
    senha = input("Informe sua senha novamente: ")

print("Parabéns. Perfil registrado com sucesso")