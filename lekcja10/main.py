def funkcja_test():
    print("Funkcja!")


def inkrementuj(x):
    print(x+1)


#funkcja_test()
#inkrementuj(3)


def dodaj(x, y=1, z=0):    # tylko tak mozna przeciazac
    return x + y + z

def zwracanie_tablicy(x, y=1, z=0):    # tylko tak mozna przeciazac
    return [x, y, z]

print(dodaj(3, 5))
print(dodaj(3))
wynik = dodaj(2, 3, 5)
print(wynik)

x = zwracanie_tablicy(1)[2]
print(x, "xd")  # ciekawe


