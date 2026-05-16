"""
#VARIABLES   
#Ejercicio 1
#Crea una variable llamada nombre y guarda tu nombre.
#Luego imprímelo.
nombre = "Randy"

print(nombre)
#-------------------------------------------------------------------
#Ejercicio 2
#Crea variables para:
#edad
#ciudad
#altura
#e imprímelas.

edad = 22
ciudad = "Cadereyta"
altura = 1.78

print(edad)
print(ciudad)
print(altura)
#-------------------------------------------------------------------
#Ejercicio 3
#Guarda dos números y muestra su suma.

numero1 = 10
numero2 = 20
print(numero1 + numero2)
#-------------------------------------------------------------------
#Ejercicio 4
#Crea una variable llamada mensaje y guarda:
#Hola Python
#Luego imprímela.

mensaje = "Hola Python"
print(mensaje)
#-------------------------------------------------------------------
#Ejercicio 5
#Crea variables para:
#nombre
#edad
#carrera
#e imprime:
#Me llamo Randy, tengo 20 años y estudio programación

name = "Randy"
age = 22
carrera = "Programación"

print("Me llamo",name, "Tengo",age, "años y estudio",carrera)
#-------------------------------------------------------------------
#TIPOS DE DATOS

#Ejercicio 1
#Crea:
#un string
#un int
#un float
#un boolean
#e imprime cada uno.

nombre = "Daniel"
edad = 22
altura = 1.78
esEstudiante = False

print(nombre)
print(edad)
print(altura)
print(esEstudiante)
#-------------------------------------------------------------------
#Ejercicio 2
#Usa type() para mostrar el tipo de:
#nombre
#edad
#altura

print(type(nombre))
print(type(edad))
print(type(altura))
#-------------------------------------------------------------------
#Ejercicio 3
#Crea una variable booleana llamada tiene_hambre.

tiene_hambre = True
print(tiene_hambre)
#-------------------------------------------------------------------
#Ejercicio 4
#Guarda un precio decimal y muéstralo.

precio = 1.99
print(precio)
#-------------------------------------------------------------------
#Ejercicio 5
#Crea variables de distintos tipos y muestra su tipo usando type().
print(type(nombre))
print(type(edad))
#-------------------------------------------------------------------

#OPERADORES
#Ejercicio 1
#Crea dos números e imprime:
#suma
#resta
#multiplicación
#división

numero1 = 10
numero2 = 20

suma = numero1 + numero2
resta = numero2 - numero1
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(suma)
print(resta)
print(multiplicacion)
print(division)
#-------------------------------------------------------------------
#Ejercicio 2
#Calcula el residuo de una división usando %.

numero_1 = 30
division = numero_1 / 2 % 4
residuo = division
print(residuo)
#-------------------------------------------------------------------
#Ejercicio 3
#Calcula una potencia usando **.

potencia = 2 ** 4
print(potencia)
#-------------------------------------------------------------------
#Ejercicio 4
#Crea:
#numero = 10
#y súmale 5.

numero_2 = 10
print(numero_2 + 5)
#-------------------------------------------------------------------
#Ejercicio 5
#Haz una calculadora básica con dos números.
number = int(input("Ingresa un numero: "))
number1 = int(input("Ingresa el segundo numero: "))
signo = "*"

if signo == "+":
    print(number + number1)
elif signo == "-":
        print(number - number1)
elif signo == "*":
        print(number * number1)
elif signo == "/":
        print(number / number1)
#-------------------------------------------------------------------
"""
#Operadores Lógicos
#Ejercicio 1
#Comprueba si un número es mayor que 10.

#-------------------------------------------------------------------
#Ejercicio 2
#Verifica si una persona es mayor de edad.

#-------------------------------------------------------------------
#Ejercicio 3
#Comprueba si un número es par usando %.

#-------------------------------------------------------------------
#Ejercicio 4
#Crea:
#usuario = "admin"
#password = "1234"
#Verifica si ambos son correctos usando and.

#-------------------------------------------------------------------
#Ejercicio 5
#Crea una variable:
#tiene_permiso = False
#Usa not para imprimir el valor contrario.

#-------------------------------------------------------------------