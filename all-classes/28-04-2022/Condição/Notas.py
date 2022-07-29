nome = input("Digite seu nome: ")
nota1 = int(input("Digite o primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

nota = ((nota1 + nota2 + nota3 + nota4) / 4)
if nota >= 7:
    print(f'{nome.upper()}, você foi aprovado')
elif nota <= 5:
    print(f'{nome.upper()} você está em exame')
else:
    print(f'{nome.upper()}, você foi reprovado')