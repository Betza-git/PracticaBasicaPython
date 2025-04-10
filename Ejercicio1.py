""" Programa BETA para Nike
La reconocida empresa multinacional Nike, líder en la industria del calzado y ropa deportiva, ha
encargado el desarrollo de un programa BETA como parte de una iniciativa de mejora en la gestión
interna de datos dinámicos. Este programa, desarrollado en Python, servirá como una herramienta
de prueba para validar operaciones básicas sobre estructuras de datos tipo diccionario,
fundamentales en múltiples procesos de la compañía, como el manejo de inventarios
Como parte del equipo de desarrollo, tu tarea consiste en construir un programa que permita al
usuario interactuar con un diccionario predefinido, brindando funcionalidades para modificar y
eliminar elementos de forma controlada y amigable.

Requerimientos del Programa
Tu programa debe cumplir con las siguientes funcionalidades:
1. Interacción con el Usuario:
o Solicita al usuario que ingrese la clave (key) del diccionario cuyo valor desea
modificar.
o Si la clave existe, permite al usuario ingresar un nuevo valor y actualiza dicha
entrada en el diccionario.
"""



# Definición del diccionario inicial
inventario = {
    "Tennis": 50,
    "Camisetas": 100,
    "Color": "Rojo",
    "Pantalones": 75,
    "Gorras": 30
}

#Interacción con el Usuario:
print("****************************************")
print("*                                      *")
print("*     ¡Bienvenidos a BETA Nike!        *")
print("*                                      *")
print("****************************************")

def menu():
    print("1. Modificar valor de una clave existente")
    print("2. Eliminar una clave")
    print("3. Salir") 
    option = input("Ingresa una opción: ")    
    return option

def modificar_clave(inventario): 
    clave = input("Ingresa la clave que deseas modificar: ")
    if clave in inventario:
        nuevo_valor = input(f"Ingresa el nuevo valor para '{clave}': ")
        inventario[clave] = nuevo_valor
        print(f"El valor de '{clave}' ha sido actualizado a '{nuevo_valor}'.")
    else:
        print(f"La clave '{clave}' no existe en el inventario :(") 

#eliminar una clave usando del, *funciona mejor en diccionarios que .pop
def eliminar_clave(inventario):
    clave = input("Ingrese la clave que desea eliminar: ")
    if clave in inventario:
        del inventario[clave]  # del para eliminar la clave
        print(f"La clave '{clave}' ha sido eliminada.")
    else:
        print(f"La clave '{clave}' no existe en el inventario.")
    return inventario 

# Ciclo principal del programa
while True:
    print("\nInventario actual:", inventario)
    opcion = menu()
    
    if opcion == "1":
        modificar_clave(inventario)
    elif opcion == "2":
        inventario = eliminar_clave(inventario)
    elif opcion == "3":
        print("Saliendo del programa; Gracias por usar BETA Nike:)")
        break
    else:
        print("Opción no válida:( Por favor, intenta nuevamente.")

        
def cls(): # Limpia la consola
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
cls() # Limpia la consola al finalizar el programa
# Fin del programa
  
