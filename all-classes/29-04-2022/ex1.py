x = int(input("Selecione a temperatura para conversão: \n1.Celsius \n2.Kelvin \n3.Fahrenheit"))

if x == 1:
    temp = int(input("Insira a temperatura em celsius: "))
elif x == 2:
    temp = int(input("Insira a temperatura em kelvin: "))
elif x == 3:
    temp = int(input("Insira a temperatura em fahrenheit: "))

y = int(input("Selecione a temperatura para conversão: \n1.Celsius \n2.Kelvin \n3.Fahrenheit"))

if x == 1 and y == 2:
    print(f'Valor em Kelvin igual a {temp + 273.15}')
elif x == 1 and y == 3:
    print(f'Valor em Fahrenheit igual a {temp * 1.8 + 32}')


elif x == 2 and y == 1:
    print(f'Valor em Celsius é igual a {temp - 273.15}')
elif x == 2 and y == 3:
    print(f'Valor em Fahrenheit é igual a {(temp+273.15) * 1.8 + 32}')


elif x == 3 and y == 2:
    print(f'Valor em Celsius igual a {(temp-32) * 1.8}')
elif x == 3 and y == 2:
    print(f'Valor em Kelvin igual a {(temp+459,67) * 5 / 9}')

