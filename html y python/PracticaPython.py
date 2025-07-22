# Tienda electrodomesticos willy
# Listas para almacenar la información
productos = ['Lavadora', 'Nevera', 'Televisor', 'Microondas', 'Tostadora']
precios = [300, 600, 400, 50, 20]
carrito = []
comprados = []

# Función para mostrar los productos
def mostrar_productos():
    print("\nProductos disponibles:")
    for i in range(len(productos)):
        print(f"{i+1}. {productos[i]} - Precio: {precios[i]}€")


#print(str(i+1) + ". " + productos[i] + " - Precio: " + str(precios[i]) + "€")


# Función para añadir al carrito
def añadir_al_carrito():
    mostrar_productos()
    eleccion = int(input("\nElige el número del producto que quieres añadir al carrito: ")) - 1
    if 0 <= eleccion < len(productos):
        carrito.append(productos[eleccion])
        print(f"\nHas añadido un/a {productos[eleccion]} a tu carrito.")
    else:
        print("\nNumero NO valido")

# Función para comprar productos
def comprar_productos():
    print("\nProductos en tu carrito:")
    for i in range(len(carrito)):
        print(f"{i+1}. {carrito[i]}")
    eleccion = int(input("\nElige el número del producto que quieres comprar: ")) - 1
    if 0 <= eleccion < len(carrito):
        comprados.append(carrito[eleccion])
        print(f"\nHas comprado un/a {carrito[eleccion]}.")
        del carrito[eleccion]
    else:
        print("\nElección inválida. Vuelve a intentarlo.")

# Función para devolver productos
def devolver_producto():
    print("\nProductos comprados:")
    for i in range(len(comprados)):
        print(f"{i+1}. {comprados[i]}")
    eleccion = int(input("\nElige el número del producto que quieres devolver: ")) - 1
    if 0 <= eleccion < len(comprados):
        print(f"\nHas devuelto un/a {comprados[eleccion]}.")
        del comprados[eleccion]
    else:
        print("\nElección inválida. Vuelve a intentarlo.")

# Bucle principal del programa
while True:
    print("\nBienvenido a la tienda de electrodomésticos. Elige una opción:")
    print("1. Mostrar productos")
    print("2. Añadir al carrito")
    print("3. Comprar productos")
    print("4. Devolver producto")
    print("5. Salir")
    opcion = int(input("\nTu opción: "))

    if opcion == 1:
        mostrar_productos()
    elif opcion == 2:
        añadir_al_carrito()
    elif opcion == 3:
        comprar_productos()
    elif opcion == 4:
        devolver_producto()
    elif opcion == 5:
        print("\n¡Gracias por visitar nuestra tienda!")
        break
    else:
        print("\nOpción inválida. Por favor, elige una opción del menú.")
