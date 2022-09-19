import tkinter as tk
from tkinter import font

ventana=tk.Tk()
ventana.title("Formulario Simple")
ventana.iconbitmap("pollo.ico")
ventana.config(bg="white", relief="flat")
ventana.geometry=("1000x1000")

mi_Label=tk.Label(ventana, text="Bienvenido")
mi_Label.grid(row=0, column=0)
mi_Label.config(font=("Arial", 20), bg="light grey")

mi_Label2=tk.Label(ventana, text="Cual es tu nombre")
mi_Label2.config(bg="white")
mi_Label2.grid(row=1, column=0)
mi_Entry2=tk.Entry(ventana)
mi_Entry2.config(justify="center",insertbackground="blue" )
mi_Entry2.grid(row=1, column=1)

mi_Label3= tk.Label(ventana, text="Cual es tu apellido:")
mi_Label3.config(bg="white")
mi_Label3.grid(row=2, column=0)
mi_Entry3=tk.Entry(ventana)
mi_Entry3.config(justify="center",insertbackground="yellow")
mi_Entry3.grid(row=2, column=1)

mi_Label4=tk.Label(ventana, text="Direccion:")
mi_Label4.config(bg="white")
mi_Label4.grid(row=3, column=0)
mi_Entry4=tk.Entry(ventana)
mi_Entry4.config(justify="center",insertbackground="blue")
mi_Entry4.grid(row=3, column=1)

ventana.mainloop()