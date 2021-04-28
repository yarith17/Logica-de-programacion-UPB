#TALLER DE PRACTICA
#Yarith Fernanda Espitia Ortiz
#Ejercicio 1
nombre = "Yarith"
calificativo=str(input("Ingresa un calificativo: "))
print(nombre, calificativo)

#Ejercicio 2
numero = int(input("Ingrese un numero: "))
print("El cuadrado de " + str(numero) + " es: " + str(numero*numero))

#Ejercicio 3
n1=float(input("Introduzca un número: "))
n2=float(input("Introduzca un número: "))
suma=n1+n2

print("La suma de los numeros es: ",suma)

#Ejercicio 4
n1=int(input("Introduzca un número: "))
n2=int(input("Introduzca un número: "))
suma=(n1+n2)
resta=(n1-n2)
multiplicacion=(n1*n2)
division=(n1/n2)
residuo=(n1%n2)
print("suma", suma, "resta", resta, "multiplicacion", multiplicacion, "division", division, "residuo", residuo)

#Ejercicio 5
import math
numero = float(input("Ingresa un numero decimal: "))
print("El número es: ", numero)
parte_decimal, parte_entera = math.modf(numero)
print("Su parte entera es {} y su parte decimal es {}".format (parte_entera, parte_decimal))

#Ejercicio 6
p1 = 0.15
p2 = 0.15
p3 = 0.20
p4 = 0.20
p5 = 0.30
count = 1
while 0 <= 5:
    i = 0
    if count == 1:
            nota1 = float(input("ingresa la nota numero 1: "))
            i = nota1
    elif count ==2:
            nota2 =float(input("ingresa la nota numero 2: "))
            i = nota2
    elif count == 3:
            nota3 =float(input("ingresa la nota numero 3: "))
            i = nota3
    elif count == 4:
            nota4 =float(input("ingresa la nota numero 4: "))
            i = nota4
    elif count == 5:
            nota5 =float(input("ingresa la nota numero 5: "))
            i = nota5

    if i > 0 and  i <= 5:
            count = count + 1
    if count == 6:
            break

resultado = (nota1*p1) +( nota2*p2) +( nota3*p3) + (nota4*p4) +(nota5*p5)
print ("Su nota definitiva es: " , resultado)

#Ejercicio 7
precio = float(input("ingrese el valor del producto: "))
iva = (precio  * 0.19)
total = (precio + iva)
print(" El valor del producto es: ",precio, "\n","El valor del iva es: ",iva,"\n", "El valor total a pagar con iva incluido es: ",total)

#Ejercicio 8
import math
radio =float(input("Ingresa el valor del radio del circulo(en metros): "))
area = math.pi * pow(radio,2)
perimetro = 2 * math.pi * radio
print(" El valor del area  es: ", area, "M^2\n", "El valor del perimetro es: ", perimetro, "M^2")

#Ejercicio 9
lado = float(input("ingresa el valor de un lado del hexagono(en centimetros):"))
apotema = float(input ( "ingresa el valor del apotema del hexagono( en centimetros):6"))
area =  ((lado * 6)* apotema )/2
print("el valor del area es = ",area ,"cm")

#Ejercicio 10
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))
resultado = (num1 + num2 + num3) / 3
print ("El promedio de los numeros es: ",resultado)

#Ejercicio 11
a = int(input("ingresa un numero: "))
b = int(input("ingresa un numero: "))
print("El valor de A es: ",a)
print("El valor de B es: ",b)
temporal = a
a = b
b = temporal
print("Al intercambiar los valores\n" "A es: ",a, "\nB es: ",b)

#Ejercicio 12
import math
gravedad = 9.81
altura = float(input("Ingrese la altura desde la cual es lanzado el objeto( en metros ): "))
tiempo = math.sqrt ((2*altura)/gravedad)
print ("El tiempo de caida del objeto es de: ",tiempo,"segundos")

