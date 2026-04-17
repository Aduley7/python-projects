#WAP to print the length of a list. (List is the parameter)

cities = ["delhi", "gurgaon", "noida", "leh", "pune", "chennai"]
heroes = ["thor", "ironman", "spiderman", "hulk"]

def print_len(list):
    print(len(list))
    
# print_len(cities)
# print_len(heroes)

#WAP to print the elements of a list in a single line

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)     
print()   