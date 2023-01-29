print(" rozdzielacz ".join(["a", "b", "c"]))
print("Witaj Świecie, Witaj".replace("Witaj", "Cześć"))
print("To jest zdanie".startswith("To"))
# startswith sprawdza czy sie zaczyna z tym co damy jako arg

print("To jest zdanie.".endswith("zdanie."))
print("j" in "To jest zdanie.") # sprawdza czy jest j w stringu

print("To jest zdanie".upper())
print("TO JEST ZDANIE".lower())

lista = [10, 20, 25, 36, 40]

if all([i % 2 == 0 for i in lista]):
    print("Wszystkie parzyste")
else:
    print("Nie wszystkie parzyste")

if any([i % 2 != 0 for i in lista]):
    print("Nie wszystkie parzyste")
else:
    print("Wszystkie parzyste")

for i in enumerate(lista):
    print(i[0] + 1 ,"-", i[1])
