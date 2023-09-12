#---------------------------------------------------#
#Autor: Antonio Ramírez Martín                      #
#Ejercicio 2: "Hackeando, a lo bruto, a Julio César"#
#---------------------------------------------------#

#El módulo isfile comprueba si existe un archivo.
from os.path import isfile
from modulos import diccionario, decodificador

#Condición para evitar la creación del diccionario personalizado tras cada uso.
if isfile("Diccionario_personalizado.txt") == False:
    diccionario.crear_diccionario_personalizado()

decodificador.decodificar_claves(decodificador.leer_archivo_cifrado())
decodificador.buscar_clave_usada()
decodificador.mostrar_claves_consola()
