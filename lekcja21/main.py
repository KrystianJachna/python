# wyrażenia lambda

def funkcja(f, liczba):
    return f(liczba)


# czyli taka funkcja "na szybko"
print(funkcja(lambda x: x * x, 3))


def kwadrat(x):
    return x * x


print(kwadrat(5))

wyn = (lambda x: x * x)(6)
print(wyn)

lam = lambda x: x * x
print(lam(8))

lam2 = lambda x, y: x * y
print(lam2(3,2))