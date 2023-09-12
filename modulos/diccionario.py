#---------------------------------------------------#
#Autor: Antonio Ramírez Martín                      #
#Ejercicio 2: "Hackeando, a lo bruto, a Julio César"#
#                                                   #
#Módulo para la creación del diccionario            #
#---------------------------------------------------#


#Función para crear un diccionario a partir de otro, sin tildes, diéresis y en mayúsculas.
def crear_diccionario_personalizado():
    
    archivo_diccionario = open('Diccionario.txt', 'r')
    archivo_salida = open('Diccionario_personalizado.txt', 'w')    
    
    #Para todas las palabras mayores de dos caracteres (tres incluyendo el caracter de salto de línea en Window) sustituimos 
    #caracteres si es necesario, los agregamos al nuevo diccionario y ponemos las palabras en mayúsculas.
    for linea in archivo_diccionario:
        if len(linea) > 3:
            linea = linea.replace("á", "a")
            linea = linea.replace("é", "e")
            linea = linea.replace("í", "i")
            linea = linea.replace("ó", "o")
            linea = linea.replace("ú", "u")
            linea = linea.replace("ü", "u")
            linea = linea.replace("ñ", "nn")
            linea = linea.upper()
            archivo_salida.write(linea)
    
    archivo_diccionario.close()
    archivo_salida.close()
