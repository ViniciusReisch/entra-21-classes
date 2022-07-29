lista = [["1",'2','3'],['4','5','6'],['7','8','9']]
print(f"{lista[0]}\n{lista[1]}\n{lista[2]}")
while True:
    x = input("Posição: ")
    for i in range(3):
        for e in range(3):
            if x == lista[i][e]:
                lista[i][e] = "X"
    print(f"{lista[0]}\n{lista[1]}\n{lista[2]}")
    for i in range(3):
        if lista[i][0] == lista[i][1] == lista[i][2]:
            print("Ganhou")
            break
    x = input("Posição: ")
    for i in range(3):
        for e in range(3):
            if x == lista[i][e]:
                lista[i][e] = "O"
    print(f"{lista[0]}\n{lista[1]}\n{lista[2]}")
    for i in range(3):
        if lista[i][0] == lista[i][1] == lista[i][2]:
            print("Ganhou")
            break

    if x == "t":
        break


print(f"{lista[0]}\n{lista[1]}\n{lista[2]}")


