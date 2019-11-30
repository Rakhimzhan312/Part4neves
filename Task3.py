class Car:

    def __init__(self, brand, model, year, odometer, fuel):

        self.odometer = 0
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = 70

    def __subtract_fuel(self,consumed):

        self.fuel -= consumed 
        print('Lets Drive!! and you have this much of fuel remaining ',str(self.fuel))
    
    def add_distance(self, addkms):
        self.odometer = addkms


    
    def drive(self, distance):

        if distance <= self.fuel * 10:
            kms = distance
            self.add_distance(kms)
            fuel_consumed = kms/10
            self.__subtract_fuel(fuel_consumed)
        else:
            print('Not enough fuel')

car = Car('bmw','x5m', 2019, 0, 0)

car.drive(701)