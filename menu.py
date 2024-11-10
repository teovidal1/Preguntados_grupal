from logica_juego import *
from funciones_preguntas import *
from funciones_print import *
from funciones_usuarios import *
#
opcion_elegida = ""
#

while opcion_elegida != "5" :

    match menu_juego():

        case "1":
            jugar(lista_usuarios)

        case "2":
            mostrar_instrucciones()
            
        case "3": 
            if len(lista_usuarios) > 0:
                mostrar_rankings(cargar_usuarios())
            else: 
                print ("No hay datos de jugadores todavía.")
                print ("")

        case "4":
            if len(lista_usuarios) > 0 :
                borrar_jugadores(lista_usuarios)
            else: 
                print ("No hay datos de jugadores todavía.")
                print ("")

        case "5":
            print ("¡Gracias por jugar!")
#
