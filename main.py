def Calcular_palabra(palabra):
    xd = "?"*len(palabra)
    return xd

def Construir_palabra(palabra_referencia, palabra, letra):
     palabra_nueva = ''
     for i in range (len(palabra)):
         if(palabra_referencia[i] == letra):
             palabra_nueva += letra
         else:
             palabra_nueva += palabra[i]

     return palabra_nueva

def Es_repetida(letras_ingresadas, letra):
    return letra in letras_ingresadas


def Existe_letra(letra, palabra):
    return letra in palabra

def Validacion_ingreso(letra):
    return len(letra) != 1

def main():
    palabra_referencia = "piton"
    acierto_desacierto = [0,0]
    palabra = Calcular_palabra(palabra_referencia)
    letras_no_acertadas = []
    while acierto_desacierto[1] <= 7 and acierto_desacierto[0] < len(palabra):
        print("xdbienvendidos xd?")
        print("Palabra:", palabra)
        print("Aciertos:", acierto_desacierto[0], "Desaciertos:", acierto_desacierto[1])
        print("Letras no acertadas:", letras_no_acertadas)
        letra = input("Ingrese una letra: ")
        if Validacion_ingreso(letra):
            print("Es una letra, no una palabra")
        else:
           if Existe_letra(letra, palabra_referencia):
               if Es_repetida(palabra, letra):
                    print("La letra que queres ingresar, ya fue ingresada :")
               else: 
                    print("Bien xD")
                    palabra = Construir_palabra(palabra_referencia, palabra, letra)
                    acierto_desacierto[0] += 1
           else:
               acierto_desacierto[1] += 1
               letras_no_acertadas.append(letra)

    

main()