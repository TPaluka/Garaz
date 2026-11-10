import random
from datetime import datetime

class Auto:
    def __init__(self,znacka:str, model:str, rok:int, STK:int, palivo:int = 100):
        self.znacka = znacka
        self.model = model
        self.rok = rok
        self.STK = STK
        self.palivo = palivo
        pass

    def __str__(self): #metoda která se volá jako základní pro výpis vlastnosti objektu
        return f"{self.znacka}, {self.model}, ({self.rok}), {self.STK}, palivo: {self.palivo} %"
    
    def move(self):
        spotreba = random.randint(5, 20)
        if self.palivo >= spotreba:
            self.palivo -= spotreba # / self.palivo - spotreba
            return f"{self.znacka}, {self.model} spotřeboval {spotreba} % paliva a zbývá mi {self.palivo}"
        else:
            return f"{self.znacka}, {self.model} nemá dostatek paliva aby dojel. Potřebuje {spotreba} % paliva, ale má jen {self.palivo} % paliva"
        pass

    def natankovat(self):
        natankovano = 100 - self.palivo
        self.palivo = 100
        return f"{self.znacka}, {self.model} natankoval {natankovano} % paliva."
    
    def STKControl(self):
        if self.STK < datetime.now().year:
            return f"{self.znacka}, {self.model} musí na technickou - technická skončila v roce {self.STK}"
        else:
            return f"{self.znacka}, {self.model} nemusí na technickou - na technickou musíte za: {self.STK - datetime.now().year} let"
        pass

auto1 = Auto("Škoda", "Octavia 3", 2016, 2026, 85)
auto2 = Auto("Volkswagen", "Golf 7", 2018, 2022, 10)
auto3 = Auto("Toyota", "Hilux", 2014, 2028, 3)

#testovaci vypis
print(auto1)
print(60*"-")
print(auto2)
print(60*"-")
print(auto3)
print(60*"-")
print(auto1.move())
print(60*"-")
print(auto2.move())
print(60*"-")
print(auto3.move())
print(60*"-")
print(auto1.natankovat())
print(60*"-")
print(auto2.natankovat())
print(60*"-")
print(auto3.natankovat())
print(60*"-")
print(auto1.STKControl())
print(60*"-")
print(auto2.STKControl())
print(60*"-")
print(auto3.STKControl())
print(60*"-")

class Garaz:
    def __init__(self, name):
        self.name = name
        self.cars = []
        pass

    def addCars(self, car:Auto):
        self.cars.append(car)
        return f"Do garáže {self.name} bylo přidáno auto: {car.znacka} {car.model}"
    
    def showCars(self):
        if len(self.cars) == 0:
            print(f"Garáž {self.name} je prázdná")
        else:
            print(f"Auta v garáži {self.name}:")
            for cars in self.cars:
                print("-->", cars)

    def oldestCar(self):
        if len(self.cars) == 0:
            return None
        theOldest = min(self.cars, key=lambda a: a.rok)
        return theOldest
    
    def avgPalivo(self):
        if len(self.cars) == 0:
            return 0
        return sum(car.palivo for car in self.cars) / len(self.cars)

garaz = Garaz("Podzemní garáž")

garaz.showCars()
print(60*"-")
print(garaz.addCars(auto1))
print(60*"-")
print(garaz.addCars(auto2))
print(60*"-")
print(garaz.addCars(auto3))
print(60*"-")
print(f"{garaz.avgPalivo():.1f} %")
garaz.showCars()

oldest = garaz.oldestCar()
if oldest:
    print(f"Nejstarší auto v garáži je {oldest.znacka}, {oldest.model} ({oldest.rok})")

print(garaz.cars[2].move())

for brambora in garaz.cars:
    print(brambora.STKControl())