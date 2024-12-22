import keyword

slowa  = ["for", "print", "break", "done", "bad"]

for x in slowa:
    if x in keyword.kwlist:
        print(f"{x} jest slowem kluczowym")
    else:
        print(f"{x} nie jest slowem kluczowym")