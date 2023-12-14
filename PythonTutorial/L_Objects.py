'''
Created on 14 dic 2023
Python code
@author: Tomeu Sabater 
'''

import math

#--- PYTHON OBJECTS #############################################
print("#--- PYTHON OBJECTS #############################################")

#-- Object Creation 
class MiPrimeraClase:

    nombre = "Tomeu Sabater"
    edad = 50 # Contains an integer

print(MiPrimeraClase)
print(MiPrimeraClase.nombre)
print(MiPrimeraClase.edad)

#-- Let's go to create our first object
Persona = MiPrimeraClase() #-- Create a new Object
print(Persona.edad)
print(Persona.nombre)

#-- _init_ function to create an object with different values. 

class Person:
    def __init__(self, nombre, edad): #-- Constructor, it is automatically executed
        self.name = nombre
        self.age = edad

Persona1 = Person("Tomeu Sabater", 50)  #-- Creae a new object
Persona2 = Person("John Smith", 20) #-- Crate a new object

print(Persona1.name)   
print(Persona2.name)

#-- __str__(self) defines the string representation of the object is returned:

class Person2:
    def __init__(self, nombre, edad): #-- Constructor, it is automatically executed
        self.name = nombre
        self.age = edad
        
    def __str__(self):
        return f"{self.name}({self.age})"  


Persona3 = Person2("Tomeu", 50)
print(Persona3) 

#-- Method creation

class Person3:
    def __init__(self, nombre, edad): #-- Constructor, it is automatically executed
        self.name = nombre
        self.age = edad
        
    def __str__(self):
        return f"{self.name}({self.age})"  

    def imprime_nombre(self):
        print(self.name)
        
    def imprime_edad(self):
        print(self.age)
        
    def set_edad(self, edad):
        self.age = edad

    def set_nombre(self, nombre):
        self.name = nombre
        
Persona3 = Person3("Ana", 10)
Persona3.imprime_nombre()
Persona3.imprime_edad()
Persona3.set_edad(10)
Persona3.set_nombre("Juan")
print(Persona3)

class PersonAdult:
    def __init__(self, nombre):
        self.name = nombre
        self.age = 18
     
    def set_age(self, edad):
        if edad < 18:
            self.age = 18
        else: 
            self.age = edad 

    def __str__(self):
        return f"{self.name}({self.age})"  

Persona4 = PersonAdult("Tomeu")
print(Persona4)
Persona4.set_age(10)
print(Persona4)

class circle:
    def __init__(self, radio):
        if radio < 0:
            self.radius = -radio
        elif radio == 0:
            self.radius = 1
        else:
            self.radius = radio
        
        self.diameter = self.radius * 2
        self.perimeter = 2 * math.pi * self.radius
        self.area = math.pi * self.radius * self.radius
        
    def print_info_circle(self):
        print("The circle has the next info:")
        print("The radius is :" + str(self.radius))
        print("The perimeter is:" + str(self.perimeter))
        print("The area is:" + str(self.area))
        
    def circle_radius_update(self, radio):
        if radio < 0:
            self.radius = -radio
        elif radio == 0:
            self.radius = 1
        else:
            self.radius = radio
        
        self.diameter = self.radius * 2
        self.perimeter = 2 * math.pi * self.radius
        self.area = math.pi * self.radius * self.radius
        
    
Circle1 = circle(5)
Circle1.print_info_circle()