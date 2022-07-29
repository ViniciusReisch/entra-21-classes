from lista4 import Bomba_Combustivel

bomba = Bomba_Combustivel(tipo_combustivel=input('Tipo de combustivel: '),
                          valor_litro=float(input('Valor do litro de combustivel: ')),
                          quantidade_Combustivel=float(input('Quantidade de combustivel na bomba: ')))
while True:
    x = int(input('Bomba'
                  '\n[1] Abastecer por valor '
                  '\n[2] Abastecer por litros '
                  '\n[3] Alterar valor por litro'
                  '\n[4] Alterar quantidade na bomba'
                  '\n[5] Alterar tipo de combustivel'))
    if x == 1:
        bomba.abastecer_Por_Valor(valor=float(input('Valor que deseja abastecer: ')))
    elif x == 2:
        bomba.abastecer_Por_Litros(litros=float(input('Quantos litros deseja colocar: ')))
    elif x == 3:
        bomba.alterar_Valor(new_valor=float(input('Novo valor: ')))
    elif x == 4:
        bomba.quantidade_Bomba(new_valor=float(input('Nova quantidade: ')))
    elif x == 5:
        bomba.alterar_Combustivel(new_valor=float(input('Novo tipo de combustivel: ')))
