lista = list(range(10))

print("stara: ", lista)

nowa = [i * 2 for i in lista]

print("nowa:  ", nowa)

nowa2 = [i + 2 for i in lista if i % 2 == 0]
# najpierw idziemy forem, sprawdzamy warunek
# jesli element spelnia to jest dodawany do nowej listy
# i na koncu jest wykonywana operacja tutaj i+2

print("nowa2: ", nowa2)

# Formatowanie String

argumenty = ["Krystian", 21]
tekst = "Cześć mam na imię {0} i mam {1} lat.".format(argumenty[0], argumenty[1])
tekst2 = "Cześć mam na imię {imie} i mam {wiek} lat.".format(imie = argumenty[0], wiek = argumenty[1])
print(tekst)
print(tekst2)