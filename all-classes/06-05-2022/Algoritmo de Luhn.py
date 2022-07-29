cartao = input("Digite o número de seu cartão: ")
cartao = ' '.join(filter(str.isalnum, cartao))
cartao = cartao.split()
bandeiras = [" ",  " ", " ", "American Express e Diners Club","Visa", "MasterCard","Discover Card"]
cont = 0
m1 = len(cartao) // 2
m2 = len(cartao) - m1
print(m1)
print(m2)
a = 0
c = 0
soma = 0
ct = 0

while cont < m1:
    c = int(cartao[a]) * 2
    if c > 9:
        c -= 9
    a += 2
    cont += 1
    soma += c
cont = 0
a = 1

while cont < m2:
    ct += int(cartao[a])
    cont += 1
    a += 2
soma = soma + ct
soma = soma%10

if soma == 0:
    print("Cartão valido")
else:
    print("Cartão inválido")
t = int(cartao[0])
print(f"Sua bandeira é {bandeiras[t]}")