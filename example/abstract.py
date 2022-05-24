#https://www.geeksforgeeks.org/abstract-classes-in-python/
#https://www.pythontutorial.net/python-oop/python-abstract-class
"""
    An abstract class can be considered as a blueprint for other classes.
    A class which contains one or more abstract methods is called an abstract class
    When we want to provide a common interface for different implementations of a component, we use an abstract class.
"""

from abc import ABC, abstractmethod
class Animal(ABC):

    def move(self):
        pass

    def read(self):
        print("Abstract Base class")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Human(Animal):

    def move(self):
        print("I can say hello!!")

# Driver code
# H = Human()
# H.move()
#
# D = Dog()
# D.move()

# Implementation Through Subclassing :
# isSub = issubclass(Human, Animal)
# print(isSub)

#Concrete Methods in Abstract Base Classes by use super().
# class ChildRead(Animal):
# 	def newRead(self):
# 		super().read()
# 		print("Subclass ")
#
# r = ChildRead()
# r.newRead()


"""
	Abstract Properties :
    Abstract classes include attributes in addition to methods, you can require the attributes in concrete classes by defining them with @abstractproperty
"""
# Abstract Class Instantiation :
from abc import ABC,abstractmethod

class AbstractAnimal(ABC):
#     @abstractmethod
#     def move(self):
#         pass

# h = AbstractAnimal()