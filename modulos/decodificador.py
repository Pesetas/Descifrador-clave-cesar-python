#---------------------------------------------------#
#Autor: Antonio Ramírez Martín                      #
#Ejercicio 2: "Hackeando, a lo bruto, a Julio César"#
#                                                   #
#Módulo decodificador de clave                      #
#---------------------------------------------------#


#Lee el archivo cifrado y devuelve una cadena sin espacios, que será sobre la que trabajaremos.
def leer_archivo_cifrado():
    archivo = open('fichero_cifrado.txt', 'r')
    cadena_cifrada = archivo.read()
    archivo.close()
    cadena_cifrada = cadena_cifrada.replace(" ", "")
    return cadena_cifrada


#Decodifica el cifrado usando las 27 claves y las añade al archivo "fichero_plano.txt"
def decodificar_claves(cadena_cifrada):
    archivo_fichero_plano = open('fichero_plano.txt', 'w')
    
    for clave in range(0,26):
        archivo_fichero_plano.write(str(clave) + " - ")
        for caracter_cifrado in cadena_cifrada:
            archivo_fichero_plano.write(chr(65 + ((ord(caracter_cifrado) - clave + 13) % 26)))
        archivo_fichero_plano.write("\n")
        
    archivo_fichero_plano.close()

#Busca el número de coincidencias por líneas entre el "diccionario_modificado" y el "fichero_plano" y nos indica cuál 
#podría ser la clave válida.
def buscar_clave_usada():
    archivo_fichero_plano = open('fichero_plano.txt', 'r+')
    archivo_diccionario = open('Diccionario_personalizado.txt', 'r')
    
    #Identifica el número de palabras que coinciden con el diccionario de cada línea descifrada.
    lista_crackeo = []
    for linea_clave in archivo_fichero_plano:
        contador = 0
        for linea in archivo_diccionario:
            if (linea_clave.find(linea[:(len(linea)-1)]) != -1):
                contador += 1
        lista_crackeo.append(contador)
        archivo_diccionario.seek(0)
    archivo_diccionario.close()
    
    #Busca el mayor valor de coincidencias, su posición y nos lo indica tanto por terminal como en el "fichero_plano".
    mayor = 0
    posicion = 0
    for valor in lista_crackeo:
        if valor > mayor:
            mayor = valor
            posicion_mayor = posicion
        posicion += 1
    
    #Busca la posición de la frase clave y la guarda.
    archivo_fichero_plano.seek(0)
    contador = 0
    for linea in archivo_fichero_plano:
        contador += 1
        if contador == posicion_mayor:
            frase_clave = archivo_fichero_plano.readline()
    
    archivo_fichero_plano.write("\nEl código más probable es el que se encuentra en la clave nº " + frase_clave)
    archivo_fichero_plano.seek(0)
    
    
    archivo_fichero_plano.close()

#Lee las claves del archivo y las muestra las claves en pantalla
def mostrar_claves_consola():
    archivo_fichero_plano = open('fichero_plano.txt', 'r')
    print("\nLista de resultados por clave:\n")
    print(archivo_fichero_plano.read())
    archivo_fichero_plano.close()

