


def Calcular_palabra(palabra):
    xd = "?"*len(palabra)
    return xd

def Construir_palabra(palabra_a_adivinar, palabra_con_signos_de_pregunta, letra):
    """
    Toma la palabra original, la palabra q tienen los "?" y letras que ya haya adivinado, y la letra q haya ingresado el usuario en la ultima carga; genera 
    una nueva palabra en la cual, se va a ir fijando en cada posicion de la palabra que tine q adivinar el 
    usuario, y si la letra de la palabra coincide con la letra que se ingresa por parametro, en la nueva palabra, se
    le va a asignar la letra, en cualquier otro caso, se le va a asignar la letra o en su defecto un "?", que 
    haya en la palabra con signos de pregunta

    """

    palabra_nueva = ''
    for i in range(len(palabra_con_signos_de_pregunta)):
        if palabra_a_adivinar[i] == letra:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra_con_signos_de_pregunta[i]

    return palabra_nueva

def Es_repetida(letras_ingresadas, letra):
    return letra in letras_ingresadas


def Existe_letra(letra, palabra):
    return letra in palabra

def Ingreso_Valido(letra):
    """
    Cambié para que tambien se fije que están ingresando solo letras
    """
    resp = False
    if len(letra) == 1 and letra.isalpha():
        resp = True

    return resp

def agregar_letra_no_acertada(letras_no_acertadas, letra):
    if not letra in letras_no_acertadas :
        letras_no_acertadas += letra + " "
    
    return letras_no_acertadas

def main():
    palabra_a_adivinar = "juego"
    acierto_desacierto = [0,0]
    palabra_con_signos_de_pregunta = Calcular_palabra(palabra_a_adivinar)
    letras_no_acertadas = " "
    print("Palabra a adivinar:", palabra_con_signos_de_pregunta, end = "    ")
    print("Aciertos:", acierto_desacierto[0], "  -  Desaciertos:", acierto_desacierto[1]) 

    while acierto_desacierto[1] <= 7  and  acierto_desacierto[0] < len(palabra_con_signos_de_pregunta):
        letra = input("Ingrese una letra: ")
        
        if not Ingreso_Valido(letra):
            
            print("Debe ingresar una única letra.")
      
        else:

           if Existe_letra(letra, palabra_a_adivinar):

               if Es_repetida(palabra_con_signos_de_pregunta, letra):
                
                   print("La letra que queres ingresar ya fue ingresada, intenta con otra: ")


               else: 
                    palabra_con_signos_de_pregunta = Construir_palabra(palabra_a_adivinar, palabra_con_signos_de_pregunta, letra)
                    acierto_desacierto[0] += 1

                    print("Bien!! ->  ", palabra_con_signos_de_pregunta, end = "  ") 
                    print("Aciertos:", acierto_desacierto[0], "  -   Desaciertos:", acierto_desacierto[1], end = "  ")
                    print("Letras no acertadas:", letras_no_acertadas)

           else:
               acierto_desacierto[1] += 1
               letras_no_acertadas = agregar_letra_no_acertada(letras_no_acertadas, letra)
               print("Lo siento!!! ->  ", palabra_con_signos_de_pregunta, end = "     ") 
               print("Aciertos:", acierto_desacierto[0], " -  Desaciertos:", acierto_desacierto[1], end = " ;  ")
               print("Letras no acertadas:", letras_no_acertadas)

    

main()