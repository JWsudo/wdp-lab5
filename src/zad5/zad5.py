from random import sample

liczby = []

for i in range(1,50):
    liczby.append(i)

print(liczby)

print(sample(liczby, 6))