from q import enqueue
def pelea(a,b):
    while a['vida'] > 0 and b['vida'] > 0:
        a.atacar(b)
        if b.atributos['vida'] <= 0:
            print(f"El ganador es: {a['nombre']}")
            enqueue(b)
            break
        b.atacar(a)
        print(f"{a['vida']}, {b['vida']}")
        if a.vida <= 0:
            print(f"El ganador es: {b['nombre']}")
            enqueue(a)
"""es solo la funcion de peelar"""