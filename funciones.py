# Aca van las preguntas dentro de funciones
def historia():
    # Pregunta 1
    puntaje = 0
    pregunta1 = str(input("Pregunta 1: \n ¿Cuantas regiones tiene Chile? \n a) 16 \n b) 13 \n c) 10 \n Ingrese su respuesta: ").upper())
    if pregunta1 == 'A' or pregunta1 == '16':
        print("Respuesta correcta \n has ganado 10 puntos")
        puntaje = puntaje + 10

    else:
        print("\n Respuesta incorrecta...!!! \n \n Hasta 2007 las regiones de Chile fueron 13; y desde aquel año el total fue de 15 regiones, \n número que aumento a 16 a partir del 6 de septiembre de 2018.")

    print("\n")

    # PREGUNTA 2
    respuesta2 = str(input(
        "Pregunta 2: \n ¿Cual es la capital de Chile? \n a)Antofagasta \n b)Santiago \n c)Valparaiso \n ").upper())

    if respuesta2 == 'SANTIAGO' or respuesta2 == 'B':
        print("\n Respuesta correcta \n has ganado 10 puntos")
        puntaje = puntaje + 10


    else:
        print(
            "Respuesta incorrecta...!!! \n \n Santiago es la capital de Chile fundada el 14 de febrero de 1541 en el valle del río Mapocho, a los pies del cerro Santa Lucía, por el adelantado Pedro de Valdivia. \n")


    print("\n")

    # PREGUNTA 3
    respuesta3 = str(input(
        "Pregunta 3: \n ¿Que idioma se habla en Chile? \n a)Inglés \n b)Portugues \n c)Español \n Ingrese su respuesta: ").upper())

    if respuesta3 == 'ESPAÑOL' or respuesta3 == 'C':
        print("\n Respuesta correcta \n has ganado 10 puntos")
        puntaje = puntaje + 10


    else:
        print(
            "\n Respuesta incorrecta...!!! \n \n El español es el idioma oficial de facto y la lengua administrativa de Chile, hablado por el 99,3 % de la población.")

    print("\n")
    print(f"El total de tus puntos es {puntaje} de 30")




def fiestas():
    # PREGUNTA 1
    respuesta1 = str(input("Pregunta 1: \n ¿Que se celebra el 21 de Mayo en Chile? \n a)El año nuevo \n b)El día de las Glorias Navales \n c)La fiesta de la Tirana \n Ingrese su respuesta: ").upper())
    puntaje = 0
    if respuesta1 == 'B' or respuesta1 == 'EL DIA DE LAS GLORIAS NAVALES':
        print("Respuesta correcta \n has ganado 10 puntos")
        puntaje = puntaje + 10
    else:
        print(
            "\n Respuesta incorrecta...!!! \n \n El 21 de Mayo se celebra el Día de las Glorias Navales, el combate naval de Iquique que ocurrio entre Chile y Perú en 1879.")

    print("\n")

    # PREGUNTA 2
    respuesta2 = str(input("Pregunta 2: \n ¿Cuando son las Fiestas Patrias? \n a)18 de septiembre \n b)1 enero \n c)27 Junio \n Ingrese su respuesta: ").upper())
    if respuesta2 == 'A' or respuesta1 == '18 de septiembre':
        print("Respuesta correcta \n has ganado 10 puntos")
        puntaje = puntaje + 10
    else:
        print(
            "\n Respuesta incorrecta...!!! \n \n El 18 de septiembre se conmemora, porque en esta misma fecha pero en 1810, se creo la Primera Junta Nacional de Gobierno, lo que dio paso al proceso de independencia para Chile.")

    print("\n")
    print(f"El total de tus puntos es {puntaje} de 20")


def cultura():
    # PREGUNTA 1
    respuesta1 = str(input("Pregunta 1: \n ¿Cual es el baile nacional Chileno? \n a)Reggaeton \n b)Cumbia \n c)Cueca \n Ingrese su respuesta: ").upper())
    puntaje = 0
    if respuesta1 == 'C' or respuesta1 == 'CUECA':
        print("Respuesta correcta \n has ganado 10 puntos")
        puntaje = puntaje + 10
    else:
        print("\n Respuesta incorrecta...!!! \n \n La cueca es el baile nacional de Chile, fue escogido como simbolo de la cultura Chilena, ya que nació a partir de una mezcla entre ritmos amerindios y españoles.")

    print("\n")

    # PREGUNTA 2
    respuesta2 = str(input("Pregunta 2: \n Escoja los platos tipicos Chilenos \n a)Cazuela \n b)Charquican \n c)Curanto \n d)Humitas \n e)Todas \n Ingrese su respuesta: ").upper())
    if respuesta2 == 'E' or respuesta2 == 'TODAS':
        print("Respuesta correcta \n has ganado 10 puntos")
        puntaje = puntaje + 10
    else:
        print("\n Respuesta incorrecta...!!! \n \n La gastronomía Chilena tiene muchos platos de comida tipica entre ellos los nombrados anteriormente, aunque se dicen que tambien son: el caldillo de congrio, carbonada, chancho en piedra y la empanda de pino, entre otros.")

    print("\n")
    print(f"El total de tus puntos es {puntaje} de 20")


