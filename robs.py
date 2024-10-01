from habilidad import Habilidad
from q import enqueue
from batalla import pelea
import random
class Robots:
    
    def __init__(self, nombre, defensa, ataque, vida, lugar_origen ,contador=0 ): 
       
        self.atributos = {
            'nombre': nombre,
            'defensa': defensa,
            'ataque': ataque,
           
            'vida': vida,
            'lugar_origen': lugar_origen,
            
            'contador': contador
        }

    def __str__(self):
        return f"Robot(nombre={self.atributos['nombre']}, lugar_origen={self.atributos['lugar_origen']})"


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
        damage = random.randint(0, 100)
        Robots.vida -= damage
        
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    

    
    

    
   


Robots_registrados=[]

def registrar_robot():
    nombre = input("Ingrese el nombre del robot: ").capitalize
    defensa = int(input("Ingrese la defensa del robot: "))
    ataque = int(input("Ingrese el ataque del robot: "))

    vida=100
    lugar_origen = input("Ingrese el lugar de origen del robot: ").capitalize
    habilidad_especial = input("Ingrese la habilidad especial del robot: ").capitalize
    contador=0
    nuevo_robot=Robots(nombre,defensa,ataque,vida,lugar_origen,habilidad_especial,contador)
    Robots_registrados.append(nuevo_robot)

    
    

def mostrar_robots():
    for robot in Robots_registrados:
        print(f"Nombre: {robot.atributos['nombre']}, Lugar de origen: {robot.atributos['lugar_origen']}")

    

def menu():
    
    while True:
        print   ("\nMenú: ")
        print   ("0. Salir")
        print   ("1. Registrar robot ")
        print   ("2. Robots registrados ")
        print   ("3. Filtrar")
        print   ("4. Batalla de robots")

        opcion = input ("Elija una opción: ")

        if opcion == '0':
            break
        elif opcion == '1':
            registrar_robot()
        elif opcion == '2':
            mostrar_robots()
        elif opcion == '3':
            if Robots_registrados:
             consulta()
            else:
                print("No hay robots registrados.")
        elif opcion == '4':
            a=input("ingrese el peleador 1(nombre)")
            b=input("ingrese el peleador 2(nombre)")
            pelea(a,b)
       
            
        else:
            print ("Opcion no valida, intente nuevamente.")

def consulta():
    a=input("Ingrese el nombre del robot")
    for robot in Robots_registrados:
        if robot.atributos["nombre"] == a:
            print(robot)
   
    
    

menu()