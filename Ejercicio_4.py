from ClaseArbol import arbol

if __name__ == "__main__":
    a = arbol()
    a.insertar(19)
    a.insertar(5)
    a.insertar(15)
    a.insertar(3)
    a.insertar(20)
    a.insertar(9)

    # Muesta el padre y el hermano del valor ingresado en este caso (15) Padre:5 Hermano:3
    a.Padre_Hermano(15)

    # Mostrar cantidad de nodos del arbol en forma recursiva
    print(f'Los nodos del arbol son: {a.contar_recursivamente(a.getcabeza())}')

    # Mostrar la Altura de un Arbol
    print(f'La altura del Arbol es: {a.altura(a.getcabeza())}')
    nodo = int(input('Ingrese nodo para saber sucesores: '))
    # Mostrar los Sucesores de un nodo ingresado por teclado
    print(f'Sucesores de {nodo}:', a.sucesores(nodo))