#Ejercicio 13
aceleracion = float(input("ingresa el valor de la aceleracion ( en m/s^2): "))
velocidad = float(input("ingresa el valor de la velocidad en ( en m/s): "))
tiempo = aceleracion / velocidad
distacia = (aceleracion * tiempo )/2
print("la distancia recorrida del objeto es: ",distacia)

#Ejercicio 14
aceleracion = float(input("ingresa el valor de la aceleracion (en m/s^2): "))
tiempo = float(input ("ingresa el valor del tiempo (en seg ): "))
velocidad_final = 0 + aceleracion * tiempo
print("la velocidad final del objeto es de: " , velocidad_final,"m/s")

#Ejercicio 15
masa = float(input("ingresa la masa del objeto( en kg): "))
velocidad = float(input("ingresa la velocidad del objeto( en m/s): "))
Energia = (masa * pow(velocidad,2))/2
print("El valor de la energia del objeto es de: ",Energia ,"julios")

#Ejercicio 16
import math
x1=float(input("Ingresar el valor de x1: "))
y1=float(input("Ingresar el valor de y1: "))
x2=float(input("Ingresar el valor de x2: "))
y2=float(input("Ingresar el valor de y2: " ))
distancia =  math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("La distancia entre las coordenadas es: ",distancia)

#Ejercicio 17
segundos = float(input("ingresa los segundos que quieres pasar a horas: "))
horas = segundos / 3600
print(segundos, "segundos" , "son", horas,"horas")

#Ejercicio 18
segundos = float(input("ingresa los segundos que quieres pasar a minutos: "))
minutos = segundos / 60
print(segundos, "segundos" , "son", minutos,"minutos")

#Ejercicio 19
numero=int(input("ingrese los segundos: "))
hora=(int(numero/3600))
minutos=int((numero-(hora*3600))/60)
segundos=numero-((hora*3600)+(minutos*60))
print(str(hora),"h:",str(minutos),"m:",str(segundos),"s")

#Ejercicio 20
cantidad = int(input("Ingresa una cantidad de dinero (pesos colombianos): "))
denominaciones = [100000,50000,20000,10000,5000,2000,1000]
for i in denominaciones:
    if cantidad >= i:
        desglosado = cantidad // i
        print(str(desglosado) ,"billetes de "+ str(i) + " mil pesos ")
        cantidad = cantidad % i

#Ejercicio 21
n=input("Ingresa un numero de 4 cifras: ")
print("El numero ingresado es: ",n)
n2=n[::-1]
print("El numero ingresado de manera inversa es:", n2)

#Ejercicio 22
a = int(input("Ingresa un numero: "))
if a % 2 == 0:
    print('El número', a, 'es par.')
else:
    print('El número', a, 'es impar.')

#Ejercicio 23
a =float(input("Ingresa un numero: "))
if a < 0 :
    print("El numero",a, "es negativo")
else:
    print("El numero",a, "es positivo")

#Ejercicio 24
num =float(input("ingresa un numero: "))
if num < 0 and num % 2 == 0 :
    print(num,"Es negativo par")
elif num < 0 and num % 2 != 0 :
    print(num,"Es negativo impar")
elif num > 0 and num % 2 == 0 :
    print(num,"Es positivo par")
elif num > 0 and num % 2 != 0 :
    print(num,"Es positivo impar")

#Ejercicio 25
precio = float(input("ingresa el valor del producto: "))
iva = precio  * 0.19
descuento = precio * 0.05
if precio <= 150.000:
    precio = precio + iva
    print(precio,"Total a pagar")
elif precio > 150.000 :
    precio = precio + iva
    total = precio - descuento
    print(total, "este es el precio a pagar con un descuento del 5% por compras mayores a 150.000 y este es el valor del descuento del producto",descuento)

#Ejercicio 26
num = float(input("ingresa un numero: "))
if num >= 10 :
    num = num * 3
    print("Triple del numero ingresado",num)
