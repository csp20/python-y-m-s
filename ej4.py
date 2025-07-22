#Comúnmente se dice que un año humano equivale a 7 años de perro. Sin embargo,
#esta simple conversión no reconoce que los perros alcanzan la edad adulta en
#aproximadamente dos años. Escriba un programa que implemente la conversión de
#años humanos a años perro descrita en el párrafo anterior. Asegúrese de que su
#programa funcione correctamente para conversiones de menos de dos años
#humanos y para conversiones menores o más años humanos. Su programa debe
#mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.
def convertir_a_anios_perro(anios_humanos):
    if anios_humanos < 0:
        return "Error: Ingresa un número positivo."
    elif anios_humanos < 2:
        anios_perro = anios_humanos * 7
    else:
        anios_perro = 2 * 7 + (anios_humanos - 2) * 5

    return f"{anios_humanos} años humanos equivalen a aproximadamente {anios_perro} años de perro."

# Solicitar al usuario ingresar la edad en años humanos
anios_humanos = float(input("Ingresa la edad en años humanos: "))

# Mostrar el resultado
print(convertir_a_anios_perro(anios_humanos))