import random

def leer_csv(ruta_deportes="csvs_preguntas/preguntas_deportes.csv",ruta_ciencia="csvs_preguntas/preguntas_ciencia.csv",
            ruta_historia="csvs_preguntas/preguntas_historia.csv",ruta_entretenimiento="csvs_preguntas/preguntas_entretenimiento.csv"):
    
    """Lee los archivos csv de preguntas y guarda cada linea en diccionarios dentro de una lista
    """
    
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



def buscar_pregunta_azar(preguntas: dict):
    """Busca una pregunta al azar dentro de la lista de diccionarios de preguntas

    Args:
        preguntas (dict[list[dict]])

    Returns:
        pregunta_elegida: Dict
    """
    lista_categorias = list(preguntas.keys())
    categoria_elegida= random.choice(lista_categorias)
    pregunta_elegida = random.choice(preguntas[categoria_elegida])
    return pregunta_elegida, categoria_elegida



def buscar_pregunta_azar_en_categoria(preguntas:dict, categoria_elegida:str):
    """Busca una pregunta al azar dentro de una categoria definida, con la clave del diccionario pasada por parámetro

    Args:
        preguntas (dict[list[dict])
        categoria_elegida (str): Clave para buscar dentro del valor de la categoria

    Returns:
        _type_: _description_
    """
    pregunta_elegida = random.choice(preguntas[categoria_elegida])
    return pregunta_elegida



def mostrar_pregunta(pregunta:dict,categoria:str):
    """Muestra por consola la pregunta con sus opciones

    Args:
        pregunta (dict): Pregunta y opciones 
        categoria (str): Categoria de la pregunta
    """
    print (" ")
    print(f"{' '*20}{categoria.upper()}{' '*20}")
    print (pregunta["pregunta"])
    for opcion in range (len(pregunta["opciones"])):
        print (f"{opcion+1}: {pregunta["opciones"][opcion]}")
    print (" ")



def pedir_respuesta()-> int:
    """Pide por teclado una opcion entre 1,2,3,4 y 5 y la valida.

    Returns:
        int: [1,2,3,4,5]
    """
    opciones_validas = ["1","2","3","4"]
    respuesta_usuario =(input("Ingrese la respuesta: 1, 2, 3 o 4:  "))
    while respuesta_usuario not in opciones_validas:
        respuesta_usuario =(input("Ingrese la respuesta: 1, 2, 3 o 4: "))
    respuesta_usuario = int (respuesta_usuario)
    return respuesta_usuario



def validar_respuesta(pregunta:dict, respuesta_usuario:int)-> bool:
    """Valida si la opcion elegida por el usuario corresponde a la respuesta correcta, de ser asi retorna True, sino, False.

    Args:
        pregunta (dict): Diccionario con pregunta, opciones y respuesta correcta.
        respuesta_usuario (int): [1,2,3,4,5]

    Returns:
        bool
    """
    if pregunta["opciones"][respuesta_usuario-1]== pregunta["respuesta_correcta"]:
        return True
    else : 
        return False



def pedir_categoria_coronacion(preguntas:dict, lista_usuarios:list, indice_jugador:int)->tuple[str, set[str]]:
    """Muestra al usuario las coronas de las categorías que le falta obtener y pide que elija una, retorna la categoria y las coronas faltantes

    Args:
        preguntas (dict): Diccionario con categorías como claves y listas de diccionarios con preguntas como valores.
        lista_usuarios (list[dict]): Lista de diccionarios que almacenan los datos de cada jugador
        indice_jugador (int): Indice del usuario dentro de la lista_usuarios

    Returns:
        tuple[str, set[str]]: Categoria elegida y las coronas restantes para ganar el juego
    """
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