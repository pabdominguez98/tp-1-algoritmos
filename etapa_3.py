import random

def seleccion_palabra(diccionario, longitud):
    lista_palabras = list(diccionario.keys())
    lista_palabras_longitud = []
    for i in range (len(lista_palabras)):
        if len(lista_palabras[i]) == longitud:
            lista_palabras_longitud.append(lista_palabras[i]) 
    
    random_num = random.randint(0, len(lista_palabras_longitud) - 1)
     
    return lista_palabras_longitud[random_num]
    


def main():
    diccionario = {
        'carlos': 1,
        'juan': 321,
        'hola': '3',
        'dsadsa': 3,
        '4444':3
    }
    
    print(seleccion_palabra(diccionario, 4))


main()


