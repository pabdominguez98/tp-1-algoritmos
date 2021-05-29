import re
import unidecode


def sacar_tildes(palabra):
    palabra = palabra.upper()
    string_s = palabra.replace('Ñ', '@')
    o_string = unidecode.unidecode(string_s)
    string_n = o_string.replace('@', 'Ñ')
    return string_n


def palabras_validas(texto):
    lista_palabra_valida = []

    for palabra in re.split(' |-|_|\n', texto):
        palabra_sin = ''
        for letra in palabra:
            if (letra.isalpha()):
                palabra_sin += letra
        if (len(palabra_sin) >= 5):
            lista_palabra_valida.append(sacar_tildes(palabra_sin))

    return lista_palabra_valida


def crear_diccionario(lista_palabras):
    diccionario_palabras = {}

    for palabra in lista_palabras:
        if (palabra in diccionario_palabras):
            diccionario_palabras[palabra] += 1

        else:
            diccionario_palabras[palabra] = 1

    return dict(sorted(diccionario_palabras.items(), key=lambda palabra: palabra[0]))


texto = '''
Al anochecer llegó Ñoñería Ñeembucú la noticia. Sí que había _firmica_. Aquella señora
que Rafael se imaginaba allá en Madrid con todos los esplendores y
adornos que el Padre Eterno tiene en los altares, vencida por telegramas
y súplicas, prolongaba la vida del sentenciado.

El indulto produjo en la cárcel un estrépito de mil demonios, como si
cada uno de los presos hubiera recibido la orden de libertad.

--Alégrate, mujer--decía en el rastrillo el cura a la mujer del
indultado--. Ya no matan a tu marido: no serás viuda.
'''
print(palabras_validas(texto))