lista1 = list(range(5,11))
print(lista1)
lista2 = [1, 3, 5, 7, 9, 1]
set1 = set(lista1)
set2 = set(lista2)
if len(lista2) == len(set2):
    print("Sem duplicadas")
else:
    print('tem duplicadas')
print(set1,set2)

set3 = {4, 5, 6, 7, 9}
print(type(set3))

print(f"Union {set2.union(set1)}")
print(f"Intersection {set2.intersection(set1)}")
print(f"Difference {set2.difference(set1)}")
print(f"Difference {set1.difference(set2)}")
print(f"Symmetric Diference{set2.symmetric_difference(set1)}")

if 9 in set2:
    print("Encontrei")
set2.add(23)
tupla = (123,31245,5345,32,3)
lista3 = [123,32,3,24535,4324]
set2.update(tupla)
print(set2)
set2.update(lista3)
print(set2)
set2.remove(123)
print(set2)
set2.discard(2312423)
print(set2)
set2.pop()
print(set2)
for i in set2:
    print(i)
set2.clear()
print(set2)