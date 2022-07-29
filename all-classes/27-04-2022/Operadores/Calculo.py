nome = input("Escreva seu nome: ")
sobrenome = input("Escreva seu sobrenome: ")
cor = input("Escreva sua cor favorita: ")
iniciocep = input("Digite a primeira parte do seu cep: ")
fimcep = input("Digite a segunda parte do seu cep")
idade = input("Digite a sua idade: ")

cpf = input("Digite 2 digitos do CNPJ de onde você trabalha: ")
cpf1 = input("Digite 3 digitos do CNPJ de onde você trabalha: ")
cpf2 = input("Digite 3 digitos do CNPJ de onde você trabalha: ")
cpf3 = input("Digite 4 digitos do CNPJ de onde você trabalha: ")
cpf4 = input("Digite 2 digitos do CNPJ de onde você trabalha: ")

print(nome, sobrenome, "\n" + cor + "\n" + idade, "anos de idade")
print("CEP:", iniciocep, end="-")
print(fimcep)
print(cpf, cpf1, cpf2, sep=".", end="/")
print(cpf3, cpf4, sep=".")

CEP = iniciocep+"-"+fimcep
CNPJ = cpf+"."+cpf1+"."+cpf2+"/"+cpf3+"."+cpf4
nomecom = nome+ " " + sobrenome

print(nomecom.upper(), "tem", idade, "anos de idade")
print(cor + "\n" + idade, "anos de idade" + "\n" + CEP + "\n" + CNPJ)