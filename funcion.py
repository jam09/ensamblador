#Escribir una función que convierta un 
#número decimal en binario 
#y otra que convierta un número
 #binario en decimal.
 #(a) 12 = 8 + 4 = 23 + 22    1 1 0 0

def d_ecimal(i):

     i = list(i)
     i.reverse()#contenedor de varible
     decimal = 0 #el decimal debe estar en cero 
     for i in range(len (i)):
        decimal += int(L[i]) * 2 ** i #funcion de multiplicacion de decimal
     return decimal 

     print(d_ecimal('1010'))

       









