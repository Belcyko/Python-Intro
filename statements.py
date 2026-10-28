age=int(input('Enter your age: ')) #this will convert the input to an integer
if age >= 18:
    print('You are an adult.') #this will print if the condition is true
else:
    print('You are not an adult.') #this will print if the condition is false

    marks=int(input('Enter your marks: '))
    if marks >= 80:
        print('You got an A.')
    elif marks >= 70:
        print('You got a B.') 
    elif marks >= 60:
        print('You got a C.')
    elif marks >= 50:
        print('You got a D.')
    else:
        print('You failed.')


#create a simple BMI system using the conditional statements, letting weight and height be user inputs, and then calculating the BMI and printing the result based on the BMI value.
weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in centimeters: '))
bmi = weight / (height / 100 ** 2)
if bmi >= 30:
    print('You are obese.')
elif bmi >= 25:
    print('You are overweight.')
elif bmi >= 18.5:
    print('You have a normal weight.')
else:
    print('You are underweight.')



#Loops
#For loop
for number in [12,34,543,656,76,87,98,90]:
    print(number) #this will print each number in the list  

#While loop
i = 0
while i < 10:
    print(i) #this will print each number from 0 to 9   
    i += 1

    
