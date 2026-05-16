"""
#programa en el cual el usuario pueda introducir 3 números distintos y este responda
# con el número más pequeño y el más grande.
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))
d = max(a, b, c)
e = min(a, b, c)
print(d)
print(e)
#------------------------------------------------------------------------------------
#De Fahrenheit a Celsius!: Diseña un programa que indicando los grados Fahrenheit los transforme el Celsius.
#Fórmula de conversión: (X- 32)*5/9= Y
fahrenheit = int(input("Ingresa los grados fahrenheit: "))
celcius = (fahrenheit - 32) * 5/9
print(celcius)
#-----------------------------------------------------------------------------------------------
#De Libras a Euros!: Diseña un programa que realice el cambio de libras a euros. 
#Primero debe preguntar la cantidad de libras que queremos cambiar y después, 
#el valor de la conversión
libras = int(input("¿Cuanto es lo que desea cambiar a euros?: "))
euros = libras * 1.15
print(euros)
#-----------------------------------------------------------------------------------------------
#diseña un programa en el cual el usuario  tenga que adivinar un número dentro de una secuencia de 
#1 a 10. Cuando se pregunte al usuario cuál es el número que está dentro de la secuencia, en el caso 
#de que acierte debéis darle la enhorabuena al usuario por adivinar el número, si no acierta el número 
#se concluye el juego.
print("Adivina el numero")
import random
numero_aleatorio = random.randint(1, 10)
user = int(input("Ingresa un numero del 1 al 10: "))
if (user == numero_aleatorio):
    print("Felicidades, has adivinado el numero")
else:
    print("Has fallado")
#-----------------------------------------------------------------------------------------------
"""



