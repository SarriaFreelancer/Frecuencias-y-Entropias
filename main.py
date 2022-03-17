#Autores: JUAN DAVID CUERO SARRIA
#         CARLOS IVAN GUEVARA MOSQUERA
#         DIEGO ANDREY MURRILLO MACHUCA
#         MARVIN JAVIER MORENO TANGARIFE
#---------------------------------MATEMATICAS DISCRETAS II 2022---TSI-UNIVALLE-SEDE-PACÍFICO-----------------------------------

#--------------PROGRAMA PARA CALCULAR FRECUENCIAS Y ENTROPIAS DE PALABRAS Y LETRAS EN UN DETERMINADO TEXTO---------------------
from collections import Counter
from types import GenericAlias
import math

# =====================================FUNCION PRINCIPAL=============================================

def principal():
    opcion = 0
    while opcion != 1 and  opcion != 2 and  opcion != 3 :
        opcion = int(input(f'''
                       ***********************************************************************
                       *******SISTEMA PARA CALCULAR FRECUENCIAS Y ENTROPIAS EN OBRAS**********
                       ***********************************************************************
                       **                                                                   **
                       **          Elige una de las obras que tenemos disponibles           **
                       **                                                                   **
                       **                                                                   **
                       ** 1. Don Quijote de La Mancha                                       **
                       ** 2. Cien Años de Soledad                                           **
                       ** 3. Cronicas de una Muerte Anunciada                               **
                       **                                                                   **
                       ** Numero de Obra: '''))

        if opcion == 1:
            nombre = 'Don Quijote de la Mancha'
            obra = donQuijote
        elif opcion == 2:
            nombre = 'Cien Años de Soledad'
            obra = garciaCien
        elif opcion == 3:
            nombre = 'Cronicas de Una Muerte Anunciada'
            obra = muerteAnunciada
        else:
            print("\n                               opcion errada, dijite un numero de obra existente\n")



    # Menu para elegir la obra completa o parcial
    opc = 0

    while opc <=2:
        opc = int(input(f'''
                         \n
                           ***********************************************************************
                           *********************************Elegir********************************
                           ***********************************************************************
                           \n
                           ** 1. Obra Total                                                     **
                           ** 2. Obra Parcial                                                   **
                           ** 3. Volver al menu principal y elegir otra obra                    **
                           ** 
                           ** ingrese opcion: '''))
        if opc == 1:
            op = int(input(f'''
                              \n
                                ***********************************************************************
                                **********Menu Para Frecuencias y Entropias en Obra Total**************
                                ***********************************************************************
                                \n
                                ** lo que desee realizar en la obra {nombre}\n
                                ** 1. Visualizar texto obra                                          **
                                ** 2. Frecuencia de Palabras y entropia                              **
                                ** 3. Frecuencia de una palabra                                      **
                                ** 4. Palabras Válidas                                               **
                                ** 5. Frecuencia de letras y entropia                                **
                                ** 6. Frecuencia de una letra                                        **
                                ** 7. Letras Válidas                                                 **\n
                                ****  dijite  la opcion a realizar: '''))
            # ===================================CONFIRMACION DE OPCIONES========================================
            # ===A ESTA LINEA DENTRO DE LA FUNCION PRINCIPAL
            if op == 1:
                print(f'''  \n*************************************************************************
                              **  Visualizando texto original de la obra {nombre}       **
                              *************************************************************************\n ''')
                mostrar(obra)
            elif op == 2:
                print(f'''\n
                         ***************************************************************************
                         **    Tabla de Frecuencia y Entropia de la obra {nombre} **
                         ***************************************************************************\n''')
                print(f'Termino---Ocurrencia---Frecuencia %\n')
                frecuenciaPalabras(obra)
                print(f'''\n
                          ***************************************************************************
                          **            Entropia de la obra {nombre}        
                          ***************************************************************************
                          \n''')
                entropiaPalabras(obra)
            elif op == 3:
                print(f'''\n
                          ********************************************************************************
                          ***  Tabla de frecuencia para una palabra de la obra {nombre}
                          ********************************************************************************\n''')
                frecuenciaTermino(obra)
            elif op == 4:
                print('''\n
                                         **************************************************************************************
                                         ***                                Palabras Validas                                ***
                                         **************************************************************************************\n''')
                contarPalabras(obra)
            elif op == 5:
                print(f'''\n
                                     ***************************************************************************************
                                     **Tabla de Frecuencia y Entropia de la obra {nombre} en letras**
                                     ***************************************************************************************\n''')
                print(f'\nTermino-----Ocurrencia----Frecuencia %\n')
                frecuenciaLetras(obra)
                print(f'''\n
                                      ***************************************************************************
                                      **    Entropia de letras en la obra {nombre}        
                                      ***************************************************************************
                                      \n''')
                entropiaLetras(obra)
            elif op == 6:
                print(f'''\n
                                      ***************************************************************************
                                      **    Frecuencia de una letra en la obra {nombre}        
                                      ***************************************************************************\n''')
                frecuenciaTerminoLetra(obra)
            elif op == 7:
                 print('''\n
                         **************************************************************************************
                         ***                                Letras Validas                                  ***
                         **************************************************************************************\n''')
                 contarLetras(obra)
            else:
                print(f'\nError Opcion no disponible\n')

        elif opc == 2:
            opc1 = int(input(f'''\n
                    ***********************************************************************
                    **********Menu Para Frecuencias y Entropias en Obra Parcial************
                    ***********************************************************************
                    \n
                    ** lo que desee realizar en la obra {nombre}\n
                    ** 1. Visualizar obra y seleccionar el texto que desee
                    ** 2. Volver al menu anterior                                        **
                  \n****  dijite  la opcion a realizar: '''))
            if opc1 == 1:
                print(f'''\n***********************************************************************
                            ** A continuacion se mostrará la obra:                               **
                            ***********************************************************************
                                                       \n''')
                mostrar(obra)
                # Solicitar texto para calcular frecuencia parcial
                texto = input(f'Ingrese el texto: ')
                opc2 = int(input(f'''
                                          \n***********************************************************************
                                            *******Menu Para Frecuencias y Entropias del texto seleccionado********
                                            ***********************************************************************
                                            \n
                                            ** lo que desee realizar en la obra:\n
                                            ** 1. Frecuencia de Palabras y entropia:                             **
                                            ** 2. Frecuencia de una palabra:                                     **
                                            ** 3. Contar Palabras:                                               **
                                            ** 4. Frecuencia de letras y entropia:                               **
                                            ** 5. Frecuencia de una letra                                        **
                                            ** 6. Contar Letras                                                  **
                                          \n****  dijite  la opcion a realizar: '''))
                if opc2 == 1:
                    print(f'''\n*************************************************************************
                                **               Tabla de frecuencias para el texto ingresado          **
                                *************************************************************************\n ''')
                    print(f'\nTermino---Ocurrencia---Frecuencia %\n')
                    frecuenciaPalabras(texto)
                    print(f'''\n
                                          **************************************************************************
                                          **            Entropia de del texto seleccionado        
                                          **************************************************************************
                                          \n''')
                    print(f'\nEntropia total\n')
                    entropiaPalabras(texto)
                elif opc2 == 2:
                     print(f'''\n
                              ***************************************************************************************
                              ***           Tabla de frecuencia para una palabra del texto parcial                ***
                              ***************************************************************************************\n''')
                     frecuenciaTermino(texto)
                elif opc2 == 3:
                     contarPalabras(texto)
                elif opc2 == 4:
                    print(f'''\n
                                ***************************************************************************************
                                **          Tabla de Frecuencias y Entropia de letras del texto ingresado            **
                                ***************************************************************************************\n''')
                    print(f'\nTermino-----Ocurrencia----Frecuencia %\n')
                    frecuenciaLetras(texto)
                    print(f'''\n
                              ***************************************************************************
                              **            Entropia de letras para el texto ingresado                 **
                              ***************************************************************************\n''')
                    entropiaLetras(obra)
                elif opc2 == 5:
                    print(f'''\n
                              ***************************************************************************
                              **                 Frecuencia de letras en el Texto                      **
                              ***************************************************************************\n''')
                    frecuenciaTerminoLetra(texto)
                elif opc2 == 6:
                     contarLetras(texto)
                else:
                    print(f'``               \nError Opcion no disponible\n''')
        elif opc == 3:
             print(f'''                    \nElija nuevamente el menu si desea realizar un calculo o salir del programa\n''')
        else:
            print(f'''                      \nDigite una opcion disponible\n''')




