class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.brk = True
        self.clutch = True
        print("Car Starting...")
        
c1 = Car()
c1.start()