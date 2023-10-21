'''
Created on 17 oct 2023

Python Variables

@author: bmesa
'''

x = 5       # x es de tipo entero
y = "Tomeu" # y es de tipo string
print(x)
print(y)

# Podemos especificar el tipo de variable cuando se define
# La operación se denomina Casting

x = str(3) # x es un entero y vale 3
y = int(3) # y contiene el carácter 3
z = float(3) # z contiene el número real 3.0

print(x)
print(y)
print(z)

# También podemos consultar el tipo de una variable

print(type(x))
print(type(y))
print(type(z))

# Las cadenas de carácters se pueden escribir con comillas simples o compuestas

x = 'Tomeu Sabater'
print(x)
x = "Tomeu Sabater"
print(x)
x = "Ca'n Nadal"
print(x)
x = "La \"x\" sueler ser una variable"
print(x)

# Los nombres de la variables son Case-Sensitive
a = int(5) # a minúscula no es A
A = int(15) # A mayúscula no es a

print(a)
print(A)

# Y tendremos cuidado porque los nombres de la variables son diferentes
# por tanto, las variables son diferentes

Total = int(5)
Total = 10
print(Total)
total = 0
print(Total)

# Nombres de las Variables en Python
Variable = int(5)
_Variable = int(10)
Total_sin_descuento = int(0)
Total_con_descuento = int(0) 
# 9Variable = int(0) No puede comenzar con un número 
Variable_1 = int(20)
# print = int(20) Una variable no puede ser una palabra reservada  
# $Total = int(10) No puede comenzar con un símbolo  

print(Variable)
print(_Variable)
print(Variable_1)
print(Total_sin_descuento)
print(Total_con_descuento)

#Recomendación para los nombres de la variables
Totalsindescuento = int(0) # Válido pero no es la mejor solución 
Total_sin_descuento = int(20) # Buen ejemplo con Snake Case
TotalConDescuento = int(30) # Otro buen ejemplo fácil de leer con Pascal Case

print(Totalsindescuento)
print(Total_sin_descuento)
print(TotalConDescuento)

# Asignación múltiple de variables
x, y, z = 1, 2, 3 # Asignación de 3 valores a 3 variables 
x, y ,z = int(1), int(2), int(3) # Asignación de 3 valores a 3 variables
print(x)
print(y)
print(z)

x = y = z = int(99) # Asignación de un unico valor a varias variables
print(x)
print(y)
print(z)

# Desempaquetar una colección 
frutas = ["manzana", "naranja", "pera"]
fruta_1, fruta_2, fruta_3 = frutas
print(fruta_1)
print(fruta_2)
print(fruta_3)

# Print multiple variables
print(fruta_1, fruta_2, fruta_3)
print(fruta_1 + fruta_2 + fruta_3)
print(fruta_1 + ' ' + fruta_2 + ' ' + fruta_3)

# Print con + en variables numéricas es una operación matemática
x = str(99)
y = str(99)
z = str(99)
print(x + y + z) # Imprime la suma no la concatenación

x = int(0) # Number 0
y = str(0) # Caracter '0' 
# print(x + y) # Dará un error puesto que aplicas '+' a 2 tipos distintos
print(x,y)

# GLOBAL VARIABLES ####################################################################################

# Definimos e inicializamos una variable de tipo string
x = str("Tomeu es increiblemente malo")

# Definimos una función 
def myFuncion():
    x = str("Tomeu es increiblemente bueno") # Definimos una variable local
    print(x) # Imprime la variable x
    
myFuncion() # Llamamos a la función e imprimirá la variable local
print(x) # Imprimimos el valor de x 

# Definimos una función con una variable global
y = str("No me gusta la programación")

def myFuncion2():
    global y  # La definimos como global 
    y = str("Si que me gusta programar") # La inicializamos
    print(y) # La imprimimos

myFuncion2() # llamamos a myFuncion2
print(y) # Imprimimos la variable gobal 

