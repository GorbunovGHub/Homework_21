class Car:
    price = 1000000

    def horse_powers(self):
        self.horsepower = 100
        print(self.horsepower)


class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        self.horsepower = 300
        print(self.horsepower)


class Kia(Car):
    price = 500000

    def horse_powers(self):
        self.horsepower = 150
        print(self.horsepower)


car_1 = Car()
print(car_1.price)
print(car_1.horse_powers())
car_2 = Nissan()
print(car_2.price)
print(car_2.horse_powers())
car_3 = Kia()
print(car_3.price)
print(car_3.horse_powers())
