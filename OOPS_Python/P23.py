#Inheritance
#Single Level Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car Started...")
        
    @staticmethod
    def stop():
        print("Car Stopped...")
        
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        
car1 = ToyotaCar("Supra")
car2 = ToyotaCar("RX-7")

# print(car1.name)
# print(car2.name)
# car1.start()
# car2.stop()
# print(car1.color)
# print(car2.color)

#Multi-Level Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car Started...")
        
    @staticmethod
    def stop():
        print("Car Stopped...")
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Supra(ToyotaCar):
    def __init__(self, type):
        self.type = type
        
# car1 = Supra ("Diesel")
# car1.start()
# print(car1.type)

#Multiple Inheritance
class A:
    varA = "welcome to class A"
    
class B:
    varB = "welcome to class B"
    
class C(A, B):
    varC = "welcome to class C"
    
c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)
