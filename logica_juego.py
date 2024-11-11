from funciones_usuarios import *
from funciones_preguntas import *
from funciones_print import *

lista_usuarios=cargar_usuarios()

def jugar(lista_usuarios:list):
    
    preguntas=leer_csv()

    nombre_usuario = input ("Ingrese su nombre de usuario: ").capitalize()
    if validar_nombre(nombre_usuario, lista_usuarios)==False:
        lista_usuarios.append(crear_usuario(nombre_usuario))

    indice_jugador = buscar_indice_usuario_en_lista(lista_usuarios, nombre_usuario)

    while len(set(lista_usuarios[indice_jugador]["coronas"]))<4 and lista_usuarios[indice_jugador]["vidas"]>0:
        
        if lista_usuarios[indice_jugador]["racha"]<3:
            pregunta, categoria = buscar_pregunta_azar(preguntas)
            mostrar_pregunta(pregunta, categoria)

            if validar_respuesta(pregunta, pedir_respuesta()):

                lista_usuarios[indice_jugador]["racha"]+=1
                print ("")
                print ("¡CORRECTO!")
                print (f"¡¡Ahora tu racha es de {lista_usuarios[indice_jugador]["racha"]}!!")
                print ("")

            else:

                lista_usuarios[indice_jugador]["racha"] =0
                lista_usuarios[indice_jugador]["vidas"]-=1
                print ("")
                print (f"¡INCORRECTO! La respuesta correcta era {pregunta["respuesta_correcta"]}")
                print (f"¡¡Ahora te quedan {lista_usuarios[indice_jugador]["vidas"]} vidas!!")
                print ("")

        if lista_usuarios[indice_jugador]["racha"]==3:
            print ("")
            print ("¡¡Llegaste a una pregunta de coronacion!!")
            print ("")

            categoria_elegida, coronas_faltantes = pedir_categoria_coronacion(preguntas, lista_usuarios, indice_jugador)
            pregunta = buscar_pregunta_azar_en_categoria(preguntas, categoria_elegida)
            mostrar_pregunta(pregunta,categoria_elegida)

            if validar_respuesta(pregunta, pedir_respuesta()):
                lista_usuarios[indice_jugador]["racha"] =0
                (lista_usuarios[indice_jugador]["coronas"]).append(categoria_elegida)

                coronas_faltantes.remove(categoria_elegida)
                coronas_faltantes_string = ", ".join(coronas_faltantes)

                print ("")
                print ("¡¡¡CORRECTO!!!")
                print (f"¡¡¡GANASTE LA CORONA DE {categoria_elegida}!!!")
                if len(coronas_faltantes_string)!=0:
                    print (f"AHORA TE FALTAN LAS CORONAS DE: {(coronas_faltantes_string)}")
                print ("")

            else: 
                lista_usuarios[indice_jugador]["racha"] = 0
                lista_usuarios[indice_jugador]["vidas"] -= 1

                print ("\n ¡¡¡INCORRECTO!!!")
                print (f"¡¡¡NO GANASTE LA CORONA DE {categoria_elegida}!!!")
                print (f"La respuesta correcta era {pregunta["respuesta_correcta"]}")

        guardar_usuarios(lista_usuarios)

    if len(set(lista_usuarios[indice_jugador]["coronas"]))==4:
        lista_usuarios[indice_jugador]["victorias"] += 1 
        print (f"¡¡VICTORIA!!, AHORA TENES {lista_usuarios[indice_jugador]["victorias"]} victoria/s")
        
    if lista_usuarios[indice_jugador]["vidas"]==0:
        print (f"Perdiste!")
        

    lista_usuarios[indice_jugador]["vidas"] = 3
    lista_usuarios[indice_jugador]["partidas_jugadas"] +=1
    lista_usuarios[indice_jugador]["coronas"]=()

    guardar_usuarios(lista_usuarios)

