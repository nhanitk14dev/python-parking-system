#Parent class: is the class being inherited from,also called base class.
#Child class: is the class that inherits from another class, called derived class
class Bird:
    def __init__(self, name):
        self._name = name # Encapsulation (private property)
        print(self._name, "is born.")

    def get_name(self):
        print(self._name, "is a 'Bird'.")


class Penguin(Bird): # Inheritance
    def __init__(self, name):
        super().__init__(name)
        print("New penguin is born.")

    def fly(self):
        print(self._name, "cannot fly.")

# bird = Bird("Dove")
# print(bird.get_name())

# jacky = Penguin("Jacky")
# jacky.get_name() # Polymorphism
# jacky.fly()


# print(jacky)
# -------------------Learn by W3SCHOOLS--------------------------------
#https://www.w3schools.com/python/python_classes.asp

# Object method
class Person:
    pass
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        #Converting a Python int to a String and reverse use str, int
        print("Hello my name is " + self.name + ". I'm " + str(self.age))

p1  = Person("nhan", 26)
p1.age = 40  # Modify Object Properties
del p1.age #Delete Object
# p1.greeting()

print (Person())
