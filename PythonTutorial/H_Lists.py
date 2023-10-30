'''
Created on 25 oct 2023

CESUR - Python Tutorial
@author: Tomeu Sabater
'''
#--- PYTHON LISTS #############################################

#-- List is a data type in Python.
#-- Lists are used to store multiple items in a single variable.
#-- List items can be of any data; str, int, boolean.  
#-- List is a collection which is ordered and changeable (change the value of any item). 
#-- List allows duplicate members.

mi_lista_texto = list(["manzana","pera","melón"]) # Create a list of values of type 'str'
print(mi_lista_texto)

mi_lista_numeros = list([1,2,3,4,5]) # Create a list of values of type 'int'
print(mi_lista_numeros)

mi_lista_mezcla = list([False,"a",1,"e",2,"i",3, True]) # Create a list of different type of values
print(mi_lista_mezcla)

print(type(mi_lista_mezcla)) #-- Prints the type of the list

#--- ACCESS Item ##################################
#-- List items are indexed and you can access them by referring to the index numer
print("#-- ACCESS specific Item")
print(mi_lista_texto)
print(mi_lista_texto[0])
print(mi_lista_texto[1]) #-- The index starts by 0, this prints the second element

print(mi_lista_texto)
print(mi_lista_texto[-1]) #-- Negative index means starts by the end
print(mi_lista_texto[-2])
print(mi_lista_texto[-3])

#-- You can specify a Range of indexes
#-- Specifiying a Range the result is a new list
print(mi_lista_mezcla)
print(mi_lista_mezcla[3:5]) #-- Last index is excluded. 
print(mi_lista_mezcla[3:]) #-- From the index 3 to the end
print(mi_lista_mezcla[:5]) #-- Until the index 5 excluded
print(mi_lista_mezcla[-4:-1]) #-- Remember, last item in a range is excluded 
print(mi_lista_mezcla[-4:]) #-- Remember, last item in a range is excluded 
print(mi_lista_mezcla[0:3])
print(mi_lista_mezcla[len(mi_lista_mezcla)-1]) #-- The last element / returns one element
print(mi_lista_mezcla[-1:10])
print("xxxxxxxxxxx")
print(mi_lista_mezcla[0:len(mi_lista_mezcla)]) #-- From first to the last element
print("xxxxxxxxxxx")

#-- List length
print("mi_lista_mezcla tiene " + str(len(mi_lista_mezcla)) + " elementos")

#--- CHECK for an Item ##################################
#-- The index of the Item is not returned
print("#-- Check for an Item")

fruta = str("MANZANA") #-- Check with pera, naranja, piña, etc. 
if (fruta.lower() in mi_lista_texto):
    print(fruta + " existe en la lista")
else:
    print(fruta + " no existe en la lista")

#--- CHANGE list Items ############################
print("#--CHANGE List Items")

#-- Change item value 
print(mi_lista_texto)
mi_lista_texto[2] = "naranja" #-- Change item value
print(mi_lista_texto)

#-- Change a range of item values
mi_lista_texto[0:2] = ["melocotón","piña"] #-- Change a range of items
print(mi_lista_texto)

#-- You can change and insert items at the same time
mi_lista_texto[0:1] = ["melicotó","pera"] #-- Change and insert items
print(mi_lista_texto)

#-- You can change and renove items at the same time
mi_lista_texto[1:3] = ["pera y piña"] #-- Change and remove items
print(mi_lista_texto)

#--- INSERT items in the list ############################
#-- we can use the insert() method.
print("#--INSERT List Items")
print(mi_lista_texto)
mi_lista_texto.insert(3, "watermelon")
print(mi_lista_texto)

mi_lista_texto.insert(0, "Guacamole")
print(mi_lista_texto)
print("xxxxxxxxxxxxxxxxxxxxxxxx")
mi_lista_texto.insert(-1, "manzanaxxxx")
print(mi_lista_texto)
print("xxxxxxxxxxxxxxxxxxxxxxxx")

#--- ADD list Items ############################
#To add an elemento to the end of the list we can use the .append()
print("#-- ADD List Items")
mi_lista_texto.append("plátano")
print(mi_lista_texto)

