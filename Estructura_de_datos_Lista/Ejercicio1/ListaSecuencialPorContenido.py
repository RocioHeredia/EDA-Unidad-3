
import numpy as np

class ListaContenido:
    def __init__(self):
        self.__lista = np.array([])

    def insertar(self, elemento, posicion):
        """
        Inserta el elemento en la posición especificada en la lista.
        """
        if posicion >= 0 and posicion <= len(self.__lista):
            self.__lista = np.insert(self.__lista, posicion, elemento)
        else:
            print("Posición fuera de rango.")

    def suprimir(self, posicion):
        """
        Elimina el elemento en la posición especificada de la lista.
        """
        if posicion >= 0 and posicion < len(self.__lista):
            self.__lista = np.delete(self.__lista, posicion)
        else:
            print("Posición fuera de rango.")

    def recuperar(self, posicion):
        """
        Recupera el elemento en la posición especificada de la lista.
        """
        if posicion >= 0 and posicion < len(self.__lista):
            return self.__lista[posicion]
        else:
            print("Posición fuera de rango.")
            return None

    def buscar(self, elemento):
        """
        Busca el elemento en la lista y devuelve su posición si se encuentra, o -1 si no se encuentra.
        """
        for i, e in enumerate(self.__lista):
            if e == elemento:
                return i
        return -1

    def primer_elemento(self):
        """
        Devuelve el primer elemento de la lista.
        """
        if len(self.__lista) > 0:
            return self.__lista[0]
        else:
            print("La lista está vacía.")
            return None

    def ultimo_elemento(self):
        """
        Devuelve el último elemento de la lista.
        """
        if len(self.__lista) > 0:
            return self.__lista[-1]
        else:
            print("La lista está vacía.")
            return None

    def siguiente(self, posicion):
        """
        Devuelve la posición del elemento siguiente a la posición especificada en la lista.
        """
        if posicion >= 0 and posicion < len(self.__lista) - 1:
            return posicion + 1
        else:
            print("Posición fuera de rango para la posición siguiente.")
            return None

    def anterior(self, posicion):
        """
        Devuelve la posición del elemento anterior a la posición especificada en la lista.
        """
        if posicion > 0 and posicion < len(self.__lista):
            return posicion - 1
        else:
            print("Posición fuera de rango para la posición anterior.")
            return None

    def recorrer(self):
        """
        Imprime todos los elementos de la lista.
        """
        for elemento in self.__lista:
            print(elemento)


'''
# Ejemplo de uso
mi_lista = ListaContenido()

mi_lista.insertar(10, 0)
mi_lista.insertar(20, 1)
mi_lista.insertar(30, 2)

print("Elementos de la lista:")
mi_lista.recorrer()

mi_lista.suprimir(1)
print("Elementos de la lista después de suprimir:")
mi_lista.recorrer()

elemento = mi_lista.recuperar(1)
print(f"Elemento en la posición 1: {elemento}")

posicion = mi_lista.buscar(10)
if posicion != -1:
    print(f"El elemento 10 se encuentra en la posición {posicion}")
else:
    print("El elemento 10 no se encuentra en la lista")

primer_elemento = mi_lista.primer_elemento()
ultimo_elemento = mi_lista.ultimo_elemento()
print(f"Primer elemento: {primer_elemento}, Último elemento: {ultimo_elemento}")

posicion = 0
posicion_siguiente = mi_lista.siguiente(posicion)
posicion_anterior = mi_lista.anterior(posicion)
print(f"Posición actual: {posicion}, Posición siguiente: {posicion_siguiente}, Posición anterior: {posicion_anterior}")'''