else:
    num = num /4
    print("Cuarta parte del numero ingresado", num)

#Ejercicio 27
p1 = 0.15
p2 = 0.15
p3 = 0.20
p4 = 0.20
p5 = 0.30
nota1=0
nota2=0
nota3=0
nota4=0
nota5=0
count = 1
while count <= 5:
    nota=float(input("Ingrese la nota: "+str(count)+ " : " ))
    print(nota)

    if count == 1:
            nota1 = nota * p1
    if count == 2:
            nota2 = nota * p2
    if count == 3:
            nota3 = nota * p3
    if count == 4:
            nota4 = nota * p4
    if count == 5:
            nota5 = nota * p5

    count=count+1

resultado = float(nota1 + nota2 + nota3 + nota4 + nota5)
if resultado < 3:
    print("Nota: ",resultado,"Reprobaste")
elif resultado >= 3:
    print("Nota: ",resultado,"Aprobaste")
elif resultado > 4.5:
    print("Nota: ",resultado,"Excelente aprobaste, tuviste una muy buena nota")

#Ejercicio 28
num1 = float(input("ingresa un numero: "))
num2 = float(input("ingresa un numero: "))
if num1 > num2 :
    print("Numero mayor: ",num1,"\nNumero menor: ",num2)
if num1 < num2 :
    print("Numero mayor: ",num2,"\nNumero menor: ",num1)

#Ejercicio 29
num=int(input("Ingresa un numero: "))
print(float(num))

#Ejercicio 30
numeros = []
for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)
menor = numeros[0]
mayor = numeros [0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
print("El numero menor es: ", menor, "\nEl numero mayor es: ",mayor)

#Ejercicio 31
numero_1=int(input("ingresa un numero: "))
numero_2=int(input("ingresa un numero: "))
numero_3=int(input("ingresa un numero: "))
suma = numero_1 + numero_2
if suma > numero_3:
    print("Suma de los dos primeros numeros: ",suma,"(es mayor que el tercer numero)")
else:
    print("Suma de los dos primeros numeros: ",suma,"(es menor que el tercer numero)")

#Ejercicio 32
print("Si viajas mas de 1000 km y mas de 7 dias obtienes un descuento del 15%")
distancia = float (input("Ingresar la cantidad de km que va viajar: "))
dias = int(input("Ingresar la cantidad de dias que viajara: "))
precio = distancia * 5000
descuento = precio * 0.15
if distancia > 1000 and dias > 7 :
    print("Has obtenido un descuento del 15%")
    precio = precio - descuento
    print(precio)
if precio < 100000 or distancia < 20:
    print("No es posible, La cantidad minima para poder realizar el vuelo es de 20 km... ")
else:
    print("El costo de tu viaje es: ",precio)

#Ejercicio 33
año = int(input("Ingresa el año:"))
if año % 4 == 0  and año % 100 != 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
if año % 400 == 0:
    print("Es un año bisiesto")

#Ejercicio 34
from math import sqrt
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))
determiante =(( b**2)-4*a*c)
if determiante > 0:
    x_1 = -b+sqrt(b**2-4*a*c)/(2*a)
    x_2 = -b-sqrt(b**2-4*a*c)/(2*a)
    print(x_1, x_2)
elif determiante == 0:
    x_1 = -b / ("2 * a")
    print (x_1)
elif determiante < 0:
    print("la solucion de la ecuacion es con numeros complejos")

#Ejercicio 35
print("Usuario: User123 Contraseña: 12345 ")
print("Inicia sesion:")
while True:
    user = str (input("Ingresa el usuario: "))
    password = int(input("Ingresa la contraseña: "))
    if user == "User123" and password == 12345:
        print("Has iniciado sesion exitosamente", user)
        break
    else:
        print("Datos incorrectos, ingresa nuevamente")

