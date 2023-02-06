liczby = [2, 10, 12, 15, 20, 25, 30, 35]

# Funkcja mapy - iteruje po liscie i wykonuje operacje
# takie jak zadamy w funkcji

def funkcja(x):
    return x * 2


wynik = map(funkcja, liczby)
print(list(wynik))

wynik2 = map(lambda x: x * 2, liczby)
print(list(wynik2))


# Filtry - wybiera te ktore spelniaja warunki

wynik3 = filter(lambda x: x % 2 == 0, liczby)
print(list(wynik3))