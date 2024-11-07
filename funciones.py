import random
import json 

def cargar_usuarios(ruta="datos_usuarios.json")->list:
    with open (ruta) as contenido:
        lista_usuarios = json.load(contenido)
        for i in range (len(lista_usuarios)):
            lista_usuarios[i]["coronas"]=set((lista_usuarios)[i]["coronas"])
    return lista_usuarios

def guardar_usuarios (lista_usuarios:list, ruta="datos_usuarios.json", ):
    for i in range (len(lista_usuarios)):
        lista_usuarios[i]["coronas"]= list(lista_usuarios[i]["coronas"])

    with open (ruta, "w") as contenido:
        json.dump(lista_usuarios,contenido)
        


def leer_csv(ruta_deportes="preguntas_deportes.csv",ruta_ciencia="preguntas_ciencia.csv",
            ruta_historia="preguntas_historia.csv",ruta_entretenimiento="preguntas_entretenimiento.csv"):
    
    preguntas = {"Deportes":[],
                "Historia":[],
                "Ciencia":[],
                "Entretenimiento":[]               
                }

    def leer_archivo_categoria(categoria,ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:]:
                linea = linea.strip().split(",")
                dict_pregunta= {
                            "pregunta":linea[0],
                            "opciones":linea[1:-1],
                            "respuesta_correcta":linea[-1]
                            }
                preguntas[categoria].append(dict_pregunta)

    
    leer_archivo_categoria("Deportes",ruta_deportes)
    leer_archivo_categoria("Entretenimiento",ruta_entretenimiento)
    leer_archivo_categoria("Historia",ruta_historia)
    leer_archivo_categoria("Ciencia",ruta_ciencia)
    return preguntas



def menu_juego()->str:
    """
    Imprime el menú en pantalla

    Returns:
    input: para seleccionar la opción que querramos
    """

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



def crear_usuario(nombre:str):
    return {
        "nombre": nombre,
        "vidas": 3,
        "coronas": set(), 
        "victorias": 0,
        "racha": 0,
        "partidas_jugadas": 0
    }



def mostrar_instrucciones():
    print("                 ¡Bienvenido a Preguntados!")
    print("El juego consiste en contestar preguntas sobre 4 categorías al azar:")
    print("Historia, deportes, entretenimiento y ciencia")
    print("El objetivo del juego es conseguir la corona de cada una de las 4 categorías")
    print("Para obtener una corona, deberás contestar 3 preguntas correctamente")
    print("y se te dará la chance para conseguir una corona a elección")
    print("Si contestás 3 preguntas mal, se termina el juego.")
    print (" ")


def mostrar_rankings(lista_jugadores:list):
    cantidad_jugadores= len(lista_jugadores)
    for i in range(cantidad_jugadores):
        for j in range(0, cantidad_jugadores-i-1):
            if lista_jugadores[j]["victorias"]>lista_jugadores[j+1]["victorias"]:
                lista_jugadores[j], lista_jugadores[j+1] = lista_jugadores[j+1], lista_jugadores[j] 

    for i in range(cantidad_jugadores-1, -1, -1):
        print(f"{lista_jugadores[i]["nombre"].capitalize()} - {lista_jugadores[i]["victorias"]} victorias.")



def validar_nombre(nombre_a_buscar:str, lista_usuarios:list)->bool:

    for usuario in lista_usuarios:
        if usuario['nombre'] == nombre_a_buscar:
            return True
    return False



def buscar_indice_usuario_en_lista(lista_usuarios:list, nombre_usuario:str)->int:

    for i in range (len(lista_usuarios)):
        if lista_usuarios[i]["nombre"]==nombre_usuario:
            indice_usuario_actual= i
    return indice_usuario_actual



def buscar_pregunta_azar(preguntas: dict):
    lista_categorias = list(preguntas.keys())
    categoria_elegida= random.choice(lista_categorias)
    pregunta_elegida = random.choice(preguntas[categoria_elegida])
    return pregunta_elegida, categoria_elegida



def buscar_pregunta_azar_en_categoria(preguntas:dict, categoria_elegida:str):
    pregunta_elegida = random.choice(preguntas[categoria_elegida])
    return pregunta_elegida



def mostrar_pregunta(pregunta:dict,categoria:str):
    print (" ")
    print(f"{' '*20}{categoria.upper()}{' '*20}")
    print (pregunta["pregunta"])
    for opcion in range (len(pregunta["opciones"])):
        print (f"{opcion+1}: {pregunta["opciones"][opcion]}")
    print (" ")



def pedir_respuesta()-> int:
    opciones_validas = ["1","2","3","4"]
    respuesta_usuario =(input("Ingrese la respuesta: 1, 2, 3 o 4:  "))
    while respuesta_usuario not in opciones_validas:
        respuesta_usuario =(input("Ingrese la respuesta: 1, 2, 3 o 4: "))
    respuesta_usuario = int (respuesta_usuario)
    return respuesta_usuario



def validar_respuesta(pregunta:dict, respuesta_usuario:int)-> bool:
    if pregunta["opciones"][respuesta_usuario-1]== pregunta["respuesta_correcta"]:
        return True
    else : 
        return False


def pedir_categoria_coronacion(preguntas:dict, lista_usuarios:list, indice_jugador:int)->tuple[str, set[str]]:

    categorias = set(preguntas.keys())
    coronas_usuario = set(lista_usuarios[indice_jugador]["coronas"])
    coronas_faltantes = categorias-coronas_usuario
    coronas_faltantes_string = ", ".join(coronas_faltantes)
    if len(coronas_faltantes)>1:
        categoria_corona_elegida = input(f"Ingrese la categoría que desea coronar: {coronas_faltantes_string}: ").capitalize()
    else:
        categoria_corona_elegida = input(f"Ingrese {coronas_faltantes_string}, es la ultima corona que le falta: ").capitalize()
    while categoria_corona_elegida not in coronas_faltantes:
        categoria_corona_elegida = input("ERROR. Ingrese la categoría que desea coronar: ").capitalize()

    return categoria_corona_elegida, coronas_faltantes


def borrar_jugadores(lista_jugadores:list):
    cantidad_jugadores = len(lista_jugadores)
    for i in range(cantidad_jugadores):
        print (f"{(lista_jugadores[i]["nombre"]).capitalize()}, {lista_jugadores[i]["victorias"]} victorias en {lista_jugadores[i]["partidas_jugadas"]}")