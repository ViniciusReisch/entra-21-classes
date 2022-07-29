def cafe(xicara, ml):
    metadeXicara = xicara / 2
    if metadeXicara > ml:
        print("Está acabando, encha")
    if ml > xicara:
        print("A xicara transbordou")
    if ml == xicara:
        print("A xicara está cheia")


leite = cafe(int(input("Quantos ml tem sua xicara: ")), int(input("Quantos ml de cafe tem? ")))
