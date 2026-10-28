#user input
name=input('Belvick')
print(name)

first_name=input('Please enter your first name: ')
last_name=input('Please enter your last name: ')
age=input('Enter your age: ')

print(f'Hello {first_name} {last_name}, you are {age} years old.')

num1=input('Enter a number: ')
num2=input('Enter another number: ')   
total=int(num1)+int(num2)
print(f'The total of {num1} and {num2} is {total}.')

price =float(input('Enter the price of the item: '))
quantity =int(input('Enter the quantity of the item: '))
item_name =input('Enter the name of the item: ')
total = price * quantity
print(f'The total cost of {quantity} {item_name}(s) is Kes{total}.')

#ask the user for amount paid and calculate the change due assuming amount paid is sufficient
amount_paid = float(input('Enter the amount paid: '))
change_due = amount_paid - total
print(f'The change due is Kes{change_due}.')


