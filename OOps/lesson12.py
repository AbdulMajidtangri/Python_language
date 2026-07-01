# OOP is the modular programming approach that tell us to write the code in the form of classes and objects. 
#OOP is a programming paradigm that uses objects and classes in programming.
class Student:
    #init is the constructor of the class. It is used to initialize the object of the class.
    def __init__(self, name):# self refers to the current instance of the class. It is used to access variables that belongs to the class.
        self.name = name
s1 = Student("Majid")
s2 = Student("Ali")

print(s1.name)
print(s2.name)
#function insdie the class is called method. 
# class Car:
#     def __init__(self,name,model,color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def display(self):
#         print(f"The Name of the car of is {self.name} and model number is {self.model} ")

#     def car_name(self):
#         print(f"The Car is {self.name}")
#     def car_model(self):
#         print(f"The Car Modal is :{self.model}")

# car1 = Car("Carolla",2012,"white")

# car1.display()
# car1.car_name()
# car1.car_model()

#Inheritance is the process of creating a new class from an existing class. The new class is called derived class and the existing class is called base class. The derived class inherits the properties and methods of the base class.
class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display(self):
        print(f"The Name of the vehicle is {self.name} and model number is {self.model} ")
    
class Car(Vehicle):
    def __init__(self, name, model, color):
        super().__init__(name, model)
        self.color = color

    def display(self):
        print(f"The Name of the car is {self.name} and model number is {self.model} and color is {self.color} ")

car1 = Car("Carolla",2012,"white")
car1.display()
class Bike(Vehicle):
    def __init__(self, name, model, color):
        super().__init__(name, model)
        self.color = color

    def display(self):
        print(f"The Name of the bike is {self.name} and model number is {self.model} and color is {self.color} ")
bike1 = Bike("Honda",2015,"black")
bike1.display()

#Encapsulation means keeping data protected inside class, In Python, we use _ or __ to show protected/private data.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount(5000)
account.show_balance()

class user:
    def __init__(self, name, age, email,password):
        self.name = name
        self.age = age
        self.email = email
        self.__password = password  # private variable
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
# Polymorphism is the ability to take many forms. In Python, we can use the same method name in different classes and it will behave differently based on the object that is calling it.
#Polymorphism means same method name but different behavior.

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


class Student:
    def __init__(self, name, age, department, marks):
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def find_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A1"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "Fail"

    def show_result(self):
        print("----- Student Result -----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average()}")
        print(f"Grade: {self.find_grade()}")


s1 = Student("Majid", 22, "Software Engineering", [80, 75, 90, 85, 70])
s1.show_result()