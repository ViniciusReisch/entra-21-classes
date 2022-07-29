nome = input("Qual o nome.txt do jogador? ")
partidas = int(input("Quantas partidas ele jogou? "))
dic = {"Nome:": nome,
       'Partidas:': partidas}
for i in range(1, partidas+1):
    gol = int(input(f"Quantos gols o jogador fez na partida {i}? "))
    dic[f'Partida {i}'] = gol
print(dic)
