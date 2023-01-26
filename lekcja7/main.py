lista = [3, 2, 3, 4,3, 'u', "cde", "d",]
# print(lista[7])
# lista[3] = 'd'
# print(lista)


# tekst = "Hello world"
# print(tekst[0])
# print(lista[6][0], lista[6][1], lista[6][2])
#
#
# print(lista + ['x', 'd'])
# lista = lista + ['x', 'd']
# print(lista)
# print(lista * 3)
# print("Ilość elementów w liście:", len(lista))

lista.append("f")
lista.append(['u', 'j'])
print(lista[9][1])

lista.insert(3, 'gdzie chce wstawic')
print(lista)

print("Ilość wystąpień danego elementu:", lista.count('u'))
print("Na ktorym indeksie wystepuje dany element:", lista.index(['u', 'j']))

print(lista)


lista2 = [1, 20, -34, 21, -5, 0]
print("Min: ", min(lista2))
print("Max: ", max(lista2))
lista2.reverse()
lista2.sort()
lista2.clear()
print(lista2)





