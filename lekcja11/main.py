def func(x):
    return x*x


zmienna = func
print(zmienna(5))   # dziwne, ale przekazujemy moc funkcji zmiennej


def func2(f1, x):       # argumentem funkcji jest funkcja
    return f1(x) * x


print(func2(func, 5))


def silnia(n):
    if n <= 1:
        return 1
    else:
        return n * silnia(n-1)


print(silnia(5))