# =========================Fin de llamado a funcion principal========================================

# importacion de obras y abriendo archivos txt
donQuijote = open(
    'C:\\Users\\andre\\Desktop\\JUANDA-2022\\SEMESTRE 4-2021\\PROYECTO DISCRETAS\\PPP\\Frecuencias\\Cervances_Don_2020.txt', 'r', encoding='utf8')
donQuijote = donQuijote.read()

garciaCien = open(
    'C:\\Users\\andre\\Desktop\\JUANDA-2022\\SEMESTRE 4-2021\\PROYECTO DISCRETAS\\PPP\\Frecuencias\\Garcia_Cien_2020.txt', 'r', encoding='utf8')
garciaCien = garciaCien.read()

muerteAnunciada = open(
    'C:\\Users\\andre\\Desktop\\JUANDA-2022\\SEMESTRE 4-2021\\PROYECTO DISCRETAS\\PPP\\Frecuencias\\Cronicas_Muerte.txt', 'r', encoding='utf8')
muerteAnunciada = muerteAnunciada.read()

# Funcion para Mostrar texto original de Obra
def mostrar(obra):
    print(obra)


# Funcion Completa que calcula la frecuencia de una Obra Total
def frecuenciaPalabras(obra):
    global termino

    # convirtiendo lista en diccionario para acceder a cada uno de sus valores u ocurrencias
    diccionario = dict(entregarListaPalabras(obra))
    # sumando el total de ocurrencias
    total = sum(diccionario.values())

    for termino, valor in diccionario.items():
        #Formula para sacar la frecuencia de cada palabra
        frecuencia = ((valor / total) * 100)
        print(f'"{termino}"    {valor}     {round(frecuencia, 9)} %')

