# f = open("Demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# with open("Practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.") 

# with open("Practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("Java", "Python")
# print(data)

# with open("Practice.txt", "w") as f:
#     f.write(new_data)

def check_for_word():
    word = "mlearning"
    with open("Practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")
            
# check_for_for_word()

def check_for_line():
    word = "pgg"
    data = True
    line_no = 1
    with open("Practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_for_line())