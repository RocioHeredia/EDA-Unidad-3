import numpy as np


class pila:
    __tope = 0
    __cantidad = 0
    __arre = None

    def __init__(self, cantidad):
        self.__tope = -1
        self.__cantidad = int(cantidad)
        self.__arre = np.empty(cantidad)

    def pila_vacia(self):
        return self.__tope == -1

    def pila_llena(self):
        return self.__tope == self.__cantidad - 1

    def insertar(self, dato):
        if self.pila_llena():
            print('La pila esta llena. No se puede añadir mas contenido')
        else:
            self.__tope += 1
            self.__arre[self.__tope] = dato

    def suprimir(self):
        if self.pila_vacia():
            print('La pila esta vacia.')
        else:
            dato = self.__arre[self.__tope]
            self.__arre[self.__tope] = None
            self.__tope -= 1
            return dato

    def mostrar(self):
        print('Contenido de la pila: ')
        for i in range(self.__tope, -1, -1):
            print(self.__arre[i])


if __name__ == '__main__':
    pila = pila(3)
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(4)
    pila.mostrar()