#prueba======================================================

# Funcion para hallar la entropia de shannon para palabras
def entropiaPalabras(obra):
    #convirtiendo obra en lista de cada palabra y sus ocurrencia en diccionario para acceder a cada uno de sus valores u ocurrencias
    diccionario = dict(entregarListaPalabras(obra))
    # sumando el total de ocurrencias
    total = sum(diccionario.values())
    print('Entropia Total de palabras')

    #Creando una lista vacia para almacenar las entropias obtenidas
    nuevalista = []
    #obteniendo cada valor de ocurrencia de cada termino o palabra
    for termino, valor in diccionario.items():
           #aplicando formula de entropia a cada valor u ocurrencia y almacenando cada una en la variable entropia
           entropia = ((valor / total)* -1)  *  (math.log((valor / total), 2))
           #funcion para agregar cada entropia obtenida en la nuevalista
           nuevalista.append(entropia)
    #optenemos la Nueva lista con todas las entropias las sumamos y redondeamos a 9 luego imprime entropia total
    print(round(sum(nuevalista), 9))

# Funcion para calcular la frecuencia de una palabra en la Obra Total
def frecuenciaTermino(obra):
    # convirtiendo lista en diccionario para acceder a cada uno de sus valores u ocurrencias
    diccionario = dict(entregarListaPalabras(obra))
    # sumando el total de ocurrencias
    total = sum(diccionario.values())
    ocurr = diccionario.values()

    palabraAbuscar = input('Digite la palabra a buscar en la obra: ')

    if palabraAbuscar in diccionario:
        frecuenciaPa = ((diccionario[palabraAbuscar] / total) * 100)
        print(f'\nTermino-----Ocurrencia-----Frecuencia %\n')
        print(f'"{palabraAbuscar}" {diccionario[palabraAbuscar]}  {round(frecuenciaPa, 9)} %')
    else:
        print(f'La palabra {palabraAbuscar} no se encuentra en la obra')

def contarPalabras(obra):
    # convirtiendo obra en lista de cada palabra y sus ocurrencia en diccionario para acceder a cada uno de sus valores u ocurrencias
    diccionario = dict(entregarListaPalabras(obra))
    # sumando el total de ocurrencias
    total = sum(diccionario.values())
    print('\nTotal de palabras válidas\n')
    print(total)

# Funcion para entregar lista de palabras y sus ocurrencias
def entregarListaPalabras(obra):
    entrada = obra

    signos = ".,:;-[]{}()<>'\"@/¿?¡! ¼ º"
    a_espacios = str.maketrans(signos, " " * len(signos))
    # convirtiendo de mayusculas a minusculas y contando por espacios
    palabras = str.translate(entrada, a_espacios).lower().split()
    # creando lista de objetos palabra y su ocurrencia total en obra
    contador = Counter(palabras).most_common()

    return contador

