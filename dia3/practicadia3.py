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
Juego por puntuacion
"""
print("Bienvenido al juego de Minecraft")
print("Responde correctamente para ganar")

puntuacion = 0

opcion1 = input(
    "Pregunta 1 : ¿Que pasa si matas a un animal con una espada con aspecto ígneo?\n"
    "A - no pasa nada\n"
    "B - te dropea el item\n"
    "C - te dropea el item cocinado\n"
)

if opcion1 == "A":
    puntuacion += 0

elif opcion1 == "B":
    puntuacion += 10

elif opcion1 == "C":
    puntuacion += 15

else:
    print("Las opciones son solo A, B y C")

opcion2 = input(
    "Pregunta 2 : ¿Que se necesita para craftear una espada de madera?\n"
    "A - Nada\n"
    "B - 1 de madera y 1 palo\n"
    "C - 2 de madera, y 1 palo\n"
)

if opcion2 == "A":
    puntuacion += 0

elif opcion2 == "B":
    puntuacion += 10

elif opcion2 == "C":
    puntuacion += 15

else:
    print("Las opciones son solo A, B y C")

opcion3 = input(
    "Pregunta 3 : ¿Que item se ocupa para encontrar al end portal?\n"
    "A - ojos de araña\n"
    "B - blaze\n"
    "C - ojos de enderman\n"
)

if opcion3 == "A":
    puntuacion += 0
    
elif opcion3 == "B":
    puntuacion += 10

elif opcion3 == "C":
    puntuacion += 15

else:
    print("Las opciones son solo A, B y C")

print("Tu puntuacion final es: ", puntuacion)

if puntuacion <= 24:
    print("Que lastima, estas en nivel basico")

elif puntuacion <= 30:
    print("Enhorabuena, estas nivel medio")

else:
    print("Felicidades! Eres experto")