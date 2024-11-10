import json


def crear_usuario(nombre:str)->dict:
    """Recibe un nombre por parámetro y 
    retorna un usuario con ese nombre y los datos predeterminados
    Args:
        nombre (str): nombre del usuario

    Returns:
        dict: Diccionario con nombre, vidas, coronas, victorias, racha y partidas_jugadas
    """
    return {
        "nombre": nombre,
        "vidas": 3,
        "coronas": set(), 
        "victorias": 0,
        "racha": 0,
        "partidas_jugadas": 0
    }



def validar_nombre(nombre_a_buscar:str, lista_usuarios:list[dict])->bool:
    """Busca un nombre(str) en todas las claves "nombre" de los diccionarios de una lista

    Args:
        nombre_a_buscar (str): 
        lista_usuarios (list): list[dict]

    Returns:
        bool: _description_
    """
    for usuario in lista_usuarios:
        if usuario['nombre'] == nombre_a_buscar:
            return True
    return False



def buscar_indice_usuario_en_lista(lista_usuarios:list[dict], nombre_usuario:str)->int|None:
    """Busca un nombre(str) en la clave "nombre" de todos los diccionarios de una lista y retorna la posición del diccionario si lo encuentra.

    Args:
        lista_usuarios (list): list[dict]
        nombre_usuario (str)

    Returns:
        int: Índice del diccionario en el que encuentra el nombre
    """
    for i in range (len(lista_usuarios)):
        if lista_usuarios[i]["nombre"]==nombre_usuario:
            indice_usuario_actual= i
        return indice_usuario_actual
    return None



def borrar_jugadores(lista_jugadores:list):
    """Busca un nombre en las claves "nombre" de cada duccionario dentro de una lista y, si lo encuentra, borra ese diccionario.

    Args:
        lista_jugadores (list[dict])
    """
    cantidad_jugadores = len(lista_jugadores)
    for i in range(cantidad_jugadores):
        print (f"{(lista_jugadores[i]["nombre"]).capitalize()}, {lista_jugadores[i]["victorias"]} victorias en {lista_jugadores[i]["partidas_jugadas"]} partidas jugadas")
    jugador_a_eliminar = input("Ingrese qué jugador desea eliminar")
    for i in range (len(lista_jugadores)):
        if lista_jugadores[i]["nombre"]==jugador_a_eliminar:
            lista_jugadores.pop(lista_jugadores[i])



def cargar_usuarios(ruta="datos_usuarios.json")->list[dict]:
    """
    Carga una lista de usuarios desde un archivo JSON.

    Args:
        ruta (str, optional): La ruta del archivo JSON. Predefinida en "datos_usuarios.json".

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un usuario y contiene sus datos. 
    """
    with open (ruta) as contenido:
        lista_usuarios = json.load(contenido)
        for i in range (len(lista_usuarios)):
            lista_usuarios[i]["coronas"]=set((lista_usuarios)[i]["coronas"])
    return lista_usuarios



def guardar_usuarios (lista_usuarios:list, ruta="datos_usuarios.json", ):
    """Guarda los datos de una lista de diccionarios en un json, después de transformar los valores de todas las claves "coronas" en una lista.

    Args:
        lista_usuarios (list)
        ruta (str, optional): _description_. Defaults to "datos_usuarios.json".
    """
    for i in range (len(lista_usuarios)):
        lista_usuarios[i]["coronas"]= list(lista_usuarios[i]["coronas"])

    with open (ruta, "w") as contenido:
        json.dump(lista_usuarios,contenido, indent=4)
