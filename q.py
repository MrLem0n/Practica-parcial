colaRep=[]


def enqueue(robot):
    if robot.atributos['vida']==0:
        colaRep.append(robot)
        print(f"Robot {robot.atributos['nombre']} añadido a la cola")