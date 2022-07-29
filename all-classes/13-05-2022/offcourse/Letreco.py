import random
from unidecode import unidecode

arquivo = open('dicionario.txt', "rt", encoding="utf-8")
lines = arquivo.read().split()
dicionario2 = [unidecode(palavra) for palavra in lines]
arquivo.close()
contador = 0
aleatoria = random.randrange(1, 16716)
palavraFinalComAcento = lines[aleatoria]
palavraFinalSemAcento = dicionario2[aleatoria]
while contador < 5:
    i = 0
    palavra = unidecode(input("").lower())
    palavraCertaIndex = dicionario2.index(palavra)
    palavraCerta = dicionario2[palavraCertaIndex]
    palavraCertaComAcento = lines[palavraCertaIndex]
    while palavra not in dicionario2 or len(palavra) != 5:
        print("PALAVRA INVÁLIDA")
        palavra = unidecode(input("").lower())
    else:
        while i < len(palavra):
            letraPalavraFinalSemAcento = palavraFinalSemAcento[i]
            letraPalavraFinalComAcento = palavraFinalComAcento[i]
            letraPalavraCertaSemAcento = palavraCerta[i]
            letraPalavraCertaComAcento = palavraCertaComAcento[i]
            verificação = letraPalavraCertaSemAcento in palavraFinalSemAcento
            i += 1
            if letraPalavraCertaSemAcento == letraPalavraFinalSemAcento:
                print(f"\033[1;42m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
            elif verificação == True:
                print(f"\033[1;41m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
            elif letraPalavraCertaSemAcento != letraPalavraFinalSemAcento:
                print(f"\033[1;40m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
    contador +=1

