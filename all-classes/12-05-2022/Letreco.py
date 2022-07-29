contador = 0
palavraFinal = list("teste")
while contador < 5:
    i = 0
    palavra = list(input(""))
    if len(palavra) != 5:
        print("Palavra Invalida")
    else:
        while i < len(palavra):
            letraPalavraDigitada = palavraFinal[i]
            letraPalavraCerta = palavra[i]
            verificação = letraPalavraCerta in palavraFinal
            i += 1
            if letraPalavraCerta == letraPalavraDigitada:
                print(f"\033[1;42m{letraPalavraCerta}", end="")
            elif verificação == True:
                print(f"\033[1;41m{letraPalavraCerta}", end="")
            elif letraPalavraCerta != letraPalavraDigitada:
                print(f"\033[1;40m{letraPalavraCerta}", end="")
    contador +=1