#Ejercicio 36
numeros = ["0->cero","1->uno","2->dos","3->tres","4->cuatro","5->cinco","6->seis","7->siete","8->ocho","9->nueve","10->diez"]
n = int(input ("ingresa un numero del 1 al 10: "))
if n >= 0 and n <= 10:
    print(numeros[n])
else:
    print("ingresa un numero entre 1 y 10")

#Ejercicio 37
n = int(input("ingresa un numero(no mayor a 100.000: "))
cont = 0
while n > 0:
    if n < 100000:
        n //= 10
        cont = cont + 1
    else:
        print("Ingrese un numero menor a 100.000")
print("El numero ingresado tiene",cont,"digitos")

#Ejercicio 38
n1 = int(input("ingresa un numero: "))
n2 = int(input("ingresa un numero: "))
n3 = int(input("ingresa un numero: "))
if n1 < n2 < n3 :
    print("La secuencia de numeros se esta incrementando")
elif  n1 > n2 > n3:
    print("La secuencia de numeros se estan disminuyendo")
else :
    print("La secuencia de numeros ni se incrementan ni se disminuyen")

#Ejercicio 39
numero = int(input("ingresa un numero: "))
numero2= int(input("ingresa un numero: "))
if numero <= 5 and  numero  > 0:
    if numero2 <= 5 and  numero2  > 0:
        print("True")
    else:
        print("false")

#Ejercicio 40
dias = [0,"1-->lunes","2-->martes","3-->miercoles","4-->jueves","5-->viernes","6-->Sabado","7-->Domingo"]
dia = int(input(" presiona 1 : para iniciar \n presiona 0 : para finalizar\n"))
while dia != 0 :
    try:
        dia = int(input("Ingresa un dia de la semana (1 a 7) y (0 para salir): "))
        if dia != 0:
            if dia < 0 or dia > 7 :
                print("Ingresa un numero entre 1 y 7")
            elif dia > 0 and dia <=5:
                temp ="."
                print("Es {0} {1}".format(dias[dia],temp))
            elif dia == 6 or dia == 7:
                print("Es festivo")
        else:
            print("Fin")
    except:
            print("Ingresa un valor valido")

#Ejercicio 41
n1=int(input("Ingrese un numero por favor: "))
n2=int(input("Ingrese un numero por favor: "))
n3=int(input("Ingrese un numero por favor: "))

if n1 == n2 :
    print(n1, "y",n2, "son iguales")
elif n1 == n3 :
    print(n1, "y",n3, "son iguales")
elif n2 == n3 :
    print(n2, "y",n3, "son iguales")
else:
    print("No son iguales ninguno de los numeros")

#Ejercicio 42
for i in range (10):
    print(i,"Es un numero natural")

#Ejercicio 43
for i in range(20):
    if i % 2 != 0:
        print(i)

#Ejercicio 44
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#Ejercicio 45
n=int(input("Ingresa un numero: "))
for i in range (n):
    print(i)

#Ejercicio 46
n = int(input("ingresa un numero: "))
for i  in range(1,n):
    if i % 2 == 0:
        i = i - (2*i)
    print(i)

#Ejercicio 47
print("El primer numero debe ser menor al segundo")
n = int(input("ingresa un numero: "))
m =  int(input("ingresa un numero: "))
if n < m:
    for i in range(n,m):
        print(i)

#Ejercicio 48
print("El primer numero debe ser menor al segundo")
n = int(input("ingresa un numero: "))
m =  int(input("ingresa un numero: "))
total=0
if n < m:
    for i in range(n,m):
        total=total+i
        print(total)

#Ejercicio 49
sumatoria=0
promedio=0
count=1
while True:
    numero=int(input("Ingresa un numero: "))
    sumatoria=sumatoria+numero
    count=count+1
    if count==11:
        break
promedio=sumatoria/10
print("La suma de los numeros ingresados es: ",sumatoria)
print("El promedio de los numeros ingresados es: ",promedio)

