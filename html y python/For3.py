""" ej3
Uso de string(array de caracteres). Escribir un programa que, dada una frase introducida por el usuario,
 muestre la cantidad total de vocales (tanto mayúsculas como minúsculas) que contiene
 """
# Pedir al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Contar el número total de vocales
num_vocales = 0
for caracter in frase:
    if caracter in vocales:
        num_vocales += 1

# Imprimir el resultado
print("La frase contiene", num_vocales, "vocales.")