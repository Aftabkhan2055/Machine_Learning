class demo:
    a = 0
    b = 0
    c = 0

    def accept(self):
        self.a = int(input("enter no a"))
        self.b = int(input("enter no b"))

    def total(self):
        self.c = self.a + self.b
        print("sum is", self.c)
#-----------------------------------------------
x = demo()
x.accept()
x.total()