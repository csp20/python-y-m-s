""" ej2
Uso de string (array de caracteres). Averiguar si una cadena es un palíndromo. 
Introducir sin espacios. (tenet, yosoy). Comparar 0 con ultima posición y sucesivamente.
"""
cadena = input("Introduce una cadena: ")
cadena = cadena.replace(" ", "")
es_palindromo = True
for i in range(len(cadena) // 2):
    if cadena[i] != cadena[-i - 1]:
        es_palindromo = False
        break

# Imprimir el resultado
if es_palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")