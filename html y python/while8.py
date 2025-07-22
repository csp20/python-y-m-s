""" ej 8 
Uso de string(array de caracteres). Solicitar por pantalla una frase que puede tener letras tanto 
en mayúsculas como minúsculas. Contar la cantidad de vocales. 
Se recomienda crear un segundo string con toda la frase en minúsculas para que sea más fácil disponer 
la condición que verifica que es una vocal. 
"""
frase = input("Introduce una frase: ")
frase = frase.lower()
vocales = 'aeiou'
contador = 0

for caracter in frase:
    if caracter in vocales:
        contador += 1

print("La cantidad de vocales en la frase es: ", contador)