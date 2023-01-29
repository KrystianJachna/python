x = 12
y = 0

try:
    print(x + "!")
    print(x/y)
    print("Linijka po")
except ZeroDivisionError:
    print("Nastąpiło dzielenie przez 0!")
except TypeError:
    print("Niezgodność typów danych")


# po try program probuje cos wykonac, jednak
# to co ma zostac wykonane w przypadku niepowodzenia
# okreslami w except i po okresleniu rodzaju bledu
# jakiego sie spodziewamy

print("Dalsze instrukcje")


try:
    lista = [3]
    print(lista[0])
    print("siema" + "!")
    print(x/3)
    print("Linijka po")
except (ZeroDivisionError, TypeError):
    print("Błąd!!!")
except:
    print("Inny błąd")
# w ten sposob wszystkie inne bledy zostaja przechwycone
finally:
    print("FINALLY, wykonuje sie zawsze czy bedzie blad"
          "czy nie")

