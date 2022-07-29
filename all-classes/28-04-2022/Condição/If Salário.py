salario = float(input("Escreva seu sálario"))
nome = input("Escreva seu Nome: ")
cargo = input("Escreva seu Cargo: ")

if salario > 5000:
    salario1 = salario * 1.05
    aumento = "5%"
    val = salario1 - salario
elif salario > 3000:
    salario1 = salario * 1.07
    aumento = "7%"
    val = salario1 - salario
elif salario < 3000:
    salario1 = salario * 1.10
    aumento = "10%"
    val = salario1 - salario

print(f'Nome: {nome} \n Cargo: {cargo} \n salario antigo: {salario} \n salario novo: {salario1} \n aumento aplicado: {aumento} \n valor do aumento: {val}')
