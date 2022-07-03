#Nombre alumno: Patricio Reyes
#Bootcamp Python/Django

from funciones import *
print(" \n ========== Cuanto sabes sobre Chile ========== \n")
# ========== Aca va la Clase con atributo y metodo ==========
class Pais:
    def __init__(self, nombre):
        self.nombre = nombre


    def elegir(self):
        print(f"Has ingresado el pais: '{self.nombre.upper()}' \n")
        self.tema = str(input("Escoge el número del tema de tu interes: \n 1. Historia \n 2. Fiestas \n 3. Cultura \n 4. Salir del programa \n =>").upper())
        if self.tema == '1' or self.tema == 'HISTORIA':
            print("Has escogido 'Historia' \n")
            #llamar a una funcion con las preguntas
            historia()

        elif self.tema == '2' or self.tema == 'FIESTAS':
            print("Has escogido 'Fiestas'")
            # llamar a una funcion con las preguntas
            fiestas()

        elif self.tema == '3' or self.tema == 'CULTURA':
            print("Has escogido 'Cultura'")
            # llamar a una funcion con las preguntas
            cultura()

        elif self.tema == '4' or self.tema == 'SALIR':
            print("Fin del programa")
            exit()

        else:
            print("Ingresa un número de la lista, \n intentalo nuevamente... \n")
            return self.elegir()




# ========== Creamos un objeto ==========
pais1 = Pais('Chile')

print(pais1.elegir())




