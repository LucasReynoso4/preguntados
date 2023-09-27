import pygame
from constantes import *
from datos import lista
lista_preguntas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_respuesta_correcta = []
pregunta = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
posicion = 0
puntuacion = 0
errores = 2
running = True


pygame.init()
pygame.mixer.init()


pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
pygame.display.set_caption("PREGUNTADOS")

imagen = pygame.image.load("logo_preguntados.jpg")
imagen = pygame.transform.scale(imagen,(200,180))


musica = pygame.mixer.Sound("musica_fondo_desafio.mp3")


fuente = pygame.font.SysFont("Arial", 28)
texto_pregunta = fuente.render(str(pregunta), True,COLOR_BLANCO )
texto_respuesta_a = fuente.render(str(respuesta_a), True,COLOR_BLANCO )
texto_respuesta_b = fuente.render(str(respuesta_b), True,COLOR_BLANCO )
texto_respuesta_c = fuente.render(str(respuesta_c), True,COLOR_BLANCO )
texto_score = fuente.render(str(f"SCORE: {puntuacion}"), True,COLOR_BLANCO)

fuente_cuadrado = pygame.font.SysFont("Arial",30)
texto_pregunta_boton = fuente_cuadrado.render(str("PREGUNTA"), True,COLOR_BLANCO)
texto_reiniciar_boton = fuente_cuadrado.render(str("REINICIAR"), True,COLOR_BLANCO)
texto_final = fuente_cuadrado.render(str(f"PUNTUACION FINAL: {puntuacion}"), True,COLOR_BLANCO)


"""
Se recorre la lista de preguntas para almacenar las preguntas en las listas, las respuestas 'a','b' y 'c' y las correctas
"""

for e_lista in lista:
    lista_preguntas.append(e_lista['pregunta'])
    lista_respuesta_a.append(e_lista['a'])                                                        
    lista_respuesta_b.append(e_lista['b'])
    lista_respuesta_c.append(e_lista['c'])
    lista_respuesta_correcta.append(e_lista['correcta'])

