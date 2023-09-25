from ClaseArbol import arbol

if __name__ == "__main__":
    a = arbol()
    a.insertar(19)
    a.insertar(5)
    a.insertar(15)
    a.insertar(3)
    a.insertar(20)
    a.insertar(9)
    frontera = []
    hojas = a.frontera(a.getcabeza(), frontera)
    print(f'La frontera del arbol es: {hojas}')


