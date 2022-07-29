from random import randint, choice
num = int(input("Qual o número de times: "))
times = []
while len(times) != num:
    times.append((input("Escreva o nome do time: ")))
duplas = []
for i in times:
    for j in times:
        if i == j:
            continue
        duplas.append([i, j])
        print(f"{i} x {j}")
jogo = choice(duplas)
placar = []
for i in jogo:
    placar.append(randint(0, 10))
for i in jogo:
    if placar[jogo.index(i)] == min(placar) and placar[jogo.index(i)] == max(placar):
        vencedor = "Empate"
    elif placar[jogo.index(i)] == max(placar):
        vencedor = i
print(f"{jogo[0]} [ {placar[0]} ] x [ {placar[1]} ] {jogo[1]}")
print("Vencedor: ", vencedor)