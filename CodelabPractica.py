nombre = "Sharony"
edad = 22
estatura = 1.70
saludable = True

nombre = "Mi nombre es " + nombre + ", mi edad " + str(edad) + ", y mi estatura " + str(estatura) + ". Soy saludable? " + str(saludable)
nombre = nombre
print(nombre)

# Si hablamos de python version 3, la variable int no tiene limite maximo
# Cuando hablamos de float, con el siguiente codigo podemos encontrar el minimo y maximo
import sys
print(sys.float_info.min) #2.2250738585072014e-308
print(sys.float_info.max) #1.7976931348623157e+308

# Suma de los primeros numeros pares
n = 10
suma = n * (n+1)/2
suma = suma
print(suma)




