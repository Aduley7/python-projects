class Student:
    college_name = "MITE"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database...")
        
    def welcome(self):
        print("Welcome Student",s1.name)
        
    def get_marks(self):
        return self.marks
        
s1 = Student("Karan", 97)
s1.welcome()
print(s1.get_marks())
# print(s1.name)
# print(s1.marks)