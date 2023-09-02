class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getdato(self):
        return self.__dato

    def setsiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getsiguiente(self):
        return self.__siguiente

class ListaEncadenadaPorPosicion:
    def __init__(self):
        self.__primero = None

    def Insertar(self, elemento, posicion):
        nuevo_nodo = Nodo(elemento)
        if posicion == 0:
            nuevo_nodo.setsiguiente(self.__primero)
            self.__primero = nuevo_nodo
        else:
            actual = self.__primero
            contador = 0
            while actual is not None and contador < posicion - 1:
                actual = actual.getsiguiente()
                contador += 1
            if actual is not None:
                nuevo_nodo.setsiguiente(actual.getsiguiente())
                actual.setsiguiente(nuevo_nodo)
            else:
                print("Posición fuera de rango")

    def Suprimir(self, posicion):
        if posicion == 0:
            if self.__primero is not None:
                self.__primero = self.__primero.getsiguiente()
            else:
                print("La lista está vacía")
        else:
            actual = self.__primero
            contador = 0
            while actual is not None and contador < posicion - 1:
                actual = actual.getsiguiente()
                contador += 1
            if actual is not None and actual.getsiguiente() is not None:
                actual.setsiguiente(actual.getsiguiente())
            else:
                print("Posición fuera de rango")

    def Recuperar(self, posicion):
        actual = self.__primero
        contador = 0
        while actual is not None and contador < posicion:
            actual = actual.getsiguiente()
            contador += 1
        if actual is not None:
            return actual.getdato()
        else:
            print("Posición fuera de rango")
            return None

    def Buscar(self, elemento):
        actual = self.__primero
        contador = 0
        while actual is not None:
            if actual.getdato() == elemento:
                return contador
            actual = actual.getsiguiente()
            contador += 1
        return -1

    def Primer_elemento(self):
        if self.__primero is not None:
            return self.__primero.getdato()
        else:
            return None

    def Ultimo_elemento(self):
        if self.__primero is None:
            return None
        actual = self.__primero
        while actual.siguiente is not None:
            actual = actual.getsiguiente()
        return actual.getdato()

    def Siguiente(self, posicion):
        actual = self.__primero
        contador = 0
        while actual is not None and contador < posicion:
            actual = actual.getsiguiente()
            contador += 1
        if actual is not None and actual.getsiguiente() is not None:
            return posicion + 1
        else:
            return None

    def Anterior(self, posicion):
        if posicion <= 0:
            return None
        actual = self.__primero
        contador = 0
        while actual is not None and contador < posicion - 1:
            actual = actual.getsiguiente()
            contador += 1
        if actual is not None:
            return posicion - 1
        else:
            return None

    def Recorrer(self):

        actual = self.__primero
        while actual is not None:
            print(actual.getdato())
            actual = actual.getsiguiente()

'''
# Ejemplo de uso
mi_lista = ListaEncadenadaPorPosicion()
mi_lista.Insertar(1, 0)
mi_lista.Insertar(2, 1)
mi_lista.Insertar(3, 2)
print(mi_lista.Recorrer())  # Imprimir la lista: [1, 2, 3]
print(mi_lista.Recuperar(1))  # Recuperar el elemento en la posición 1: 2
print(mi_lista.Buscar(3))  # Buscar el elemento 3: Devuelve la posición 2
print(mi_lista.Siguiente(1))  # Siguiente posición después de 1: 2
print(mi_lista.Anterior(2))  # Posición anterior a 2: 1
'''