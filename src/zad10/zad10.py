import random

start = int(input("Start: "))
koniec = int(input("Koniec: "))

data = tuple(random.randint(start, koniec) for x in range(10))

srednia = 1
for i in data:
    srednia *= i

print(srednia ** (1/len(data)))