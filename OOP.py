#program paradigm oriented to objects

#example of class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def salute(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

# Object is a new istance of the class
person1 = Person("Igor", 35)
message = person1.salute()
print(message)

person2 = Person("Carlos", 30)
message = person2.salute()
print(message)


#inheritance

print("\nExample of inheritance:")
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        print(f"The animal {self.name} is walking")
        return
    
    def make_sound(self):
        pass 

class Dog(Animal):
    def make_sound(self):
        return "Woof, woof"
    
class Cat(Animal):
    def make_sound(self):
        return "Miau"
    
dog_1 = Dog(name="Hazel")
cat_1 = Cat(name="Blacky")

print("\nExample of polymorphism:")
animals = [dog_1, cat_1]
for animal in animals:
    print(f"{animal.name} makes this sound: {animal.make_sound()}")

#encapsulation
print("\nExample of encapsulation:")

class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance #protected with the double underline
       
    def deposit(self, value):
        if value > 0:
            self.__balance += value
    
    def withdraw(self, value):
        if value > 0 and value <= self.__balance:
            self.__balance -= value

    def check_balance(self):
        return self.__balance
        pass

account = BankAccount(balance = 1000)
print(f"Your account balance is: ${account.check_balance()}")
account.deposit(value = 500)
print(f"Your account balance is: ${account.check_balance()}")
account.deposit(value = -500)
print(f"Your account balance is: ${account.check_balance()}")
account.withdraw(value = 200)
print(f"Your account balance is: ${account.check_balance()}")
account.withdraw(value = 2000)
print(f"Your account balance is: ${account.check_balance()}")

print("\nSecond account")
account_2 = BankAccount(balance = 50)
print(f"Your account balance is: ${account_2.check_balance()}")
account_2.deposit(value = 100)
print(f"Your account balance is: ${account_2.check_balance()}")
