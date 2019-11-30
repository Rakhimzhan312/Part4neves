class House:

    area = 100
    tp = 'family'

    def __init__(self,furniture):
        self.furn_list = furniture
        self.table = furniture_list[0]
        self.bed = furniture_list[1]
        self.wardrobe = furniture_list[2]
        self.total_area = 0
        self.type = ''

    def calc_area(self, t, b, w):
        self.total_area = t + b + w

        
    def final_output(self):
        self.type = 'Family'
        self.remaining_area = self.area - self.total_area
        return ''.join((str(self.remaining_area), ' ', ' '.join(self.furn_list), ' ', self.type))



furniture_list = ['Table', 'Bed', 'Wardrobe']
house = House(furniture_list)
house.calc_area(2,5,8)
print(house.final_output())