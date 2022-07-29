lista = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
lista += lista2
# extend
# lista.append([2,'a','5',False])
print(lista)




# #
# # append
# # extend
# # insert
# # remove
# # pop
# # clear
# # index
# # count
# # sort
# # reverse
# # copy
# # juntar listas
# # del
#
# # append
# # for i in range(3):
# #     lista.append(input('Digite qualquer coisa'))
# # print(lista)
#
# # extend
# lista.extend([2,'a','5',False])
# print(lista)
#
# # Diferença entre append e extend?
# # Pode agregar 2 outro elemento iterável a lista, como Tupla, ou dicionário
#
# insert - insere um elemento na lista, em qualquer índice definido
lista.insert(0, '14/03/1992')
lista.insert(2, 'jonas')
lista.insert(6, 'a')
lista.insert(6, 'a')
lista[0], lista[1], lista[2] = lista[2],lista[1], lista[0]
print(lista)
#
# remove o primeiro item da lista que seja igual ao valor informado
lista.remove('a')
print(lista)
#
# remove o último índice da lista
lista.pop(0)
print(lista)
#
# lindex
data = lista.index('a')
print(lista[data])
#
# # count
lista.append('q')
print(lista)
print(lista.count('q'))
#
lista.reverse()
print(lista)

# lista3 = [3, 4, 5, 1, 9, 7, 8, 'a']
# lista3.sort()
# print(lista3)
# lista3.sort(reverse=True)
# print(lista3)

# lista.sort(key=float)
# print(lista)
# lista.sort(reverse=True)
# print(lista)
#
# # Reverse
# lista.reverse()
# print(lista)
#
# # limpa a lista
# lista.clear()
# print(lista)
#
# # print(lista)
#
# del lista[:]
#
# ['q', 8, 6, 4, 2, 'a', 7, 5, 3, '14/03/1992', 1]
# desempacotamento de lista
numero, cafe, carro, *valores = lista
print(numero)
print(cafe)
print(carro)
print(valores)
#
#
# # list comprehension
lista2 = [1,4,5,2]
nova_lista2 = [2*valor for valor in lista2]
print(nova_lista2)


lista5 = [1, 3, 5]
nova_lista3 = [3*i for i in lista5]
print(nova_lista3)

# list comprehension parte2
lista3 = [1, 4, 5, 2]
nova_lista4 = [valor for valor in lista3 if valor % 2 == 0]
print(nova_lista4)
# 4 , 2