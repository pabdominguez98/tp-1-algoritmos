from Texto import obtener_texto


def palabras_validas(texto_a_procesar):
    lista_palabra_valida = []
    
    for palabra in texto_a_procesar.split():
        palabra_sin = ''
        for letra in palabra:
            if (letra.isalpha()):
                palabra_sin += letra
                
        if (len(palabra_sin) >= 5):
            lista_palabra_valida.append(palabra_sin.lower())

    return lista_palabra_valida

def crear_diccionario(lista_palabras):
    diccionario_palabras = {}

    for palabra in lista_palabras:
        if (palabra in diccionario_palabras):
            diccionario_palabras[palabra] += 1

        else:
            diccionario_palabras[palabra] = 1

    return dict(sorted(diccionario_palabras.items(), key = lambda palabra: palabra[0]))




#NUEVA!
def eliminar_no_letras(texto) :
    """
    Al final la cambíe y hace algo parecido a lo que hace palabras_validas(), pero aparte de sacar los puntos comas y demas,
    tambn elimina todo lo q no sea una letra y lo reemplaza por un espacio. hay casos en los que hay dos guiones seguidos: "--" y 
    los reemplaza por dos espacios: "  ", eso no genera ningun problema, xq cuando hace split separa las palabras bien, lo probé con un ejemplo
    en el q incluso hay 5 espacios entre palabra y palabra :)

    """

    nueva = ''
    for i in range(len(texto)):
        if not texto[i].isalpha():
            nueva += ' '
        else:
            nueva += texto[i]
        
    nueva = nueva.split()
    return nueva


texto = obtener_texto()
texto_en_lista  = eliminar_no_letras(texto)
diccionario = crear_diccionario(texto_en_lista)


print(diccionario.keys())