"""Desarrollar un sistema integrado de robots famosos del cine y las series utilizando listas enlazadas,
clases, colas, pilas y árboles. Este sistema debe funcionar como un juego de rol donde se puedan realizar
las siguientes acciones:
Registrar un robot: Cada robot debe tener un nombre, una serie/película de origen, habilidades y
puntos de vida.

Listar robots: Mostrar todos los robots registrados.

Batalla de robots: Dos robots se enfrentan y se determina el ganador basado en sus habilidades y
puntos de vida.

Historial de batallas: Utilizar una pila para almacenar el historial de batallas.

Reparación: Los robots dañados se agregan a una estructura ordenada de reparación.

Habilidades: Representar las habilidades de los robots en una estructura para facilitar la búsqueda
y mejora de habilidades.

Mejora de habilidades: Los robots pueden mejorar sus habilidades.

Batalla entre todos los robots: Se enfrentan todos los robots y se determina el ganador. Debe ser
al estilo de un torneo.

Es importante justificar la elección de cada estructura de datos y cómo se integran para resolver el sistema
de manera eficiente. Explique cómo se resuelven los problemas de concurrencia y cómo se garantiza la
integridad de los datos. Y lo más importante, que sea con sus propias palabras."""

import random
class Robots:
    
    def __init__(self, nombre, defensa, ataque, agilidad, vida, lugar_origen,habilidad_especial ,contador=0 ): 
       
        self.nombre = nombre
        self.defensa = defensa
        self.ataque = ataque
        self.agilidad = agilidad
        self.vida = vida
        self.lugar_origen = lugar_origen
        self.habilidad_especial = habilidad_especial
        self.contador = contador


    def subir_estat(self, defensa, ataque, agilidad, vida ):
        self.defensa = self.defensa + defensa
        self.ataque = self.ataque + ataque
        self.agilidad = self.agilidad + agilidad
        self.vida = self.vida + vida

    def vive(self):
        return self.vida >0
    
    def derrota(self):
        self.vida = 0
        print(self.nombre, "ha sufrido una derrota")
    def attack(self, Robots):
        damage = random.randint(1, 100)
        Robots.vida -= damage
        
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def ataque(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "daño fisico a", enemigo.nombre)
        print("La vida de", enemigo.nombre, "es", enemigo.vida)
    
    

    
    def mostrar_robot(self):
        print (f"El robot es {self.nombre}, su lugar de origen es {self.lugar_origen}, y la vida es {self.vida} ")


Robots_registrados: list[Robots] = []

def registrar_robot():
    nombre = input("Ingrese el nombre de su robot: ")
    lugar_origen =input("Ingrese la serie o pelicula de su origen: ")
    habilidad_especial = input("Ingrese la habilidad especial del robot: ")
    
    nuevo_robot = Robots(nombre, 0, 0, 0, 100, lugar_origen,habilidad_especial)
    Robots_registrados.append(nuevo_robot)
    print ("Su robot ha sido registrado correctamente: ")

def batalla(a,b):

        while a.vida > 0 and b.vida > 0:
            a.attack(b)
           
            if b.vida <= 0:
                print(f"El ganador es: {a.nombre}")
                break
            b.attack(a)
            print(f"{a.vida}, {b.vida}")
            if a.vida <= 0:
                print(f"El ganador es: {b.nombre}")
            break
def mostrar_robots():
    for robot in Robots_registrados:
        robot.mostrar_robot()

    

def menu():
    print("soy un gordo nazi")
    while True:
        print   ("\nMenú: ")
        print   ("0. Salir")
        print   ("1. Registrar robot ")
        print   ("2. Robots registrados ")
        print   ("3. Batalla de robots")
       

        opcion = input ("Elija una opción: ")

        if opcion == '0':
            break
        elif opcion == '1':
            registrar_robot()
        elif opcion == '2':
            mostrar_robots
        elif opcion == '3':
            if Robots_registrados:
                print(f"Elija que robots desea que peleen: {mostrar_robots()}")

                a=int(input("ingrese el peleador 1: "))
                b=int(input("ingrese el peleador 2: "))
                batalla(Robots_registrados[a],Robots_registrados[b])
            else:
                print("No hay robots registrados.")
       
            
        else:
            print ("Opcion no valida, intente nuevamente.")


menu()


        