musica.set_volume(0.1)
musica.play()

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            """
                Ubicacion del boton pregunta del programa se coloca la posicion en el rectangulo antes dibujado que esta arriba
                se muestran las preguntas, las respuestas y se inicia de nuevo errores en 2 para cada siguiente pregunta cuando se toque
                el boton                          
            """
            if(posicion_click[0] > 300 and posicion_click[0]< 490) and(posicion_click[1] > 20 and posicion_click[1])< 100 :
                errores = 2
                pregunta = lista_preguntas[posicion]
                respuesta_a =lista_respuesta_a[posicion]
                respuesta_b =lista_respuesta_b[posicion]
                respuesta_c =lista_respuesta_c[posicion]
                texto_pregunta = fuente.render(str(pregunta), True, COLOR_BLANCO)
                texto_respuesta_a = fuente.render(str(respuesta_a), True, COLOR_BLANCO)
                texto_respuesta_b = fuente.render(str(respuesta_b), True, COLOR_BLANCO)
                texto_respuesta_c = fuente.render(str(respuesta_c), True, COLOR_BLANCO)

            """
                Boton reinicio del programa declara las variables iniciadas en 0 junto a la puntuacion y el indice(posicion) y
                se limpia la pantalla de las preguntas y las respuestas
            """
            if(posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 500 and posicion_click[1]< 590):
                puntuacion = 0
                posicion = 0
                texto_pregunta = fuente.render(str(" "), True, COLOR_BLANCO)
                texto_respuesta_a = fuente.render(str(" "), True, COLOR_BLANCO)
                texto_respuesta_b = fuente.render(str(" "), True, COLOR_BLANCO)
                texto_respuesta_c = fuente.render(str(""), True, COLOR_BLANCO)
                texto_score = fuente.render(str(f"SCORE: {puntuacion}"), True,COLOR_BLANCO)

            """
            Boton de respuesta 'a' si la respuesta A es correcta deja de mostrar las demas respuestas y renderiza la posicion+=1 al tocar 
            el boton de pregunta pasa a la proxima y si no es correta se resta un error ya que esta inicializada en 2 y se deja de 
            mostrar la respuesta clickeada
            """
            if (posicion_click[0] >= 20 and posicion_click[0] <= 169) and (posicion_click[1] >= 350 and posicion_click[1] <= 400): 
                    if lista_respuesta_correcta[posicion] == "a":                       
                        puntuacion += 10
                        posicion += 1
                        respuesta_b = ""
                        texto_respuesta_b = fuente.render(str(respuesta_b), True, COLOR_BLANCO)
                        respuesta_c = ""
                        texto_respuesta_c = fuente.render(str(respuesta_c), True, COLOR_BLANCO)
                        texto_score = fuente.render(str(f"SCORE: {puntuacion}"), True,COLOR_BLANCO) 
                    else: 
                        errores -= 1
                        respuesta_a = ""
                        texto_respuesta_a = fuente.render(str(respuesta_a), True, COLOR_BLANCO)


                    """
                    Boton 'b'
                    """         

            elif (posicion_click[0] > 300 and posicion_click[0] < 399) and (posicion_click[1] > 350 and posicion_click[1] < 400):
                    if lista_respuesta_correcta[posicion] == "b":
                        puntuacion += 10
                        posicion += 1
                        respuesta_a = ""
                        texto_respuesta_a = fuente.render(str(respuesta_a), True, COLOR_BLANCO)
                        respuesta_c = ""
                        texto_respuesta_c = fuente.render(str(respuesta_c), True, COLOR_BLANCO)
                        texto_score = fuente.render(str(f"SCORE: {puntuacion}"), True,COLOR_BLANCO)
                    else: 
                        errores -= 1
                        respuesta_b = ""
                        texto_respuesta_b = fuente.render(str(respuesta_b), True, COLOR_BLANCO)

                    """
                    Boton 'c'
                    """     

            elif (posicion_click[0] > 550 and posicion_click[0] < 779) and (posicion_click[1] > 350 and posicion_click[1] < 400):
                    print("Aca esta 3")
                    if lista_respuesta_correcta[posicion] == "c":
                        puntuacion += 10
                        posicion += 1
                        respuesta_a = ""
                        texto_respuesta_a = fuente.render(str(respuesta_a), True, COLOR_BLANCO)
                        respuesta_b = ""
                        texto_respuesta_b = fuente.render(str(respuesta_b), True, COLOR_BLANCO)
                        texto_score = fuente.render(str(f"SCORE: {puntuacion}"), True,COLOR_BLANCO)
                    else: 
                        errores -= 1
                        respuesta_c = ""
                        texto_respuesta_c = fuente.render(str(respuesta_c), True, COLOR_BLANCO)


            """
            Se verifica que si la cantidad de errores del usuario es igual a 0 ,ya que cada vez que se clickea la respuesta correctamente
            se resta el error - 1, se ocultan las respuestas para que el usuario no tenga posibilidad de contestar y suma la posicion para que
            renderize y al tocar el boton de pregunte pase a la siguiente pregunta
            
            """

            if errores == 0:
                posicion += 1
                respuesta_a = ""
                texto_respuesta_a = fuente.render(str(respuesta_a), True, COLOR_BLANCO)
                respuesta_b = ""
                texto_respuesta_b = fuente.render(str(respuesta_b), True, COLOR_BLANCO)
                respuesta_c = ""
                texto_respuesta_c = fuente.render(str(respuesta_c), True, COLOR_BLANCO)
                texto_score = fuente.render(str(f"SCORE: {puntuacion}"), True,COLOR_BLANCO)


    """
    Si la posicion es igual a largo de la lista, osea cuando llegue al final de la lista de preguntas se pinta la pantalla en azul y muestra la
    puntuacion del usuario y le da la oportunidad de reiniciar el programa para jugar nuevamente
    """

    if posicion == len(lista_preguntas):
        pantalla.fill(COLOR_AZUL)
        texto_final = fuente_cuadrado.render(str(f"PUNTUACION FINAL: {puntuacion}"), True,COLOR_BLANCO)
        pantalla.blit(texto_final, (250 ,200))
        pygame.draw.rect(pantalla,COLOR_ROJO,(300,500,190,80))
        pantalla.blit(texto_reiniciar_boton,(315,520))
    else:
        pantalla.fill(COLOR_AZUL)
        pygame.draw.rect(pantalla,COLOR_PRUEBA,(300,20,190,80))
        pygame.draw.rect(pantalla,COLOR_PRUEBA,(300,500,190,80))
        pygame.draw.rect(pantalla,COLOR_AZUL,(20,350,190,60)) #izq a derecha, top arriba para abajo, ancho , largo
        pygame.draw.rect(pantalla,COLOR_AZUL,(300,350,190,60)) #izq a derecha
        pygame.draw.rect(pantalla,COLOR_AZUL,(550,350,229,60))
        pantalla.blit(imagen,(POSICION_IMAGEN))
        pantalla.blit(texto_pregunta_boton,(315,40))
        pantalla.blit(texto_reiniciar_boton,(315,520))
        pantalla.blit(texto_pregunta,(10,250))
        pantalla.blit(texto_respuesta_a,(20,360))
        pantalla.blit(texto_respuesta_b,(300,360)) #X&Y 
        pantalla.blit(texto_respuesta_c,(550,360))
        pantalla.blit(texto_score,(630,10))

    pygame.display.flip()


pygame.quit()
