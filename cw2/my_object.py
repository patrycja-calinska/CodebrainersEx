

class Car:
    def __init__(self, given_color, given_engine, given_marka):
        self.color = given_color
        self.engine = given_engine
        self.marka = given_marka

    def drive(self, distance):
        print(f"przejechalem {distance} km, z uzyciem silnia {self.engine}")

    def make_some_noise(self):
        print(f"{self.marka} jest najlepsza!!")

    def my_color_is(self):
        return self.color


polonez = Car("czerwony", "v2.0", "Polonezzz")

# my_car_engine = polonez.engine
# print(my_car_engine)
polonez.drive(10)
polonez.make_some_noise()
print(polonez.color)
polonez.color = "zielony"
print("nowy color to:", polonez.color)

