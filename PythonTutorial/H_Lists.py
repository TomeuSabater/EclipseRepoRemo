'''
Created on 25 oct 2023

CESUR - Python Tutorial
@author: Tomeu Sabater
'''
#--- PYTHON LISTS #########################################################

#-- List items - Data Types ##################################
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


#-- Access Item ##################################
#-- List items are indexed and you can access them by referring to the index numer
print(mi_lista_texto[1]) #-- The index starts by 0, this prints the second element

print(mi_lista_texto[-1]) #-- Negative index means starts by the end
print(mi_lista_texto[-2])

#-- You can specify a range of indexes
print(mi_lista_mezcla[3:5]) #-- Last index is excluded. 
print(mi_lista_mezcla[3:]) #-- From the index 3 to the end
print(mi_lista_mezcla[:5]) #-- Until the index 5 excluded
print(mi_lista_mezcla[-4:-1]) #-- Remember, last item in a range is excluded 

#-- Check for an Item ########################################


