import numpy as np
class nodo:
    __dato = int
    __enlace = int

    def __init__(self, dato):
        self.__dato = dato
        self.__enlace = -1

    def getdato(self):
        return self.__dato

    def getenlace(self):
        return self.__enlace

    def setdato(self, dato):
        self.__dato = dato

    def setenlace(self, sig):
        self.__enlace = sig

# Clase para representar la lista enlazada mediante cursores
class ListaEnlazada:
    __cantidad = int
    __arreglo = []
    __libre = int
    __cabeza = int

    def __init__(self, cantidad):
        self.__cantidad = int(cantidad)
        self.__arreglo = np.empty(cantidad, dtype=nodo)  # arreglo de nodos
        self.__cabeza = -1  # Puntero al primer elemento de la lista
        self.__libre = 0

    def insertar(self, dato):
        nuevo_nodo = nodo(dato)

        if self.__libre >= self.__cantidad:
            print("La lista está llena")
            return

        libre = self.__libre
        self.__arreglo[libre] = nuevo_nodo
        self.__libre += 1

        if self.__cabeza == -1:
            self.__cabeza = libre
        else:
            actual = self.__cabeza
            while self.__arreglo[actual].getenlace() != -1:
                actual = self.__arreglo[actual].getenlace()
            self.__arreglo[actual].setenlace(libre)

    def eliminar(self, dato):
        if self.__cabeza == -1:
            print("La lista está vacía")
            return

        actual = self.__cabeza
        anterior = -1

        # Buscar el nodo a eliminar y mantener el índice del nodo anterior
        while actual != -1 and self.__arreglo[actual].getdato() != dato:
            anterior = actual
            actual = self.__arreglo[actual].getenlace()

        if actual == -1:
            return print("El dato no está en la lista")

        # Si el nodo a eliminar es el primero
        if anterior == -1:
            self.__cabeza = self.__arreglo[actual].getenlace()
        else:
            # Enlazar el nodo anterior al nodo siguiente al que se va a eliminar
            self.__arreglo[anterior].setenlace(self.__arreglo[actual].getenlace())

        # Marcar el nodo como disponible para futuras inserciones
        self.__arreglo[actual] = None


    def recorrer(self):
        if self.__cabeza == -1:
            print("La lista está vacía")
            return

        actual = self.__cabeza
        while actual != -1:
            print(self.__arreglo[actual].getdato())
            actual = self.__arreglo[actual].getenlace()

    def buscar(self, dato):
        if self.__cabeza == -1:
            print("La lista está vacía")
            return None
        actual = self.__cabeza
        while self.__arreglo[actual].getdato() != dato:
            actual = self.__arreglo[actual].getenlace()
        return actual

    def recuperar(self, p):
        if p >= len(self.__arreglo) or p < 0:
            print('Posición fuera de rango')
            return
        if self.__arreglo[p] is None:
            return None
        return self.__arreglo[p].getdato()

    def primer_elemento(self):
        if self.__cabeza == -1:
            return print('Lista vacia')
        return self.__arreglo[self.__cabeza].getdato()

    def ultimo_elemento(self):
        if self.__cabeza == -1:
            return print('Lista vacia')
        actual = self.__cabeza
        while self.__arreglo[actual].getenlace() != -1:
            actual = self.__arreglo[actual].getenlace()
        return self.__arreglo[actual].getdato()

    def siguiente(self, p):
        if p >= len(self.__arreglo) or p < 0:
            print("Índice fuera de rango")
            return None
        if self.__arreglo[p] is None:
            print("El nodo en este índice está vacío")
            return None
        enlace = self.__arreglo[p].getenlace()
        if enlace == -1:
            print("No hay siguiente nodo")
            return None
        siguiente = self.__arreglo[enlace].getdato()
        return siguiente



    def anterior(self, p):
        if p >= len(self.__arreglo) or p < 0:
            print("Índice fuera de rango")
            return None
        if self.__arreglo[p] is None:
            print("El nodo en este índice está vacío")
            return None
        if p == self.__cabeza:
            print("El nodo es el primero, no tiene anterior")
            return None
        actual = self.__cabeza
        anterior = actual
        while self.__arreglo[actual].getenlace() != p:
            anterior = actual
            actual = self.__arreglo[actual].getenlace()
        return self.__arreglo[anterior].getdato()
# Uso
lista = ListaEnlazada(5)
lista.insertar(3)
lista.insertar(5)
lista.insertar(7)
lista.insertar(9)
lista.recorrer()

print('se encontro el dato 7 en la posicion:', lista.buscar(7))
print('Recuperacion de la posición 2: ', lista.recuperar(2))
print('Primer elemento: ', lista.primer_elemento())
print('Ultimo elemento: ', lista.ultimo_elemento())
print('Siguiente de 5: ', lista.siguiente(1))
print('Anterior de 5: ', lista.anterior(1))

print("Recuperar elemento del cursor:", mi_lista.Recuperar())
mi_lista.Avanzar()
print("Recuperar elemento después de avanzar:", mi_lista.Recuperar())
mi_lista.Retroceder()
print("Recuperar elemento después de retroceder:", mi_lista.Recuperar())
'''
