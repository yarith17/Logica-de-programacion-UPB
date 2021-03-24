print("EJERCICIO 1")
print(list(range(0,10)))
print("EJERCICIO 1")
for x in range(10):
    print(x)

print("EJERCICIO 2")
print(list(range(100,200)))
print("EJERCICIO 2")
for x in range(100,200):
    print(x)

print("EJERCICIO 3")
print(list(range(5,20,3)))
print("EJERCICIO 3")
for x in range(5,20,3):
    print(x)

print("EJERCICIO 4")
x=int(input("Numero positivo: "))
for x in range(x, x*2):
    print(x)

print("EJERCICIO 5-6")
vocal1= ''
vocal2= ''
vocal3= ''
vocal4= ''
vocal5= ''

def vocales(vocal):
    global vocal1
    global vocal2
    global vocal3
    global vocal4
    global vocal5
    if vocal=='a':
        vocal1='a'
    if vocal=='e':
        vocal2='e'
    if vocal=='i':
        vocal3='i'
    if vocal=='o':
        vocal4='o'
    if vocal=='u':
        vocal5='u'

frase=input("Ingrese una frase: ")
for n in frase:
    vocales(n)
if vocal1+vocal2+vocal3+vocal4+vocal5== "":
    print("No hay vocales en esta frase")
else:
    print("Las vocales de la frase ingresada son: " , vocal1+","+vocal2+","+vocal3+","+vocal4+","+vocal5 )

print("EJERCICIO 7")
Sum = 0
for x in range(0, 101, 1):
    Sum += x
    print(x)
print("La sumatoria total de todos los números es ", Sum)

print("EJERCICIO 8")
añoInicio=int(input("Año inicial:"))
añoFin=int(input("Año final:"))
for año in range(añoInicio, añoFin+1):
   if not año%10==0:
       continue
   if not año%4==0:
       continue
   if año%100!=0 or año%400==0:
       print(año)

print("EJERCICIO 9")
numeroentero=int(input("Número Entero Positivo: "))
f=1
if numeroentero!=0:
    for i in range(1,numeroentero+1):
        f=f*i
print("Factorial:", f)

print("EJERCICIO 10")
def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
for x in range(10):
    print(fib(x))


