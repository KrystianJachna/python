def gen():
    i = 0
    while i < 5:
        yield i
        i += 1
# yield i to taki return tylko nie konczy dzialania funkjci

for i in gen():
    print(i)
# po generatorze można iterować w taki sposób

print(list(gen()))


def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1


for i in parzyste(10):
    print(i)


print(list(parzyste(10)))


