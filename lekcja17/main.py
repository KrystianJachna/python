krotka = (2, 4, 8, 16, 32, 64, 128)
# w krotce nie możemy modifikować elementów
#print(krotka[0])
print(krotka)

# print("Elementów: ", krotka.count(1)) # ilosc 1dynek
# print("Index: ", krotka.index(64))

print("\nWycinki: ")
print(krotka[0:3])
# dziala dla tablic i slowinkow(?)
# robimy subarray ar[od:do)]

print(krotka[3:5])
print(krotka[3:1000])   # nie powoduje bledu
print(krotka[-4:-2])    # liczmy od konca
print(krotka[0:7:2])    # co który element chcemy brac
print(krotka[2:])       # czyli do konca
print(krotka[:4])       # czyli od poczatku
print(krotka[::-1])     # odwrotna kolejnosc



