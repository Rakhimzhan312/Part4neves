class Airplane:

    def __init__(self, brand, model, year, max_speed, odometer, is_flying):

        self.is_flying = False
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = str(max_speed) + 'mph'
        self.odometer = odometer

    def take_off(self):

        self.is_flying = True

    def land(self):
        
        self.is_flying = False

    def fly(self, distance):

        self.odometer += distance
        print('Updated odometer value is : ' + str(self.odometer))

test_airplane = Airplane('Airbus', 'A320', 2019, 880,0, True )

test_airplane.fly(20000)