
'''

#2# ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código si el usuario introduce un 4?

x = input()
if x == 4:
    print("Hola")
else:
    print("Adios")


#3#  ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

x = 26
if x % 2 == 0:
    print("0")
else:
    print("1")


#4# ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

x = 17
y = 26
if x <= 17 or y > 40:
    print("1")
elif x < 17:
    print("2")
else:
    print("3")


#5# Cuántos # se mostrarán después de ejecutarse el siguiente fragmento de código

x = 7
if x != 10:
    print('#')
    if x < 8:
        print('#')
    elif x == 10:
        print("#")
    else:
        print("#")
else:
    print('#'*3)


#6# ¿Cuál será el resultado exacto de la siguiente operación?

float(4)


#7# ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código si el usuario introduce un 0?

import math
radio = float(input())
print(math.pi*radio**2,2*math.pi*radio)


#8# ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

x = 1
while x <= 4:
    x += 2
    print(x)


#9# Qué mostrará la consola después de ejecutarse el siguiente fragmento de código

x = 0
while x <= 3:
    print(x)
    x += 2
    


#10# ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

i = 1
j = 1
while i < 6:
    i += j + 1
    if i == 3:
        print(i)


# 11 # Qué mostrará la consola después de ejecutarse el siguiente fragmento de código

for i in range(10, 7, -1):
    print(i)


#12# Qué mostrará la consola después de ejecutarse 

for i in range(1,2,1):
    print(i)


# 13 # Qué mostrará la consola después de ejecutarse 

for i in range(15):
    print(i)

  
# 14 # Qué mostrará la consola después de ejecutarse el siguiente fragmento de código

i = range(7,15,2)
for j in i:
    print(j)

# 15 # Qué mostrará la consola después de ejecutarse el siguiente fragmento de código

for i in range(1):
    for j in range(2):
        print(i,j)
    

#16# Qué mostrará la consola después de ejecutarse el siguient fragmento de código

a= ["sistemas", "bases", "fol"]
for i in a:
    if "sistemas" in a:
        print(i)


#17# Qué mostrará exáctamente la consola después de ejecutarse el siguiente fragmento de código

li = [1,2,3,4]
print(li[1:3])

#18# Qué mostrará exáctamente la consola después de ejecutarse el siguiente fragmento de código

li = [1,2,3,4]
li[2] = 5
print(li)

#19# Qué mostrará exáctamente la consola después de ejecutarse el siguiente fragmento de código

li = [0,1,2,3]
a = len(li)
print(a)

#20# Qué mostrará exáctamente la consola después de ejecutarse el siguiente fragmento de código

li = [[1,2,3],[4,5,6],[7,8,9],['#',0,'@']]
print(li[2][1])


#21# Qué mostrará exáctamente la consola después de ejecutarse el siguiente fragmento de código

d = {1: "A", 2: "B"}
for v in d.values():
    print(v)


#22# Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código

futbolistas = {
    1 : "Casillas",15: "Ramos",3 : "Piqué",
    5 : "Puyol", 11: "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8: "Xavi Hernandez", 18 : "Pedrito",
    6 : "Iniesta", 7 : "Villa"
    }
keys = futbolistas.keys();
print(keys)


#23# Usando el diccionario “futbolistas”; 
# ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

print(len(futbolistas))


#24# Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código

def f(a, b=5):
    return a * b

print(f(2))
'''

#25# Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código

a = [1,2,3]
def f(a):
    s = 0
    for i in a:
        s += i 
    return s

print(f(a))


