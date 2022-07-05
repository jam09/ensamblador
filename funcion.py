from tkinter import *

ventana= Tk()
ventana.title("Suma de numeros")
ventana.geometry("400x400")


def sumar():
    primero = int(caja1.get())
    segundo = int(caja2.get())
    sumar = (primero + segundo) 
    return variable1.set(sumar)
    suma()
variable1=StringVar()
etiqueta1=Label(ventana, text="suma del primer numero")
caja1=Entry(ventana, text="primer  numero")
caja2=Entry(ventana,text=" Segundo numero")
boton1=Button(ventana,text="SUMAR",command=sumar)
caja3=Entry(ventana,textvariable=variable1)

etiqueta1.pack()
caja1.pack()
caja2.pack()
boton1.pack()
caja3.pack()
ventana.mainloop()