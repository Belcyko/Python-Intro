print('Hello World!')

a='Belvick'
b=123
x=23.5
z=False
print(a)

#Data types
#String

name="Belvick"
salutation='Good Morning Everyone'
age="27"
#Integer
weight=80
score=95
age1=30

#Boolean
is_student=True
is_paid=False

#Float
height=5.9
price=3.76


#List
fruits=['Apple','Banana','Mango','Grapes']
print(fruits[1]) #Accessing the second element of the list
print(fruits[3]) #Accessing the fourth element of the list

fruits[3]='Pineapple' #Changing the value of the fourth element of the list

fruits.append('Orange') #Adding a new element to the list

#Tuple; which referes to a collection of data that is ordered and unchangeable
days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print(days[0]) #Accessing the first element of the tuple
print(days[2]) #Accessing the third element of the tuple
#with tuple, we cannot change the values of the elements once they are defined. For example, if we try to change the value of the first element of the tuple, we will get an error.

#Dictionary; which refers to a collection of data that is unordered, changeable and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values.
student={'name':'Belvick','age':27,'is_student':True, 'course':'Python Programming'}
print(student['name']) #Accessing the value of the key 'name' in the dictionary
print(student['age']) #Accessing the value of the key 'age' in the dictionary

#set; which refers to a collection of data that is unordered and unindexed. In Python, sets are written with curly brackets.
colors={'Red','Green','Blue','Yellow'}
numbers={1,2,3,4,5}
print(colors)
print(numbers)

#user input
name=input("Enter your name: ")
print("Hello, " + name + "!")  

#Operators
#Arithmetic Operators
num1=10
num2=5
print(num1+num2) #Addition
print(num1-num2) #Subtraction
print(num1*num2) #Multiplication
print(num1/num2) #Division
print(num1%num2) #Modulus

total=num1+num2
print("The total is: " + str(total)) #Type casting to convert integer to string

#Comparison Operators
num1=10
num2=5
print(num1>num2) #Greater than
print(num1<num2) #Less than
print(num1==num2) #Equal to 
print(num1!=num2) #Not equal to

#Logical Operators
print(num1 and num2) #Logical AND
age2=20
is_adult=True
print(age2>18 and is_adult) #Logical AND
print(age2>18 or is_adult) #Logical OR
print(not is_adult) #Logical NOT
