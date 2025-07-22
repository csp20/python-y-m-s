"""Pedir por pantalla una nota (entre 1 y 7). Luego se debe comprobar que el número
efectivamente esté en ese rango, si no lo está imprima un mensaje de error. Si lo
está, imprima suspenso si la nota es inferior a 5, regular si está entre 5 y 6(menor),
y por último, bien si está entre 6 y 7."""
# Solicitar al usuario una nota
nota = float(input("Ingrese una nota (entre 1 y 7): "))

# Verificar si la nota está en el rango
if 1 <= nota <= 7:
    # Evaluar la nota y mostrar el resultado
    if nota < 5:
        print("Suspenso")
    elif 5 <= nota < 6:
        print("Regular")
    else:
        print("Bien")
else:
    print("Error: La nota debe estar entre 1 y 7.")