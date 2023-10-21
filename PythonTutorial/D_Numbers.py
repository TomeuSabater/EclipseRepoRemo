'''
Created on 19 oct 2023

Python Numbers

@author: bmesa
'''

#-- Números Enteros
var_int = int(-123456789)  # Número entero, positivo o negativo

print(var_int)
print(type(var_int))

#-- Números reales 
var_float = float(-222.8875)  # Variable real, positivo o negativo con parte entera y parte decimal
var_floate = float(35e3)
var_floatE = float(35E3)
var_floatSC = float(-87.7e100)

print(var_float)
print(type(var_float))
print(var_floate)
print(type(var_floate))
print(var_floatE)
print(type(var_floatE))
print(var_floatSC)
print(type(var_floatSC))

#-- Números complejos

var_complex = complex(-3+5j) # Variable compleja, con "j" es la parte imaginaria

print(var_complex)
print(type(var_complex))

#-- Type Conversion

x_int = int(10)         # int / entero
y_float = float(2.8)    # float / real 
z_complex = complex(1j) # complex

#convert from int to float
a_float = float(x_int) # Parte decimal será 0
print(a_float)
print(type(a_float))

#convert from float to int
b_int = int(y_float) # Parte decimal se pierde
print(b_int)
print(type(b_int))

#convert from int to complex:
c_complex = complex(x_int) # Parte imaginaria será 0
print(c_complex)
print(type(c_complex))

#-- Random Numebers
#-- Python has not a random generator, 
#-- Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))

x_random = int(random.randrange(1, 10))
print(x_random)

