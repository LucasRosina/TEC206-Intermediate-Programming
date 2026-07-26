#def print_details(name=" ", age= " ", country=" "):
    #print(f"My Name is {name}")
    #print(f"I am {age}")
    #print(f"I live in {country}")
#print_details(name="Lucas", age=20, country="Brazil")

#def count_occurences(*args):
    #count = {}
    #for arg in args:
        #if arg in count:
            #count[arg] += 1
        #else:
            #count[arg] = 1
    #return count
#print(count_occurences("teste", "teste", "aaaa", "aaaa"))

#def calculate_average(*args):
    #if len(args) == 0:
        #return 0

    #total = sum(args)
    #average = total / len(args)
    #return average

#print(calculate_average(1023432, 203123, 342120))       

from unicodedata import name


def create_student(name, age, grades=None):
    if grades is None:
        grades = []
    student = {
        'name': name,
        'age': age,
        'grades': grades
    }
    return student

student1 = create_student('John', 18)
student2 = create_student('Alice', 19)
student3 = create_student('Bob', 20)
student4 = create_student('Eve', 21)

student1['grades'].append(80)
student2['grades'].append(90)
student3['grades'].append(85)
student4['grades'].append(95)

print("Student 1:", student1)
print("Student 2:", student2)
print("Student 3:", student3)
print("Student 4:", student4)