tempo = 0
massa = float(input("Massa: "))
while massa >= 0.5:
    massa = massa / 2
    tempo += 50
print(f"Vai demorar um total de {tempo} segundos ou {tempo / 60} minutos ou {tempo /60/60} horas")