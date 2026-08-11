#power_of_three = lambda number: number ** 3
#print (power_of_three(3))

#some_lambda = lambda x, y, z: x + y + z
#print (some_lambda(1, 2, 3))

#check_even = lambda x: True if x % 2 == 0 else False
#print (check_even(2))

#def add(x, y):
    #return x + y

#def subtract(x, y):
    #return x - y

#def multiply(x, y):
    #return x * y

#def calculator(x, y, operation):
    #return operation(x, y)

#number1 = 100
#number2 = 50

#result1 = calculator(number1, number2, add)
#result2 = calculator(number1, number2, subtract)
#result3 = calculator(number1, number2, multiply)

#print("Addition:", result1)
#print("Subtraction:", result2)
#print("Multiplication:", result3)

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

print (list(map(square, numbers)))



