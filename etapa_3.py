import random

def seleccion_palabra(diccionario, longitud):
    lista_palabras = diccionario.keys()
    lista_palabras_longitud = []
    for i in range (len(lista_palabras)):
        if len(lista_palabras[i]) == len(longitud):
            lista_palabras_longitud.append(lista_palabras[i]) 
    
    random_num = random.randint(0, len(lista_palabras_longitud) - 1)
     
    return lista_palabras_longitud[random_num]
    


def main():
    numero = random.randint(0,99)

    print(numero)


