import numpy as np
class cola:
    __primero = int
    __ultimo = int
    __cantidad = 0
    __maximo = int
    __arreglo = []

    def __init__(self, cantidad):
        self.__primero = 0
        self.__ultimo = 0
        self.__cantidad = 0
        self.__maximo = cantidad
        self.__arreglo = np.empty(cantidad)

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, elemento):

        if self.__cantidad < self.__maximo:
            self.__arreglo[self.__ultimo] = elemento
            self.__ultimo = (self.__ultimo + 1) % self.__maximo
            self.__cantidad += 1
            return elemento
        else:
            return 0

    def suprimir(self):
        if self.vacia():
            print('Cola Vacia')
            return 0
        else:
            elemento = self.__arreglo[self.__primero]
            self.__primero = (self.__primero + 1) % self.__maximo
            self.__cantidad -= 1
            return elemento

    def mostrar(self):
        if not self.vacia():
            i = self.__primero
            j=0
            for j in range(self.__cantidad):
                print(self.__arreglo[i])
                i = (i+1) % self.__maximo



if __name__ == '__main__':
    cola = cola(5)
    cola.insertar(2)
    cola.insertar(4)
    cola.insertar(6)
    cola.insertar(7)
    cola.insertar(9)
    print('Antes de suprimir')
    cola.mostrar()
    cola.suprimir()
    print('Despues de suprimir')
    cola.mostrar()