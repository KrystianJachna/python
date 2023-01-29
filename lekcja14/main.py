def dzielenie(x, y):
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0!")
    print(x/y)
# tutaj przewidujemy blad dzielenia przez zero i w razie jego
# wystapienia wyswietlamy wiadomosc

try:
    dzielenie(2, 5)
except ZeroDivisionError:
    print("Błąd")
    raise # program nam wyrzuci jaki to konkretnie blad

def dzielenie2(x, y):
    assert y != 0, "Y == 0"      # zwraca kod bledu jesli warunek jest niespelniony
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0!")
    print(x / y)
# pozwala to wykrywac bledne linijki kodu w wiekszych programach

dzielenie2(1,0)