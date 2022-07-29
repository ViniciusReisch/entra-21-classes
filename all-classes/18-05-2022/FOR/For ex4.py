a = 0
contador = input("Deseja ver uma tabuada? ")
while contador == "s":
    tabuada = int(input("Tabuada: "))
    for a in range(11):
        print(f"{tabuada} x {a} = {tabuada*a}")
        a += 1
    contador = input("Deseja ver uma tabuada? ")
