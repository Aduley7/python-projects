class Person:
    name = "anonymous"
    
    def __init__(self, name):
        Person.name = name
        
        
p1 = Person("Rahul Kumar")
print(p1.name)
print(Person.name)