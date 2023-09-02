import numpy as np


class ListaSecuencialPorPosicion:
    __lista = None

    def __init__(self):
        self.__lista = np.array([])

    def Insertar(self, elemento, posicion):
        if 0 <= posicion <= len(self.__lista):
            self.__lista = np.insert(self.__lista, posicion, elemento)
        else:
            print("Posición fuera de rango")

    def Suprimir(self, posicion):
        if 0 <= posicion < len(self.__lista):
            self.__lista = np.delete(self.__lista, posicion)
        else:
            print("Posición fuera de rango")

    def Recuperar(self, posicion):
        if 0 <= posicion < len(self.__lista):
            return self.__lista[posicion]
        else:
            print("Posición fuera de rango")
            return None

    def Buscar(self, elemento):
        i=0
        while i < len(self.__lista):
            if self.__lista[i] == elemento:
                return i
            else:
                i += 1
        else:
            return -1

    def Primer_elemento(self):
        if len(self.__lista) > 0:
            return self.__lista[0]
        else:
            return None

    def Ultimo_elemento(self):
        if len(self.__lista) > 0:
            return self.__lista[-1]
        else:
            return None

    def Siguiente(self, posicion):
        if 0 <= posicion < len(self.__lista) - 1:
            return posicion + 1
        else:
            return None

    def Anterior(self, posicion):
        if 0 < posicion < len(self.__lista):
            return posicion - 1
        else:
            return None

    def Recorrer(self):
        return self.__lista


'''# Ejemplo de uso
mi_lista = ListaSecuencialPorPosicion()
mi_lista.Insertar(1, 0)
mi_lista.Insertar(2, 1)
mi_lista.Insertar(3, 2)

print(mi_lista.Recorrer())  # Imprimir la lista: [1, 2, 3]
print(mi_lista.Recuperar(1))  # Recuperar el elemento en la posición 1: 2
print(mi_lista.Buscar(3))  # Buscar el elemento 3: Devuelve la posición 2
print(mi_lista.Siguiente(1))  # Siguiente posición después de 1: 2
print(mi_lista.Anterior(2))  # Posición anterior a 2: 1
'''