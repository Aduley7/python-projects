class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("Tundup Angdus")
print(s1.name)

del s1.name

print(s1.name)

#Class (Public)
class Account:
    def __init__(self, acc_no, acc_pswd):
        self.acc_no = acc_no
        self.acc_pswd = acc_pswd
        
acc1 = Account("12356", "wxyz")

print(acc1.acc_no)
print(acc1.acc_pswd)

#Class (Private)
class Account:
    def __init__(self, acc_no, acc_pswd):
        self.acc_no = acc_no
        self.__acc_pswd = acc_pswd
        
    def reset_pswd(self):
        print(self.__acc_pswd)
        
acc1 = Account("12356", "wxyz")

print(acc1.acc_no)
print(acc1.reset_pswd())
