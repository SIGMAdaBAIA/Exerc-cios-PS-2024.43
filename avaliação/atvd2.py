print("Informe 3 números.")
v1 = int(input(": "))
v2 = int(input(": "))
v3 = int(input(": "))

if v1<v2>v3 and v1>v3:
    print("maior:",v2,"menor:",v3)
elif v3<v2>v1 and v3>v1:
    print("maior:",v2,"menor:",v1)
elif v1<v3>v2 and v2>v1:
    print("maior:",v3,"menor:",v1)
elif v2<v3>v1 and v1>v2:
    print("maior:",v3,"menor:",v2)
elif v2<v1>v3 and v2>v3:
    print("maior:",v1,"menor:",v3)
elif v2<v1>v3 and v3>v2:
    print("maior:",v1,"menor:",v2)