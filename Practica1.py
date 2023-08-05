print("hola chango");     #prints

x = 12                    #ints no se declaran D:!!!!
print(x);                 #muestra el entero

y = 15.7                  #float
print(y);                 #muestra float

print(type(x));           #tipo de dato x
print(type(y));           #tipo de dato y

z = True;                 #boolean
print(z);                 #muestra z
print(type(z));           #tipo de dato z


#ejemplo calculadora:

g = 2
m = 4
print(g + m);           #suma
print(g - m);           #resta
print(g * m);           #multi
print(m / g);           #division
print(m ** g);          #potencia


#strings

nombre = "caro";
nombreCompleto = nombre + " pepo";

print(nombreCompleto);

print(nombre * 3);

#alterar string en mayus y minus

nombreMayus = nombre.upper();
nombreMinus = nombre.lower();

print(nombreMayus);
print(nombreMinus);


#condicionales


#Imput scanner de string y si quieres entero pones entre parentesis int y lo transforma.

age = int (input("ingrese su edad por favor:"));

if age < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad");


#operaciones dividir con conducional

num1 = int(input("Ingrese nro 1: "))
num2 = int(input("ingrese nro 2: "))

if (num2 == 0):
    print("No se puede dividir por 0")
else:
    print(num1 / num2)

#modulo %

if num1 % 2 == 0:
    print("El numero " + str(num1) + " es par")
else:
    print("El numero " + str(num1) + " no es par")

#mayor o menor

if num1 < num2:
    print(str(num2) + " es mayor");
elif num1 > num2:
    print(str(num2) + " es menor");
else:
    print("nro 1 y nro 2 son iguales");


#bucles repeticion

numero = int(input("ingrese numero: "))

while numero > 0:
    print(numero);
    numero = numero - 1;


#bucle suma mas complejos

flag = True

while flag == True:

    num1 = int(input("Ingrese primer numero de la suma: "))
    num2 = int(input("Ingrese segundo valor de la suma: "))
    suma = num1 + num2;
    print(str(num1) + " + " + str(num2) + " = " + str(suma));

    continuar = input("Desea realizar otra suma? Si (s) - No (n): ")

    if continuar == 'n':
        flag = False;

#tenemos break si no queremos usar

#for con lista

gustosLista = ["messi", "verde claro", "mate", "eclipse", "certant"]

for gusto in gustosLista:
    print(f"a chango le gusta: {gusto}")


#for range
#donde arranca, hasta donde (no incluye) y incremento

for numero in range (2, 30, 2):
    print(str(numero))


