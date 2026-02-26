Marks = int(input("Enter your marks: "))

if(Marks >= 90):
    grade = "A"
elif(Marks >= 80 and Marks < 90):
    grade = "B"
elif(Marks >= 70 and Marks < 80):
    grade = "C"
elif(Marks >= 60 and Marks < 70):
    grade = "D"
else:
    grade = "F"
print("The grade of the student is:", grade);