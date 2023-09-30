from ClaseArbol import arbol


def frontera(ar, nodo):
    if nodo:
        if nodo.getIzq() is None and nodo.getDer() is None:
            print(nodo.getdato())
        frontera(ar, nodo.getIzq())
        frontera(ar, nodo.getDer())


if __name__ == "__main__":
    a = arbol()
    a.insertar(19)
    a.insertar(5)
    a.insertar(15)
    a.insertar(3)
    a.insertar(20)
    a.insertar(9)

    print(f'La frontera del arbol es: ')
    frontera(a, a.getcabeza())

