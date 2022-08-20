#ingresae caificacion
print("**Sistema de notas**")
nota= int(input("ingrese calificacion: "))

if nota>= 0 and nota <=3:
    print("Reprobado")
elif nota>= 4 and nota <=5:
    print("Regular")
elif nota >= 6 and nota <=10:
    print("Aprobado")
else:
    print("valor incorrecto")

input()