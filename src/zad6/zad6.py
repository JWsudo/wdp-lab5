from time import sleep

czas = int(input("Podaj liczbe sekund"))


while(czas != 0):
    print(czas)
    sleep(1)
    czas = czas - 1