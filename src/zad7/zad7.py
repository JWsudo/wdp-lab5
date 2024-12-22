import datetime

kolokwium = datetime.date(2024,12,17)
ostatnie_zajecia = datetime.date(2024, 12,15 )
print("Ostatnie zajecia: ", datetime.date.today() - ostatnie_zajecia)
print("Do kolokwium: ",  datetime.date.today() - kolokwium)