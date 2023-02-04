plik = open("wiki.txt", "r")
tekst = plik.read()
plik.close()

def policz(txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik

print(policz(tekst, "a"))
print(policz(tekst.lower(), "a"))


spacje = policz(tekst, " ")
literyTekst = len(tekst) - spacje

for z in "abcdefghijklmnopqrstuvwxyz":
    litera = policz(tekst.lower(), z)
    procent = 100 * litera / literyTekst
    print("{0} - {1} - {2}%".format(z.upper(), litera, round(procent, 2)))