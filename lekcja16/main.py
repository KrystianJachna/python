slownik = {1: "Poniedziałek",
           2: "Wtorek",
           7: "Niedziela"}
# slownik to kolejna kolekcja w ktorej mamy zbior uporzadkowanych par
# klucz: wartosc

slownik[3] = "Środa"
slownik[4] = False
slownik[5] = 5
slownik["a"] = 1
slownik["abc"] = ['a', 'b', 'c']
print(slownik)
print(slownik[7])
print(slownik["a"])

#print(slownik[8])
print(slownik.get(8, "Inny dzień"))
# zwraca druga wartosc jesli nie ma pierwszej

print("\nPętla: ")
for l in slownik.values():
    print(l)
#for l in slownik.keys():

print(slownik.pop(1))       # usuwanie  elementow
print(slownik)