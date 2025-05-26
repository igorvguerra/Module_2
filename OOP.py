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

