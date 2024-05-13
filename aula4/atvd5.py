print("Informe 3 números.")
v1 = int(input(": "))
v2 = int(input(": "))
v3 = int(input(": "))

if v1>v2>v3:
    print(v3,v2,v1)
elif v1>v3>v2:
    print(v2,v3,v1)
elif v2>v1>v3:
    print(v3,v1,v2)
elif v2>v3>v1:
    print(v1,v3,v2,)
elif v2>v1>v3:
    print(v3,v1,v2)
elif v3>v2>v1:
    print(v1,v2,v3)