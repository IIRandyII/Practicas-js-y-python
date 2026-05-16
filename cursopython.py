#COMENTARIOS CON # PARA UNA LINEA, """ PARA MULTIPLES LINEAS

"""
TIPOS DE DATOS: STRING, INT, FLOAT, BOOLEAN
EJEMPLOS: "TEXTO", 12, 1.6, TRUE


#NO HAY CONSTANTES EN PYTHON AL MENOS QUE LA VARIABLE ESTE EN MAYUS
#EJEMPLO: VARIABLE = "HOLA"   <--- ESTO SERIA UNA VARIABLE CONSTANTE

#PARA CONCATENAR UN RESULTADO NO REQUIERE EL +, SOLO COLOCAR ,

first_name = "Hola"
last_name = "Mundo"
print(first_name, last_name)


#operadores 
#== < > >= <= !=      (Boolean TRUE/FALSE)
numero1 = 10
numero2 = 20
resultado = numero1 == numero2
print(resultado)


#operadores LOGICOS
#AND, OR, NOT       <--- SIEMPRE BOOLEAN (TRUE/FALSE)
number1 = 10
number2 = 20
#ESTO SERIA UN OPERADOR AND TIENE QUE SER AMBOS TRUE
result = number1 < number2 and number2 >= number1 
print(result)
#CUANDO ES MUY LARGO EL RESULTADO SE PUEDE AGRUPAR CON ()

result = (number1 < number2 
          and number2 >= number1)
print(result)

#EL OR DARA TRUE SIEMPRE Y CUANDO EN LA OPERACION DE ALMENOS 1 TRUE
numero3 = 12
numero4 = 17
operacion = numero3 != numero4 or numero3 > numero4
print(operacion)
#Y EL NOT INVIERTE EL VALOR
numero5 = 12
numero6 = 17
operation = numero3 == numero4 or numero3 > numero4
print(operation)
------------------------------------------------------------------------------------

nombre = input("Cual es tu nombre: ")
edad = int(input("Cual es tu edad: "))
altura = float(input("Cual es tu altura: "))
activo = input("Estas activo: (yes/no)") == "yes" 

print(nombre)
print(edad)
print(altura)
print(activo)

#SE PUEDEN CREAR MULTIPLES VARIABLES EN UNA SOLA LINEA DE CODIGO

nombre, apellido, edad, es_Estudiante = "Randy", "Daniel", 22, True
print(nombre)
print(apellido)
print(edad)
print(es_Estudiante)
----------------------------------------------------------------------------------
LISTAS
<variable> = []
my_list = ["String", 10, 3.14, True, [1, 2, 3] ]
print(my_list)
print(type(my_list))
------------------------------------------------------------------------------------
INDICE      0           1       2           3       4
course = ["python", "Ruby", "mongodb", "django", "java"]

print(len(course))
value = course[0]
print(value)
-------------------------------------------------------------------------------------
SUBLISTA         #[start:end] [start:end:skip]
new_list = course[2:4]  inicio y fin   y si es course[::3] hace lo otro
print(new_list)

METODO APPEND HACE QUE AÑADA UN ELEMENTO A LA LISTA EJEMPLO course.append() Y INSERT ES PARA AÑADIR ALGO EN UNA POSICION EJEMPLO
course.insert(0, "PHP") Y PARA SABER SI HAY UN ELEMENTO EN LA LISTA ES CON PRINT Y SE COLOCA "ELEMENTO" O EL NUMERO O LO QUE SEA Y IN NOMBRE
DE LA LISTA Y LO MISMO PERO CON index para saber el numero de la posicion y remove para eliminar course.remove(elemento) y con .pop es para
quitar el ultimo elemento de la lista y .clear es resetear la lista
"""

