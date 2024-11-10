def menu_juego()->str:
    """
    Imprime el menú en pantalla

    Returns:
    input: para seleccionar la opción que querramos
    """
    print ("")
    print(f"{'Menu de opciones':^50}")
    print("1 - Jugar")
    print("2 - Instrucciones")
    print("3 - Rankings")
    print("4 - Eliminar datos de jugador")
    print("5 - Salir")
    opciones_validas = ["1","2","3","4","5"]
    opcion_menu_elegida = input ("Ingrese una opcion: ")

    while opcion_menu_elegida not in opciones_validas:
        opcion_menu_elegida = input ("Incorrecto. Ingrese una opcion:")
    return opcion_menu_elegida



def mostrar_instrucciones():
    """Imprime las instrucciones del juego
    """
    print("                 ¡Bienvenido a Preguntados!")
    print("El juego consiste en contestar preguntas sobre 4 categorías al azar:")
    print("Historia, deportes, entretenimiento y ciencia")
    print("El objetivo del juego es conseguir la corona de cada una de las 4 categorías")
    print("Para obtener una corona, deberás contestar 3 preguntas correctamente")
    print("y se te dará la chance para conseguir una corona a elección")
    print("Si contestás 3 preguntas mal, se termina el juego.")
    print (" ")



def mostrar_rankings(lista_jugadores:list):
    """Ordena los diccionarios asociados a cada jugador por orden decreciente de victorias y lo muestra en consola
    Args:
        lista_usuarios (list[dict])
    """
    cantidad_jugadores= len(lista_jugadores)
    for i in range(cantidad_jugadores):
        for j in range(0, cantidad_jugadores-i-1):
            if lista_jugadores[j]["victorias"]>lista_jugadores[j+1]["victorias"]:
                lista_jugadores[j], lista_jugadores[j+1] = lista_jugadores[j+1], lista_jugadores[j] 

    for i in range(cantidad_jugadores-1, -1, -1):
        print(f"{lista_jugadores[i]["nombre"].capitalize()} - {lista_jugadores[i]["victorias"]} victorias.")


