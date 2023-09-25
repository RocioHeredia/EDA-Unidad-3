class Nodo:
    __dato = int
    __izq = None
    __der = None

    def __init__(self, dato):
        self.__dato = dato
        self.__izq = None
        self.__der = None

    def getdato(self):
        return self.__dato

    def getIzq(self):
        return self.__izq

    def getDer(self):
        return self.__der

    def setIzq(self, objeto):
        self.__izq = objeto

    def setDer(self, objeto):
        self.__der = objeto

    def setdato(self, objeto):
        self.__dato = objeto


class arbol:
    __cabeza = None

    def __init__(self):
        self.__cabeza = None

    def getcabeza(self):
        return self.__cabeza

    def insertar(self, elemento):
        if self.__cabeza is None:
            nuevo = Nodo(elemento)
            self.__cabeza = nuevo
        else:
            self.insertar_recursivo(self.__cabeza, elemento)

    def insertar_recursivo(self, cab, elemento):
        if cab.getdato() == elemento:
            print(f"Elemento {elemento} ya existente")
        else:
            if elemento < cab.getdato():
                if cab.getIzq() is None:
                    nuevo = Nodo(elemento)
                    cab.setIzq(nuevo)
                else:
                    self.insertar_recursivo(cab.getIzq(), elemento)
            else:
                if elemento > cab.getdato():
                    if cab.getDer() is None:
                        nuevo = Nodo(elemento)
                        cab.setDer(nuevo)
                    else:
                        self.insertar_recursivo(cab.getDer(), elemento)

    def suprimir(self, elemento):
        if self.__cabeza is None:
            print('El arbol esta vacio.')
        else:
            self.__cabeza = self.suprimir_recursivo(self.__cabeza, elemento)

    def suprimir_recursivo(self, nodo, elemento):
        if nodo is None:
            print(f'El valor {elemento} no existe en el árbol')
            return None

        if elemento < nodo.getdato():
            nodo.setIzq(self.suprimir_recursivo(nodo.getIzq(), elemento))
        elif elemento > nodo.getdato():
            nodo.setDer(self.suprimir_recursivo(nodo.getDer(), elemento))
        else:
            if nodo.getIzq() is None and nodo.getDer() is None:
                return None  # El nodo actual es una hoja, simplemente lo eliminamos
            elif nodo.getIzq() is None:
                return nodo.getDer()  # El nodo actual solo tiene un hijo a la derecha
            elif nodo.getDer() is None:
                return nodo.getIzq()  # El nodo actual solo tiene un hijo a la izquierda
            else:
                # El nodo actual tiene dos hijos, encontramos el máximo en el subárbol izquierdo
                max_izquierdo = self.maximo(nodo.getIzq())
                nodo.setdato(max_izquierdo.getdato())
                nodo.setIzq(self.suprimir_recursivo(nodo.getIzq(), max_izquierdo.getdato()))

        return nodo

    def maximo(self, nodo):
        while nodo.getDer() is not None:
            nodo = nodo.getDer()
        return nodo

    def bucar_recursivo(self, nodo, elemento):

        if nodo is None:
            return None
        if nodo.getdato() == elemento:
            return nodo
        elif elemento < nodo.getdato():
            return self.bucar_recursivo(nodo.getIzq(), elemento)
        else:
            return self.bucar_recursivo(nodo.getDer(), elemento)

    def nivel(self, nodo, elemento, nivel_actual):
        if nodo is None:
            print('Arbol vacio')
        else:
            if nodo.getdato() == elemento:
                print(f'El NIVEL de {elemento} es {nivel_actual}')
            elif elemento < nodo.getdato():
                self.nivel(nodo.getIzq(), elemento, nivel_actual+1)
            elif elemento > nodo.getdato():
                self.nivel(nodo.getDer(), elemento, nivel_actual + 1)

    def hoja(self, nodo, elemento):
        if nodo is None:
            return False
        if nodo.getdato() == elemento and nodo.getIzq() is None and nodo.getDer() is None:
            return True
        return self.hoja(nodo.getIzq(), elemento) or self.hoja(nodo.getDer(), elemento)

    def padre(self, nodo, z, x):
        if nodo is None:
            return False
        if nodo.getdato() == z:
            return nodo.getIzq() and nodo.getIzq().getdato() == x or nodo.getDer() and nodo.getDer().getdato() == x
        padre_izq = self.padre(nodo.getIzq(), z, x)
        padre_der = self.padre(nodo.getDer(), z, x)

        return padre_izq or padre_der

    def hijo(self, nodo, x, z):
        if nodo is None:
            return False
        if nodo.getdato() == x:
            return (nodo.getIzq() and nodo.getIzq().getdato() == z) or (nodo.getDer() and nodo.getDer().getdato() == z)
        izquierda = self.hijo(nodo.getIzq(), x, z)
        derecha = self.hijo(nodo.getDer(), x, z)

        return izquierda or derecha

    def altura(self, nodo):
        if nodo is None:
            return 0
        izq = self.altura(nodo.getIzq())
        der = self.altura(nodo.getDer())
        return max(izq, der) + 1

    def camino(self, inicio_valor, final_valor):
        camino = self.encontrarcamino(self.__cabeza, "", inicio_valor, final_valor)
        return camino

    def encontrarcamino(self, nodo, camino_actual, inicio_valor, final_valor):
        if nodo is None:
            return None

        if camino_actual != '':
            camino_actual += '-'
        # Agregar el valor del nodo actual al camino
        camino_actual += str(nodo.getdato())

        if nodo.getdato() == final_valor:
            return camino_actual

        # Buscar en el subárbol izquierdo
        izquierda = self.encontrarcamino(nodo.getIzq(), camino_actual, inicio_valor, final_valor)
        if izquierda:
            return izquierda

        # Buscar en el subárbol derecho
        derecha = self.encontrarcamino(nodo.getDer(), camino_actual, inicio_valor, final_valor)
        return derecha

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.getIzq())
            print(nodo.getdato())
            self.inorden(nodo.getDer())

    def preorden(self, nodo):
        if nodo:
            print(nodo.getdato())
            self.preorden(nodo.getIzq())
            self.preorden(nodo.getDer())

    def posorden(self, nodo):
        if nodo:
            self.posorden(nodo.getIzq())
            self.posorden(nodo.getDer())
            print(nodo.getdato())

    def frontera(self, nodo, frontera):
        if nodo:
            if nodo.getIzq() is None and nodo.getDer() is None:
                frontera.append(nodo.getdato())

            self.frontera(nodo.getIzq(), frontera)
            self.frontera(nodo.getDer(), frontera)
        return frontera

    def Padre_Hermano(self, valor):
        if self.__cabeza is None:
            return None

        padre, hermano = self.encontrar_padre_hermano(self.__cabeza, valor)

        if padre is not None:
            print(f'El padre de {valor} es: {padre.getdato()}')
            if hermano is not None:
                print(f'El hermano de {valor} es: {hermano.getdato()}')
            else:
                print(f"No hay hermano de {valor}.")
        else:
            print(f'No se encontro el valor {valor} en el arbol')

    def encontrar_padre_hermano(self, nodo, valor):
        if nodo is None:
            return None, None

        if nodo.getIzq() and nodo.getIzq().getdato() == valor:
            derecha_hermano = nodo.getDer()
            return nodo, derecha_hermano
        if nodo.getDer() and nodo.getDer().getdato() == valor:
            izquierda_hermano = nodo.getIzq()
            return nodo, izquierda_hermano

        izquierda_padre, izquierda_hermano = self.encontrar_padre_hermano(nodo.getIzq(), valor)
        if izquierda_padre is not None:
            return izquierda_padre, izquierda_hermano

        derecha_padre, derecha_hermano = self.encontrar_padre_hermano(nodo.getDer(), valor)
        if derecha_padre is not None:
            return derecha_padre, derecha_hermano

        return None, None

    def contar_recursivamente(self, nodo):
        if nodo is None:
            return 0
        else:
            nodos_izq = self.contar_recursivamente(nodo.getIzq())
            nodos_der = self.contar_recursivamente(nodo.getDer())
            return 1 + nodos_izq + nodos_der

    def sucesores(self, valor):
        nodo = self.bucar_recursivo(self.__cabeza, valor)
        if nodo:
            sucesores = []
            self.encontrarsucesores(nodo, sucesores)
            sucesores_excluyendo_actual = []

            # Iteramos sobre la lista de sucesores y excluimos el nodo actual
            for sucesor in sucesores:
                if sucesor != nodo.getdato():
                    sucesores_excluyendo_actual.append(sucesor)

            return sucesores_excluyendo_actual

        else:
            print('Nodo no encontrado.')
        return []

    def encontrarsucesores(self, nodo, sucesores):
        if nodo:
            sucesores.append(nodo.getdato())
            self.encontrarsucesores(nodo.getIzq(), sucesores)
            self.encontrarsucesores(nodo.getDer(), sucesores)

