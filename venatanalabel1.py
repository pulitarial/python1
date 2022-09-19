import tkinter as tk

ventana= tk.Tk()
ventana.title("Label 1")
ventana.geometry("300x300")
ventana.minsize(100,100)  #define valores minimos para lla ventana

mi_label= tk.Label(ventana, text= "Hola Mundo")   #agrego txt a la ventana
mi_label.pack()

ventana.mainloop()