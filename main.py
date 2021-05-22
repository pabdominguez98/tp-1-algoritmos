def Calcular_palabra(palabra):
    xd = "?"*len(palabra)
    return xd
def Aciertos_desaciertos(acierto_desacierto, letra, palabra):
    if Existe_letra(letra, palabra):
        acierto_desacierto[0] += 1
    else:
        acierto_desacierto[1] += 1
    return acierto_desacierto

def Es_repetida(letras_ingresadas, letra):
    return letra in letras_ingresadas


def Existe_letra(letra, palabra):
    return letra in palabra

def Validacion_ingreso():
    pass

def main():
    palabra_prueba = "Piton"
    acierto_desacierto = [0,0]
    palabra = Calcular_palabra(palabra_prueba)
    while acierto_desacierto[1] <= 7 and acierto_desacierto[0] < len(palabra):
        print("xdbienvendidos xd?")
        print(palabra)