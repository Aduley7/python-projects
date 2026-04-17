student = {
    "name" : "Manik Langeh",
    "Subjects" : {
        "Phy" : 44,
        "Chem" : 45,
        "Maths" : 48
    } 
}
student.update({"City" : "Delhi"})
new_student = {"Rollno" : "237"}
student.update()
print(student)
print(student.get("name2"))