class car:
    speed=0
    def acc(self):
        self.speed=self.speed+1
    def brake(self):
        self.speed=self.speed-1
    def display(self):
        self.display=("total speed is",self.speed)
#------------------------------------------------------
x=car
x.acc()
x.brake()
x.display()

