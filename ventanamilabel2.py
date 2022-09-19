import tkinter as tk

ventana= tk.Tk()
ventana.title("Label 1")
#ventana.geometry("300x300")
#ventana.minsize(100,100)  #define valores minimos para lla ventana

mi_label= tk.Label(ventana, text= "Hola Mundo")   #agrego txt a la ventana
mi_label.pack()
mi_label.config(bg= "white", fg= "red")   #configuro colores
mi_label.config(font=("Arial", 20))  #defino estilo de letra y tamaño
mi_label.config(padx=30, pady=40)   #le doy margenes x= horizontal e Y= vertical


ventana.mainloop()