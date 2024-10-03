class Nodo:
    def __init__(self, equipo):
        self.equipo = equipo
        self.izquierda = None
        self.derecha = None

class ArbolTorneo:
    def __init__(self):
        self.raiz = None

    def agregar_partido(self, equipo):
        if self.raiz is None:
            self.raiz = Nodo(equipo)
        else:
            self._agregar_recursivo(self.raiz, equipo)

    def _agregar_recursivo(self, nodo, equipo):
        if nodo.izquierda is None:
            nodo.izquierda = Nodo(equipo)
        elif nodo.derecha is None:
            nodo.derecha = Nodo(equipo)
        else:
            self._agregar_recursivo(nodo.izquierda, equipo)

    def simular_torneo(self, nodo):
        if nodo.izquierda is not None and nodo.derecha is not None:
            ganador_izquierda = self.simular_torneo(nodo.izquierda)
            ganador_derecha = self.simular_torneo(nodo.derecha)
            # Aquí puedes definir la lógica para determinar el ganador
            ganador = ganador_izquierda if ganador_izquierda > ganador_derecha else ganador_derecha
            print(f"Partido entre {ganador_izquierda} y {ganador_derecha}. Ganador: {ganador}")
            return ganador
        return nodo.equipo

# Ejemplo de uso
equipos = ["Equipo A", "Equipo B", "Equipo C", "Equipo D"]
torneo = ArbolTorneo()
