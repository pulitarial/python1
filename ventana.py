import tkinter


import tkinter #importo toda la galeria

ventana = tkinter.Tk()  #creo el objeto ventana
ventana.title("Mi Primera Ventana")  #nombra a la ventana
ventana.geometry("500x300")  #da tamaño
ventana.config(bg="dark salmon", relief="groove", bd=10)  #personalizo el color de fondo, relieve y tamaño del borde


ventana.mainloop()  #muestro la ventana "en bucle"
