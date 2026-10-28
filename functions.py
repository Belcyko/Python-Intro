#Functions
print('Good Morning Noela')
print('Good Morning Noela')
print('Good Morning Noela')

def salutation(name, age):
    print(f'Good Morning {name}, you are {age} years old.') #this is a function that prints a greeting. a parameter can be added to the function to make it more dynamic. In this case, the parameter can be the name of the person to greet.

salutation('Noela', 25)
salutation('Mercyline', 30)
salutation('Belvick', 35)


def add(num1, num2):
    sum = num1 + num2
    return sum

add(5, 10)
print(add(5, 10))
print(add(209, 363))

def areaRectangle(length, width):
    area = length * width
    return area

print(areaRectangle(5, 10))
print(areaRectangle(209, 363))

def areaCircle(radius, pi=3.14):
    area = pi * radius ** 2
    return area

print(areaCircle(28))
print(areaCircle(6370))   


def area_of_circle(radius, pi=3.14):
    if radius < 0:
        return "Radius cannot be negative."
    elif radius == 0:
        return "Area is zero."
    else:
        return pi * radius ** 2

print(area_of_circle(28))
print(area_of_circle(-5))
print(area_of_circle(0))



def divide_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    finally:
        print("Division completed.") #this is a function that divides two numbers. It uses a try-except block to handle the case where the second number is zero, which would cause a division by zero error. The finally block will always execute, regardless of whether an exception occurred or not.

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, 5))


def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f'Your BMI is {bmi:.2f}. You are Underweight.'
    elif 18.5 <= bmi < 24.9:
        return f'Your BMI is {bmi:.2f}. You have Normal weight.'
    elif 25 <= bmi < 29.9:
        return f'Your BMI is {bmi:.2f}. You are Overweight.'
    else:
        return f'Your BMI is {bmi:.2f}. You are Obese.' 

print(calculate_bmi(1.75, 60))  # Normal weight
print(calculate_bmi(1.75, 50))  # Underweight  
print(calculate_bmi(1.75, 80))  # Overweight
print(calculate_bmi(1.75, 100)) # Obese