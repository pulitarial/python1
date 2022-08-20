#leer numeros enteros de tecado hasta que el usuario ingrese el cero, finalmente mostrar la sumatoria de todos los numeros ingresados

total= 0
nro = int(input("Ingrese numero"))

while nro != 0:
    total= total + nro
    nro= int(input("ingrese numero:"))
print("el total acumulado es", total)

input()