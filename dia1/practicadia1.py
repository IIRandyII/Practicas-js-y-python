"""
Información personal
Guarda:
nombre
edad
altura
si te gusta programar
Imprime todo en una sola oración.
nombre = "Randy"
edad = 22
altura = 1.78
teGustaProgramar = "Si me gusta programar"

print("Mi nombre es", nombre, 
      "y tengo",edad, "años",
      "y mido", altura, "y", teGustaProgramar)

edad = int(input("Cual es tu edad: ")) + 5
print(edad)

Operaciones matemáticas
Con dos números:
suma
resta
multiplicación
división
módulo
number1 = 10
number2 = 5

suma = number1 + number2
resta = number1 - number2
multiplicacion = number1 * number2
division = number1 / number2
modulo = number1 % number2
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)

Área de un triángulo
Pide:
base
altura
base = int(input("Dame la base: "))
altura = int(input("Dame la altura: "))
area = base * altura / 2
print(area)

Acceso al sistema
El usuario puede entrar si:
tiene más de 18
y tiene contraseña correcta

ingresar = input("Contraseña: ")
contraseña = ingresar
edad = 18

if edad >= 18 and contraseña == "hola123":
    print("Puedes ingresar")
    
Una persona obtiene descuento si:
es estudiante
o tiene más de 60 años

estudiante = True
edad = 50
if estudiante == True or edad > 60:
    print("Obtienes un descuento")

Verificar rango
Pide un número y verifica si está entre 10 y 50

numero = int(input("Ingresa un numero: "))
if numero >= 10 and numero <= 50:
    print("Tu numero si esta entre el 10 y 50")
else:
    print("tu numero no esta entre el 10 y 50")
     """