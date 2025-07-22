"""La duración de un mes varía de 28 a 31 días. En este ejercicio crearás
un programa que lee el nombre de un mes del usuario como una cadena.
El programa debe mostrar el mes y el número de días en ese mes. Mostrar "28 o 29
días" para febrero y los años bisiestos."""
def obtener_dias_en_mes(mes):
    meses_30_dias = ["abril", "junio", "septiembre", "noviembre"]
    meses_31_dias = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]

    if mes.lower() in meses_30_dias:
        return 30
    elif mes.lower() in meses_31_dias:
        return 31
    elif mes.lower() == "febrero":
        return "28 o 29 días (bisiesto)"

# Solicitar al usuario el nombre del mes
nombre_mes = input("Ingrese el nombre de un mes: ")

# Obtener y mostrar el resultado
dias_en_mes = obtener_dias_en_mes(nombre_mes)
if dias_en_mes:
    print(f"{nombre_mes.capitalize()} tiene {dias_en_mes} días.")
else:
    print("Nombre de mes no válido.")