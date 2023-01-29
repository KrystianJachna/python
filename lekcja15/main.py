plik = open("test.txt", "a")
# można podać ścieżkę do pliku
# jeśli ścieżki nie ma to domyslnie jest folder z kodem
# jesli pliku nie ma to zostanie wygenerowany

# "w" - pisanie z kasowaniem co bylo wczeniej
# "r" - czynie
# "w+" - pisanie od 0 bajta i czytanie
# "a" - dolączanie czyli pisanie do tego co bylo

# print(plik.writable())
# zwraca prawde jesli plik otwarty jest
# w trybie do zapisu
# falsz jesli w trybie do odczytu


# wpisywanie do pliku
if plik.writable():
    ile = plik.write(input("Wprowadź tekst do pliku: ") + "\n")
    print("Zapisano znaków: ", ile)
plik.close()

# czytanie calości
plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku: ")
    tekst = plik.read() # czyta calosc
    print(tekst)
plik.close()


# czytanie linijek i zapisywanie do listy
plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku: ")
    tekst = plik.readlines() # zapisuje do listy
    print(tekst)
    for i in tekst:
        print(i)
plik.close()


# iterowanie po slowach w pliku
plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku: ")
    for line in plik:
        print(line)
plik.close()


