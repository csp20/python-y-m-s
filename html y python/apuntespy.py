# Declaración de variables
nombre = "John"
edad = 30
activo = True

print(f"Nombre: {nombre}, Edad: {edad}, Activo: {activo}")

# Uso de if-else
if edad > 18:
    print("Adulto")
else:
    print("Menor de edad")

# Bucle for
for i in range(5):
    print(f"Iteración {i}")

# Bucle while
i = 0
while i < 5:
    print(f"Iteración {i}")
    i += 1

# Operadores aritméticos
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División Entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# Operadores lógicos
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)


# Función simple
def saludo(nombre):
    return f"Hola, {nombre}"

print(saludo("John"))


# Función con parámetros y valor de retorno
def suma(a, b):
    return a + b

resultado = suma(10, 5)
print(f"La suma es: {resultado}")


# Función lambda para sumar dos números
suma = lambda a, b: a + b

# Usando la función lambda
resultado = suma(5, 3)
print(f"La suma es: {resultado}")

# mi_modulo.py
def saludar(nombre):
    return f"Hola, {nombre}"

def despedirse(nombre):
    return f"Adiós, {nombre}"
# main.py
import  mi_modulo

nombre = "John"
print(mi_modulo.saludar(nombre))
print(mi_modulo.despedirse(nombre))

#clase persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear un objeto de la clase Persona
persona1 = Persona("John", 30)
print(persona1.saludar())


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentar(self):
        return f"Soy {self.nombre}, estudiante de {self.carrera}."

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Anna", 22, "Ingeniería")
print(estudiante1.saludar())
print(estudiante1.presentar())


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def saludar(self):
        return f"Hola, mi nombre es {self.__nombre} y tengo {self.__edad} años."

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

# Crear un objeto de la clase Persona
persona1 = Persona("John", 30)
print(persona1.saludar())

# Intentar acceder a un atributo privado directamente (no recomendado)
# print(persona1.__nombre)  # Esto generará un error

# Usar métodos de acceso para obtener y establecer valores
print(persona1.obtener_nombre())
persona1.establecer_nombre("Michael")
print(persona1.saludar())

#try-catch
try:
    resultado = 10 / 0  # Esto generará una excepción de división por cero
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Esto siempre se ejecuta, independientemente de si hubo una excepción o no.")

#listas
lista = [1, 2, 3, "cuatro", True]
lista.append(5)
print(lista)
print(lista[2])  # Acceder al tercer elemento

#tuplas
tupla = (1, 2, 3, "cuatro", True)
print(tupla)
print(tupla[2])  # Acceder al tercer elemento

#diccionarios
diccionario = {"nombre": "John", "edad": 30, "activo": True}
print(diccionario)
print(diccionario["nombre"])  # Acceder al valor asociado a la clave "nombre"


# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo\n")
    archivo.write("Otra línea de texto\n")

# Leer desde un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Usar with para manejar archivos
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
# No es necesario cerrar el archivo explícitamente; el context manager lo hace automáticamente

import numpy as np

# Crear un array de Numpy
array = np.array([1, 2, 3, 4, 5])

# Operaciones básicas
suma = np.sum(array)
media = np.mean(array)
maximo = np.max(array)
minimo = np.min(array)

print(f"Suma: {suma}, Media: {media}, Máximo: {maximo}, Mínimo: {minimo}")


import pandas as pd

# Crear un DataFrame de Pandas
data = {
    'Nombre': ['John', 'Anna', 'Peter', 'Linda'],
    'Edad': [28, 24, 35, 32],
    'Ciudad': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

# Operaciones básicas
print(df.head())  # Muestra las primeras filas
print(df.describe())  # Estadísticas descriptivas

# Filtrado de datos
df_filtrado = df[df['Edad'] > 30]
print(df_filtrado)

 
