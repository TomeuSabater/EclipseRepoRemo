'''
Created on 23 nov 2023
CESUR - Python Tutorial
@author: Tomeu Sabater 
'''
#--- PYTHON DICTIONARIES #############################################
print("#--- PYTHON DICTIONARIES #############################################")
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

# Dictionary Example
my_car = dict({
  "brand": "Ford", #-- You can put here a comment
  "model": "Fiesta",
  "year": 2015,
  "manual": False
}) 
print(my_car)

#--- DICTIONARY ITEMS #############################################
print("#--- DICTIONARY ITEMS #############################################")
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(my_car["brand"])
print(my_car["model"])
print(my_car["year"])
print(my_car["manual"])

#--- DUPLICATES #############################################
print("#--- DUPLICATES #############################################") 
# Duplicates are not allowed in Dictionaries

my_car = dict({
  "brand": "Ford", #-- You can put here a comment
  "model": "Fiesta",
  "year": 2015,
  "manual": False,
  "brand": "Renault",
  "model": "clio",
  "year": 2020,
  "manual": True
}) 
print(my_car)

#--- DICTIONARY LENGTH #############################################
print("#--- DICTIONARY LENGTH #############################################")
# To determine how many items a dictionary has, use the len() function

print("my_car dictionary has : " + str(len(my_car)) + " elements")


#--- DICTIONARY ITEM DATA TYPE #############################################
# The values in dictionary items can be of any data type

my_car = dict({
  "brand": "Ford", 
  "model": "Fiesta",
  "year": 2015,
  "manual": False,
  "color" : list(["black", "white"])
}) 
print(my_car)

#-- The dictiorany is an object
print(type(my_car))

print(''')
Python Collections (Arrays)
There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
''') 

#--- DICTIONARY ACCESS ITEMS #############################################
print("DICTIONARY ACCESS ITEMS #############################################")
# You can access the items of a dictionary by referring to its key name, inside square brackets:

print(my_car["brand"])
print(my_car["model"])
print(my_car["year"])
print(my_car["manual"])

#-- There is also a method called get() that will give you the same result:
print(my_car.get("model")) 
print(my_car.get("year")) 

#-- The keys() method will return a list of all the keys in the dictionary.
print(my_car.keys())