#--- REMOVE List Items ############################
print("#-- REMOVE List Items")
print(mi_lista_texto)
mi_lista_texto.remove("pera y piña") #-- remove this element from the list
print(mi_lista_texto)
# mi_lista_texto.remove("pera y piña") #-- If elemento doesn't exist raises an error

mi_lista_texto.append("plátano") # Add platano at the end
print(mi_lista_texto)
mi_lista_texto.remove("plátano") # Remove first occurrence
print(mi_lista_texto)

#-- Remove from specified index 
print("#-- pop")
mi_lista_texto.pop(0) #-- Remove first element from the list
print(mi_lista_texto)

mi_lista_texto.pop(len(mi_lista_texto)-1) #-- Remove last element from the list
print(mi_lista_texto)

mi_lista_texto.pop() #-- Remove last elemento from the list
print(mi_lista_texto)

#-- The "del" keyword also removes the spcified index
print("#--- del")
del mi_lista_texto[2]
print(mi_lista_texto)

# -- The del keyword can also delete the list completely.
del mi_lista_texto #-- Removes the list
# print(mi_lista_texto) #-- Raises an error because the list doesn't exist

#-- The clear() method empties the list.
print("#--- clear()")
print(mi_lista_numeros)
mi_lista_numeros.clear() #-- Empties the list
print(mi_lista_numeros) #-- List exists, is empy

#---  LOOP Lists ############################
#-- You can loop through the list items by using a for loop
print("#-------Loop Lists")
for elemento in mi_lista_mezcla:
    print(elemento)

#-- You can also loop through the list items by referring to their index number.
print("Range of \'mi_lista_mezcla\' is " + str(range(len(mi_lista_mezcla)))) #-- Show the range
for i in range(len(mi_lista_mezcla)):
    print(mi_lista_mezcla[i])

#-- Loop using a While Loop 
print("#------Using a While")
indice = int(0) #-- Index creation
while indice < len(mi_lista_mezcla):
    print(mi_lista_mezcla[indice])
    indice += 1

#---  LIST COMPREHENSION ############################
   
#-- Loop using List Comprehension 
#-- This system offers the shortest syntax for looping throug lists
print("#----- Using List Comprehension")
[print(elemento) for elemento in mi_lista_mezcla]

#-- You can create another list filtering the original list
nueva_lista_numerica = list([]) #-- Create an empty list 
nueva_lista_booleana = list([])
nueva_lista_other = list([])
for elemento in mi_lista_mezcla:
        if str(elemento).isnumeric(): #-- Check if the element is numeric
            nueva_lista_numerica.append(elemento)
        elif (elemento == True or elemento == False): #-- Check if the element is boolean
            nueva_lista_booleana.append(elemento)
        else:
            nueva_lista_other.append(elemento)
                       
print(nueva_lista_numerica)
print(nueva_lista_booleana)
print(nueva_lista_other)

#-- Let's do the same thing with one line of code using List Comprehension
#-- Syntax of List Comprehension is
#-- newlist = [expression for item in iterable if condition == True]
#-- The condition is like a filter that only accepts the items that valuate to True.
#-- The iterable can be any iterable object, like a list, tuple, set etc.
#-- The expression is the current item in the iteration, but it is also the outcome, 
#    which you can manipulate before it ends up like a list item in the new list:

nueva_lista_numerica.clear() #-- Emtpies the list 
nueva_lista_booleana.clear()
nueva_lista_other.clear() 

nueva_lista_numerica10 = [(elemento * 10) for elemento in mi_lista_mezcla if str(elemento).isnumeric()]
nueva_lista_booleanaNot = [not(elemento) for elemento in mi_lista_mezcla if (elemento == True or elemento == False)] #-- I get a "bug"
nueva_lista_other = [elemento for elemento in mi_lista_mezcla if not(str(elemento).isnumeric())]

print("#--- List comprehension")
print(mi_lista_mezcla)
print(nueva_lista_numerica10)
print(nueva_lista_booleanaNot)
print(nueva_lista_other)

#---  SORT LIST ############################



