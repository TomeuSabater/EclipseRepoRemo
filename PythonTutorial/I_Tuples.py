'''
Created on 25 oct 2023
CESUR - Python Tutorial
@author: Tomeu Sabater
'''

#--- PYTHON TUPLES #############################################
print("#--- PYTHON TUPLES #############################################")
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, 
#    the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

mi_tupla = tuple(("uno", "dos", "tres"))
print(mi_tupla)

# Tuple items are Ordered, Unchangeable, and allow Duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered: it means that the items have a defined order, and that order will not change.
# Unchangeable: we cannot change, add or remove items after the tuple has been created.
# Duplicates allowed: they can have items with the same value

mi_tupla = tuple(("uno", "dos", "tres", "uno"))
print(mi_tupla)

#-- Tuple length
print("mi_tupla tiene " + str(len(mi_tupla)) + " elementos")

#-- It is allowed to create an empty tuple
#-- Remember, name of the tuple is a pointer, with an emtpy tuple we can create a pointer to be used
mi_tupla_vacia = tuple((""))
print("mi_tupla_vacia tiene " + str(len(mi_tupla_vacia)) + " elementos")

#-- or a tuple with only one item, in this case you need add a comma after the item
mi_tupla_un_item = tuple(("uno"))
print(mi_tupla_un_item)
print("mi_tupla_un_item tiene " + str(len(mi_tupla_un_item)) + " elementos")

mi_tupla_un_item = tuple(("uno",))
print(mi_tupla_un_item)
print("mi_tupla_un_item tiene " + str(len(mi_tupla_un_item)) + " elementos")

#-- The items can be of any datatype and can be mixed
mi_tupla_mezcla = tuple(("Tomeu", 34, True, 40, "Sabater"))
print(mi_tupla_mezcla)

#-- Tuples are objects in Python
print(type(mi_tupla_mezcla)) 


#--- ACCESS TUPLES #############################################
print("#--- ACCESS TUPLES #############################################")

#-- You can access tuple items by referring to the index number, inside square brackets:
print(mi_tupla_mezcla[0]) #-- First element
print(mi_tupla_mezcla[1]) #-- Second element
print(mi_tupla_mezcla[2])
print(mi_tupla_mezcla[3])

#-- Negative indexing means start from the end.


