/*Variables y Tipos de Datos

//Ejercicio 1
//Crea una variable llamada nombre y guarda tu nombre.

let nombre = "Randy";
console.log(nombre);

//----------------------------------------------------------------------------------
//Ejercicio 2
//Crea variables para:
//edad
//altura
//peso
//e imprime todo con console.log().

let edad = 22;
let altura = 1.78;
let peso = 80;

console.log(edad);
console.log(altura);
console.log(peso);
//----------------------------------------------------------------------------------
//Ejercicio 3
//Guarda:
//un texto
//un número
//un booleano
//Luego imprime el tipo usando typeof.

let texto = "Hola";
let numero = 10;
let es_Hombre = true;

console.log(typeof texto);
console.log(typeof numero);
console.log(typeof es_Hombre);
//----------------------------------------------------------------------------------
//Ejercicio 4
//Crea dos variables:
//let nombre = "Ana";
//let edad = 22;
//Imprime:
//Hola Ana, tienes 22 años

let name = "Ana";
let age = 22;
console.log("Hola " + name + " tienes " + age + " años");
//----------------------------------------------------------------------------------
//Ejercicio 5
//Crea variables de todos los tipos:
//string
//number
//boolean
//null
//undefined
//e imprime cada una.
let texto = "hola123";
let numero = 19;
let esProgramador = true;
let nada = null;
let hola 
console.log(texto);
console.log(numero);
console.log(esProgramador);
console.log(nada);
console.log(hola);
//-----------------------------------------------------------------------------
//Operadores
//Ejercicio 1
//Crea dos números y muestra:
//suma
//resta
//multiplicación
//división

let numero1 = 10;
let numero2 = 12;

let suma = numero1 + numero2;
let resta = numero1 - numero2;
let multiplicacion = numero1 * numero2;
let division = numero1 / numero2;

console.log(suma);
console.log(resta);
console.log(multiplicacion);
console.log(division);
//-----------------------------------------------------------------------------
//Ejercicio 2
//Pide dos números y muestra el residuo %.

let number1 = 20;
let number2 = 6;

let residuo = 20 % 6;
console.log(residuo);
//-----------------------------------------------------------------------------
//Ejercicio 3
//Comprueba si un número es mayor que otro.

let numeroMayor = 30;
let numeroMenor = 8;

if (numeroMayor > numeroMenor) {
    console.log("El numero " + numeroMayor + " es mayor que " + numeroMenor);
}
//-----------------------------------------------------------------------------
//Ejercicio 4
//Crea:
//let edad = 17;
//Comprueba si es mayor o igual a 18.

let edad = 17;
if (edad >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}
//-----------------------------------------------------------------------------
//Ejercicio 5
//Crea:
//let usuario = "admin";
//let password = "1234";
//Comprueba si ambos son correctos usando &&.
let usuario = "admin";
let password = "1234";

if (usuario === "admin" && password === "1234") {
    console.log("Usuario y contraseña correctos");
} else {
    console.log("Usuario y contraseña incorrectos");
}

//-----------------------------------------------------------------------------
//Condicionales
//Ejercicio 1
//Verifica si una persona es mayor de edad.

let edad = 18;
if (edad >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");    
}
//-----------------------------------------------------------------------------
//Ejercicio 2
//Comprueba si un número es positivo o negativo.

let numero = 5;
if(numero >= 0) {
    console.log("El numero es positivo");
} else {
    console.log("El numero es negativo");    
}

//-----------------------------------------------------------------------------
//Ejercicio 3
//Pide una contraseña y verifica si es correcta.

let password = "hola123";

if (password === "hola123") {
    console.log("La contraseña es correcta");
} else {
    console.log("la contraseña es incorrecta");
}

//-----------------------------------------------------------------------------
//Ejercicio 4
//Verifica si un número es par o impar.

let numeropar = 4;

if (numeropar % 2 === 0) {
    console.log("El numero es par");
} else {
    console.log("El numero es impar");
}
//-----------------------------------------------------------------------------
//Ejercicio 5
//Crea un sistema de calificaciones:
//90-100 → Excelente
//70-89 → Aprobado
//menos de 70 → Reprobado

let calificacion = 69;

if (calificacion >= 90 && calificacion <= 100) {
    console.log("Excelente");
} else if (calificacion >= 70 && calificacion <= 89) {
    console.log("Aprobado");
} else if (calificacion < 70) {
    console.log("Reprobado");
}

//-----------------------------------------------------------------------------
//Arrays
//Ejercicio 1
//Crea un array con 5 frutas e imprime la primera.

let array = ["manzana", "uva", "piña", "naranja", "pera"];

console.log(array[0]);
//-----------------------------------------------------------------------------
//Ejercicio 2
//Crea un array de números e imprime el último elemento.
let array2 = [21, 20, 18, 46, 79];

console.log(array2[4]);

//-----------------------------------------------------------------------------
//Ejercicio 3
//Agrega un nuevo elemento usando push().
let array3 = [21, 20, 18, 46, 79];

array3.push(1);
console.log(array3);
//-----------------------------------------------------------------------------

//Ejercicio 4
//Elimina el último elemento usando pop().

let array4 = [21, 20, 18, 46, 79];

array4.pop(5);
console.log(array4);
//-----------------------------------------------------------------------------

//Ejercicio 5
//Recorre un array e imprime todos los elementos usando for.

let array5 = ["manzana", "uva", "piña", "naranja", "pera"];

for(let i = 0; i < array5.length; i++) {
   console.log(array5[i]);
}

//-----------------------------------------------------------------------------
//While
//Ejercicio 1
//Imprime números del 1 al 10 usando while.
let numero = 1;

while (numero <= 10) {
    console.log(numero);
    numero++;
}

//-----------------------------------------------------------------------------
//Ejercicio 2
//Imprime números del 10 al 1.
let numero2 = 10;

while (numero2 >= 1) {
    console.log(numero2);
    numero2--;
}

//-----------------------------------------------------------------------------
//Ejercicio 3
//Suma los números del 1 al 5 usando while.
let numero5 = 1;
let suma = 0;

while (numero5 <= 5) {
    suma = suma + numero5;
    numero5++;
}

console.log(suma);
//-----------------------------------------------------------------------------
//Ejercicio 4
//Recorre un array de nombres usando while.
let nombres = ["Ana", "Luis", "Carlos", "Maria"];
let i = 0;

while (i < nombres.length) {
    console.log(nombres[i]);
    i++;
}

//-----------------------------------------------------------------------------
//Ejercicio 5
//Cuenta cuántos elementos tiene un array usando while.
let frutas = ["manzana", "pera", "uva", "melon"];
let i = 0;
let contador = 0;

while (i < frutas.length) {
    contador++;
    i++;
}

console.log(contador);
//-----------------------------------------------------------------------------
*/