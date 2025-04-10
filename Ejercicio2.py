"""
Menú Interactivo en Python
Como parte del entrenamiento en desarrollo de interfaces básicas por consola, se te ha
encomendado la creación de un menú interactivo utilizando el lenguaje de programación Python.
Este programa simulará un sistema de navegación sencillo que responde a diferentes opciones
seleccionadas por el usuario.
El objetivo de este ejercicio es practicar estructuras de control como ciclos while, condicionales
if/elif/else, y entradas por teclado (input()), además de implementar una lógica que mantenga el
programa activo hasta que el usuario decida salir.

Requerimientos del Programa
Desarrolla un programa que cumpla con los siguientes criterios:
1. Mostrar un Menú Interactivo:
o Al iniciar, el programa debe mostrar un menú en pantalla con al menos tres
opciones:
1. Mostrar un mensaje.
2. Mostrar una lista de nombres.
3. Salir del programa.
2. Captura y Procesamiento de la Opción:
o El usuario debe poder seleccionar una opción ingresando un número o palabra clave.
o El programa debe responder a la opción elegida ejecutando la acción
correspondiente:
 Si elige la opción "Mostrar mensaje", debe imprimirse en consola un
mensaje amigable o motivacional.
 Si elige "Mostrar nombres", se debe mostrar una lista predefinida de
nombres.
 Si elige "Salir", el programa debe finalizar mostrando un mensaje de
despedida.
3. Estructura de Control:
o Usa un bucle while para mantener el programa en ejecución mientras el usuario no
elija la opción de salir.
o Asegúrate de validar la entrada del usuario y mostrar un mensaje de error si la
opción no es válida.
"""
def cls(): # Limpia la consola
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
def pausaT(segundos):
    import time
    time.sleep(segundos)

 # Limpia la consola al finalizar el programa
# Fin del programa
# Definición del menú interactivo

#Interacción con el Usuario:
print("****************************************")
print("*                                      *")
print("*      ¡Bienvenidos al Juego!          *")
print("*                                      *")
print("****************************************")


def mostrar_menu():
    print("1. Mostrar mensaje")
    print("2. Mostrar nombres")
    print("3. Salir")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("(***Tu potencial es infinito, atrévete a explorarlo.***")
        pausaT(3)
        cls()
    elif opcion == "2":
        nombres = ["Alice", "Bob", "Charlie"]
        print("Lista de nombres:", nombres)
        pausaT(3)
        cls()
    elif opcion == "3":
        print("Saliendo del programa; ¡gracias por participar :)")
        pausaT(3)
        cls()
        break
        
    else:
        print("Opción no válida:( Por favor, intenta nuevamente.")
        pausaT(3)
        cls()


