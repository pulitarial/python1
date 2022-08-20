from pydoc import text


totalEmpleado1=0
totalEmpleado2= 0
empleado1= (input("Ingrese nombre del empleado 1:"))
monto1= int(input("Ingrese montos de facturas"))
while monto1 != 0:
    totalEmpleado1= totalEmpleado1 + monto1
    monto1= int(input("Ingrese siguiente:"))

empleado2= (input("Ingrese nombre empleado 2:"))
monto2= int(input("Ingrese montos de facturas"))
while monto2 != 0:
    totalEmpleado2= totalEmpleado2 + monto2
    monto2= int(input("ingrese siguiente:"))
if totalEmpleado1 > totalEmpleado2:
    print("Mayor total acumulado:", empleado1, "con", totalEmpleado1)
else:
    print("Mayor total acumulado:", empleado2, "con", totalEmpleado2)

input()