#===============================Funciones para calcular frecuencias y entropia de letras=======================================================

#Funcion para calcular frecuencia de letras
def frecuenciaLetras(obra):
    #creando diccionario de las 26 letras y sus ocurrencias
    diccioLetras = dict(entregarListaLetras(obra))

    totalLetras = sum(diccioLetras.values())

    for letra, ocurrencia in diccioLetras.items():
        #calcular frecuencia de cada letra
        frecuencia = ((ocurrencia / totalLetras) * 100)
        print(f'"{letra}"        {ocurrencia}    {round(frecuencia, 9)} % ')

#Funcion para calcular frecuencia de una letra
def frecuenciaTerminoLetra(obra):
    # convirtiendo lista en diccionario para acceder a cada uno de sus valores u ocurrencias
    diccionario = dict(entregarListaLetras(obra))
    # sumando el total de ocurrencias
    total = sum(diccionario.values())
    ocurr = diccionario.values()

    letraAbuscar = input('Digite la Letra a buscar en la obra: ')

    if letraAbuscar in diccionario:
        frecuenciaPa = ((diccionario[letraAbuscar] / total) * 100)
        print(f'\nLetra-----Ocurrencia-----Frecuencia %\n')
        print(f'"{letraAbuscar}"       {diccionario[letraAbuscar]}          {round(frecuenciaPa, 9)} %')
    else:
        print(f'La palabra {letraAbuscar} no se encuentra en la obra')

#Funcion para entropia de letras
def entropiaLetras(obra):
    # creando diccionario de las 26 letras y sus ocurrencias
    diccioLetras = dict(entregarListaLetras(obra))
    totalLetras = sum(diccioLetras.values())

    # Creando una lista vacia para almacenar las entropias obtenidas
    nuevalista = []

    print('Entropia Total de letras')
    for letra, ocurrencia in diccioLetras.items():
        # aplicando formula de entropia a cada valor u ocurrencia y almacenando cada una en la variable entropia
        entropia = ((ocurrencia / totalLetras) * -1) * (math.log((ocurrencia / totalLetras), 2))
        # funcion para agregar cada entropia obtenida en la nuevalista
        nuevalista.append(entropia)
    # optenemos la Nueva lista con todas las entropias las sumamos y redondeamos a 9 luego imprime entropia total
    print(round(sum(nuevalista), 9))

#Funcion para contar Letras validas
def contarLetras(obra):
    # convirtiendo obra en lista de cada palabra y sus ocurrencia en diccionario para acceder a cada uno de sus valores u ocurrencias
    diccionario = dict(entregarListaLetras(obra))
    # sumando el total de ocurrencias
    total = sum(diccionario.values())
    print('\nTotal de letras válidas\n')
    print(total)

#Funcion que me devuelve una lista con cada letra y su ocurrencia en un texto
def entregarListaLetras(obra):
    texto = ''.join(char for char in obra if char.isalnum())
    #Eliminando numeros del texto
    nuevoTexto = ''.join([i for i in texto if not i.isdigit()])
    # convertir el texto de la obra en una lista de simbolos separados
    newlist = list(normalize(nuevoTexto.upper()))

    #creando una lista de simbolos con su cantidad de ocurrencias ya formateado
    listaordenada = [[l, newlist.count(l)] for l in set(newlist)]

    return listaordenada


#funcion para quitar la tilde y otros simbolos a vocales
def normalize(texto):
    #simbolos a reemplazar
    replacements = (
        ("á", "a"),
        ("à", "a"),
        ("ä", "a"),
        ("â", "a"),
        ("ã", "a"),
        ("é", "e"),
        ("ê", "e"),
        ("ë", "e"),
        ("í", "i"),
        ("ï", "i"),
        ("Î", "i"),
        ("ó", "o"),
        ("ô", "o"),
        ("ö", "o"),
        ("ò", "o"),
        ("º", "O"),
        ("ú", "u"),
        ("¼", "U"),
        ("ü", "u"),
        ("ù", "u"),
        ("û", "u"),
    )
    #creando variables a reemplazar a, b
    for a, b in replacements:
        #reemplazando las vocales con tilde por estas mismas si ella
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    return texto
#====================================Llamado a funciones ===============================================
#principal()

opp = 's'
while opp == 's':
       principal()
       opp = input('Desea seguir realizando operaciones (s/n): ')
else:
    print(f'''\n
                                Saliendo del programa, Ah finalizado con exito''')