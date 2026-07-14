age = 25
print(type(age))

name =  "John"
print(type(name))

price = 9.99
print(type(price))

is_student = True
print(type(is_student))



class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(f"{self.name} is eating.")

    def reproduces(self):
        print(f"{self.name} is reproducing.")

    def swins(self):
        print(f"{self.name} is swimming.")
    
    def climbs(self):
        print(f"{self.name} is climbing.")

    def walks (self):
        print(f"{self.name} is walking.")


Fish = Animal("Fish", 2, "Silver")
Capibara = Animal("Capibara", 5, "Brown")
Monkey = Animal("Monkey", 3, "Black")

print(Fish.name)
print(Fish.age)
print(Fish.color)


print(Capibara.name)
print(Capibara.age)
print(Capibara.color)

print(Monkey.name)
print(Monkey.age)
print(Monkey.color)

Fish.eat()
Fish.reproduces()
Fish.swins()

Capibara.eat()
Capibara.reproduces()
Capibara.walks()

Monkey.eat()
Monkey.reproduces()
Monkey.climbs()


