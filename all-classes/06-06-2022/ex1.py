def situacao(nota):
    if nota > 7:
        situ = 'APROVADO'
    else:
        situ = 'REPROVADO'
    return situ, nota


aluno = input("Qual o nome do aluno? ")
situ, nota = situacao(float(input("Qual sua nota? ")))
dic1 = {'Aluno': aluno,
        'Nota': nota,
        'Situação': situ}

print(dic1)
