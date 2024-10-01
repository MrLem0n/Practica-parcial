class Habilidad:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def agregarHabilidad(self,nombre,nivel=1):
        nombre = input("nombre de la habilidad")
        habilidad = Habilidad(nombre, nivel)
        habilidades.append(habilidad)
        print("habilidad agregada con exito!")
    def mejorar(self):
        self.nivel +=1
        print(f"Habilidad '{self.nombre}' mejorada a nivel {self.nivel}. ")

habilidades=[]

