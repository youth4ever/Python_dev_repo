#  Created by Bogdan Trif on 16-03-2018 , 9:20 PM.
'''

                                     ===     Encapsulation   ===
                                        PUBLIC  &   PRIVATE
In an object oriented python program, you can restrict access to methods and variables.
This can prevent the data from being modified by accident and is known as ENCAPSULATION.
Let’s start with an example.

                                --  Private methods --

We create a class Car which has two methods:  drive() and updateSoftware().

When a car object is created, it will call the private methods __updateSoftware().
This function cannot be called on the object directly, only from within the class.
'''
print('\n------------------------       Private methods        ------------------------------')

class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()

'''
Encapsulation prevents from accessing accidentally, but not intentionally.

The private attributes and methods are not really hidden, they’re renamed adding “_Car” in the beginning of their name.

The method can actually be called using redcar._Car__updateSoftware()
'''
print()
redcar._Car__updateSoftware()
print()

print('\n------------------------       Private variables        ------------------------------')

'''
                                    --  Private variables   --

Class with private variables
Variables can be private which can be useful on many occasions. 
A private variable can only be changed within a class method and not outside of the class.
Objects can hold crucial data for your application and you do not want that data to be changeable from anywhere in the code.
An example:
'''
class Car:

    __maxspeed = 0              # Private variable, static elements, it means, they belong to the class.
    __name = ""                     # Private variable, , static elements, it means, they belong to the class.

    def __init__(self):
        self.__maxspeed = 200       #   elements of the object (self ), they don't belong to the class
        self.__name = "Audi A8"     #   elements of the object (self ), they don't belong to the class

    def drive(self):
        print(str(self.__name)+ ' driving. maxspeed ' + str(self.__maxspeed))

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()
print()


print('\n-------- Change value to a private variable __maxspeed  -------------')

'''If you want to change the value of a private variable, a setter method is used.  
This is simply a method that sets the value of a private variable.
'''


class Car:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Audi A8"

    def drive(self):
        print(str(self.__name)+ ' driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()
print()

'''
Why would you create them? 
Because some of the private values you may want to change after creation of the object 
while others may not need to be changed at all.
'''


'''
To summarize, in Python there are:

Type	                                    Description
public methods          -   	 Accessible from anywhere
private methods	      -      Accessible only in their own class. starts with two underscores
public variables	          -      Accessible from anywhere
private variables	      -      Accesible only in their own class or by a method if defined. starts with two underscores

Other programming languages have protected class methods too, but Python does not.

Encapsulation gives you more control over the degree of coupling in your code, 
it allows a class to change its implementation without affecting other parts of the code.

'''