if __name__ == "__main__":
    a = arbol()
    a.insertar(19)
    a.insertar(5)
    a.insertar(15)
    a.insertar(3)
    a.insertar(20)
    a.insertar(9)

    print("Árbol antes de la supresión:")
    a.inorden(a.getcabeza())
    a.suprimir(3)
    print('Árbol después de la supresión:')
    a.inorden(a.getcabeza())  # se pasa la cabeza actualizada
    encontrado = a.bucar_recursivo(a.getcabeza(), 5)
    print(f'buscar: {encontrado}')
    a.nivel(a.getcabeza(), 15, 1)
    print('Hoja:', a.hoja(a.getcabeza(), 9))
    print('Padre: ', a.padre(a.getcabeza(), 19, 5))
    print('Hijo: ', a.hijo(a.getcabeza(), 19, 5))
    camino = a.camino(19, 9)
    print('Camino: ', camino)
    print('Altura: ', a.altura(a.getcabeza()))
    print('---INORDEN---')
    a.inorden(a.getcabeza())
    print('---PREORDEN---')
    a.preorden(a.getcabeza())
    print('---POSORDEN---')
    a.posorden(a.getcabeza())
    a.insertar(15)
    #       19
    #      /  \
    #     5    20
    #    / \
    #   3   15
    #       /
    #      9