#Ejercicio 50
n=int(input("Ingresa n numeros para calcular la suma y el promedio: "))
sumatoria=0
promedio=0
count=1
while True:
    numero=int(input("Ingresa un numero: "))
    sumatoria=sumatoria+numero
    count=count+1
    if count==n+1:
        break
promedio=sumatoria/10
print("La suma de los numeros ingresados es: ",sumatoria)
print("El promedio de los numeros ingresados es: ",promedio)

#Ejercicio 51
suma_impares,suma_pares = 0,0
cont1,cont2 = 0,0
while True:
    n = int(input("Ingresa los numeros :  "))
    if n == 0:
        break
    if n % 2 == 0:
        suma_pares = suma_pares + n
        cont1 = cont1  + 1
        promedio = suma_pares / cont1
    elif n % 2 != 0 :
        suma_impares = suma_impares + n
        cont2 = cont2 + 1
        promedio2 = suma_impares / cont2
print("El promedio de los numero pares es: ",promedio,"\nEl promedio de los numeros impares es", promedio2)

#Ejercicio 52
while True:
    n = int(input("ingresa un numero positivo: "))
    if n > 0:
        print(n)
        break
    else:
        print("ingresa un numero positivo valido")

#Ejercicio 53
def pidenumero():
    lista=[]
    while True :
        n =int(input("ingresa una cantidad de numeros y 0 para terminar: "))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista

def mayorMenor(lista):
    cont = 0
    contt = 0
    for i in lista:
        if i > 100:
            cont = cont + 1
        if i < 100:
            contt = contt + 1
    return cont ,contt

lista =pidenumero()
cont,contt= mayorMenor(lista)
print(cont, " son los numeros mayores a 100 y",contt, "son los numeros menores a 100")

#Ejercicio 54
def pidenumero():
    lista = []
    while True:
        n = float(input("Ingresa una cantidad de numeros y 0 para terminar: "))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista

def parImpar(lista):
    cont = 0
    contt = 0
    for i in lista:
        if i % 2 == 0:
            cont = cont + 1
        elif i % 2 != 0:
            contt = contt + 1
    return cont, contt

def me0Ma0(lista):
    me0 = 0
    ma0 = 0
    for j in lista:
        if j > 0:
            ma0 = ma0 + 1
        else:
            me0 = me0 + 1
    return me0, ma0

def multiplo8(lista):
    mult8 = 0
    for k in lista:
        if k % 8 == 0:
            mult8 = mult8 + 1
    return mult8

lista = pidenumero()
cont, contt = parImpar(lista)
me0, ma0 = me0Ma0(lista)
mult8 = multiplo8(lista)

print(cont, "son pares y ",contt, "son impares")
print(ma0, "son mayores a 0 y ",me0, "son menores a 0")
print(mult8, "son multiplos de 8")

#Ejercicio 55
def pidenumero():
    lista = []
    while True:
        n = float(input("Ingresa los numeros(0 para salir): "))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista

def parImpar(lista):
    cont = 0
    contt = 0
    for i in lista:
        if i % 2 == 0:
            cont = cont + 1
        elif i % 2 != 0:
            contt = contt + 1
    return cont, contt

def siEs5(lista):
    n5 = 0
    for k in lista:
        if k == 5:
            n5 = n5 + 1
    return n5

lista = pidenumero()
cont, contt = parImpar(lista)
n5 = cont+contt
print(cont, "son pares",contt, "impares","\nLa cantidad de numeros ingresados fueron: ",n5)

#Ejercicio 56
n = int(input("ingresa un numero: "))
for i in range(1,n+1):
    if n % i == 0:
        print(i)

#Ejercicio 57
cadena = str(input("ingresa una palabra: "))
print(cadena[::-1])

#Ejercicio 58
n = int(input("ingresa un numero: "))
s = 0
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end="")
    print()
