from random import randint

los = randint(1, 1000)
odp = -1
i = 0

print("Zgadnij liczbe z przedzialu 1 - 1000")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))

    if odp < los:
        print("Za mało!")
    elif odp > los:
        print("Za dużo!")
    else:
        break

print("Brawo udało Ci się w", i, "próbach!!!")
