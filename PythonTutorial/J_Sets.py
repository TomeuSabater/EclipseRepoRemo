'''
Created on 10 nov 2023
Python code
@author: Tomeu Sabater 
'''

#--- PYTHON SETS #############################################
print("#--- PYTHON SETS #############################################")
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data: List, Tuple, Set and Dictionary, 
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.

mi_set = set({"Windows", "Linux", "MacOS"})#-- set creation 
print(mi_set) #-- Sets are unordered, so you cannot be sure in which order the items will appear.

#-- Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered means that the items in a set do not have a defined order, 
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed, Sets cannot have two items with the same value.
# Duplicate values will be ignored:
mi_set = set({"Windows", "Windows", "Linux", "Linux", "MacOS", "Windows"})#-- set creation with duplicates
print(mi_set)

mi_set_boolean = set({1, True, 1, True, 1, False, 0, False}) #-- O/False, 1/True are the same value 
print(mi_set_boolean)

#-- Getting the lenght of the set
#-- To determine how many items a set has, use the len() function.
print(len(mi_set_boolean))
print(len(mi_set))

#-- Set items can be of any datatype
mi_set_mezcla = set({True, False, 0, 1, "Hola", 2.0, 'a'})
print(mi_set_mezcla)

#-- Set is an object
print(type(mi_set_mezcla))


#--- ACCESS SET ITEMS / LOOP SETS #############################################
print("#--- ACCESS SET ITEMS / LOOP SETS #############################################")

# You cannot access items in a set by referring to an index or a key, because they are unordered
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, 
# by using the in keyword.

for elemento in mi_set: #-- Loop through the set items
    print(elemento)

mi_so = str("Windows") 
if (mi_so in mi_set): #-- Ask for specified value in the set 
    print(mi_so + " is in mi_set")


#--- ADD SET ITEMS #############################################
print("#--- ADD SET ITEMS #############################################")

#-- Once a set is created, you cannot change its items, but you can add new items.
#-- To add one item to a set use the add() method.
print(mi_set)
mi_set.add("Android") #-- Add new item, the position is unknown
print(mi_set)

#-- You can add items from another set of items as concatenation has no sense in sets. 
mi_set_SO = set({"Chrome OS", "Solaris", "CP/M", "Windows"})
print(mi_set_SO)
print(mi_set)
mi_set_SO.update(mi_set)
print(mi_set_SO)

#-- You can add (with .update()) any iterable set

#-- Create a set of 100 random elements withouth duplicates
import random 
mi_lista_100 = list([]) #-- Crates the list empty
for i in range(100):
    mi_lista_100.append(int(random.randrange(1, 100)))

print(mi_lista_100) #-- With duplicates
mi_set_100 = set({}) #-- Creates de set empty
mi_set_100.update(mi_lista_100) #-- Transform to set, removing duplicates
print(mi_set_100)
print("mi_set_100 with no duplicates has " + str(len(mi_set_100)) + " elements") 


#--- REMOVE SET ITEMS / LOOP #############################################
print("#--- REMOVE SET ITEMS #############################################")
#-- Remove Set Items 
#-- To remove an item in a set, use the remove(), or the discard() method.

'''
for elemento in mi_set_100:
    if ((elemento % 2) == 0): #-- Even number
        mi_set_100.remove(elemento)
'''

for elemento in range(10, 100, 10): #-- 10, 20, 30, etc.
    if elemento in mi_set_100:
        mi_set_100.remove(elemento) #-- If the item to remove does not exist, remove() will raise an error.
print(mi_set_100)
print("mi_set_100 with no duplicates has " + str(len(mi_set_100)) + " elements") 

for elemento in range(0, 100, 2): #-- 2, 4, 6, 8, etc.
        mi_set_100.discard(elemento) #-- If the item to remove does not exist, remove() will NOT raise an error.

print(mi_set_100)
print("mi_set_100 with no even numbers has " + str(len(mi_set_100)) + " elements") 

#-- Clear method empties the set 
#-- The "del" keyword will delete the set completely:

mi_set_100.clear()
print(mi_lista_100)
print("mi_set_100 has " + str(len(mi_set_100)) + " elements") 

del mi_set_100
# print(mi_set_100)



