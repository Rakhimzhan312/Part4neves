class Soldier():

    def __init__(self):

        self.name = "Ryan"



class Guns(Soldier):
    def __init__(self):
        Soldier.__init__(self)
        self.num_of_bullets = 5
    
    def fire(self):
        name = self.name
        print(name, ' starts shooting!!! Watch out!!!')
        while self.num_of_bullets:
            print("tigi-tigitishh")
            self.num_of_bullets -=1
        self.reload()

    def reload (self):
        self.num_of_bullets = 5



class Act_of_shooting(Guns):

    def __init__(self):
        Guns.__init__(self)
        Soldier.__init__(self)

    def start(self):
        Guns.fire(self)
        Guns.reload(self)
        Guns.fire(self)

game = Act_of_shooting()
game.start()