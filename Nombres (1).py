#Escribir un programa que pregunte el nombre del usuario
#  en la consola y un número entero
 #e imprima por pantalla 
#en líneas distintas el nombre del usuario tantas
#  veces como el número introducido.



nombre = input("¿como te llamas?") 

apellido = input("¿Cual es tu apellido?")

num = input ("Introduce un numero entero")

print((nombre.lower() + " " + apellido + "\n") * int (num))  #imprime  el valor multiplicado 


