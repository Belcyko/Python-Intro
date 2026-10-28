class Student:
    def __init__(self, name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

    def year_of_birth(self):
        return 2026 - self.age

student1 = Student('Belvick', 24, 'Web Development')
student2 = Student('Marlick', 28, 'Python Programming')



print(student1.course)
print(student2.name)

student1.introduce()
print(f"{student1.name} was born in {student1.year_of_birth()}")



class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner #this method defines the attributes of the bank account

    def deposit(self, amount):
        self.balance += amount #this method adds funds to the account

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds") #this method withdraws funds from the account. it performs a check to ensure the account has sufficient funds before allowing the withdrawal

    def get_balance(self):
        return self.balance #this method returns the current balance of the account

# Create instances of the BankAccount class
account1 = BankAccount("12345", 1000, "Alice")
account2 = BankAccount("67890", 2000, "Bob") #these are instances of the BankAccount class where each instance has its own set of attributes

# Access attributes using dot notation
print(account1.account_number)
print(account2.owner)

# Call methods using dot notation
account1.deposit(500)
account2.withdraw(200)

print(f"{account1.owner}'s balance: ${account1.get_balance()}")
print(f"{account2.owner}'s balance: ${account2.get_balance()}")


class Person:
    def __init__ (self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age 

class Teacher(Person):
    def __init__(self, name, gender, age, subject):
        super().__init__(name, gender, age)
        self.subject = subject  #this class inherits from Person and adds a subject attribute. in simple terms, it's a specialized version of the Person class. it's like the child class of the parent class 2hich is the person class. The super() function calls the __init__ method of the parent class to initialize the inherited attributes.

person1 = Person("John", "Male", 35)
teacher1 = Teacher("Jane", "Female", 30, "Mathematics")

#Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, typically a class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. In Python, encapsulation is often implemented using private attributes and methods, which are indicated by a leading underscore (_) or double underscore (__).

class Mpesa:
    def __init__(self, name, balance):
        self.name = name  # private attribute
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance

mpesa1 = Mpesa("Alice", 1000)
print(mpesa1.get_balance())  #this returns the balance of the mpesa1 instance. it demonstrates encapsulation by providing a public method to access a private attribute, ensuring that the balance cannot be modified directly from outside the class. in simple terms, it protects the balance from being changed directly, allowing controlled access through the get_balance method.

#Abstract class is a class that cannot be instantiated on its own and is meant to be subclassed. It can contain abstract methods, which are methods that are declared but contain no implementation. Subclasses of an abstract class must provide implementations for all abstract methods. Abstract classes are used to define a common interface for a group of related classes. For example, if you have a base class called Shape, you might define abstract methods like area() and perimeter() that must be implemented by any subclass (like Circle or Rectangle). This ensures that all shapes have a consistent interface for calculating area and perimeter. In a leiman's terms, an abstract class is like a blueprint for other classes. It defines what methods should be available, but doesn't provide the actual code for those methods. Subclasses then fill in the details.

#Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In simple terms, polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name. For example, you might have a method called draw() in a base class Shape, and subclasses like Circle and Square can implement their own version of draw(). When you call draw() on an object, the appropriate method for that object's class is executed.