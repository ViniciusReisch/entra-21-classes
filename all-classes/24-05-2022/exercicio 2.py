nomes = []
somaCarlos = 0
nome = None
while nome != "fim":
    nome = input("Escreva um nome: ").lower()
    nomes.append(nome)
nomes.sort()
print(f"crescente {nomes}")
nomes.sort(reverse=True)
print(f"decrescente {nomes}")
print(f'Foram registrados o total de {len(nomes)} nomes')
print(f'Tem {nomes.count("carlos")} Carlos na lista')