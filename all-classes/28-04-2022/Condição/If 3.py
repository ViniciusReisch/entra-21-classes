orc = float(input("Escreva o orçamento: "))
gasto = float(input("Escreva o valor gasto: "))

if gasto == orc:
    print("Todo o valor do orçamento foi gasto")
elif gasto > orc:
    print("O valor do gasto é maior que seu orçamento")
else:
    print("O valor do orçamento foi suficiente para o gasto")

    