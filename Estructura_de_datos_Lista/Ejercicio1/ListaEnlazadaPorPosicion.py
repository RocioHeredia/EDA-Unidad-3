
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

    def Insertar(self, dato, posicion):
        if posicion - 1 < 0:
            print("Posición inválida")
            return
        nuevo_nodo = Nodo(dato)
        if posicion - 1 == 0:
            nuevo_nodo.setsiguiente(self.__primero)
            self.__primero = nuevo_nodo
        else:
            actual = self.__primero
            posicion_actual = 0
            while actual is not None and posicion_actual < posicion -1:
                anterior = actual
                actual = actual.getsiguiente()
                posicion_actual += 1
            anterior.setsiguiente(nuevo_nodo)
            nuevo_nodo.setsiguiente(actual)

    def Suprimir(self, posicion):
        if posicion - 1 == 0:
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
        while actual is not None and contador < posicion-1:
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


    def Ultimo_elemento(self):
        if self.__primero is None:
            return None
        actual = self.__primero
        while actual.getsiguiente() is not None:
            actual = actual.getsiguiente()
        return actual.getdato()

    def Siguiente(self, posicion):
        actual = self.__primero
        contador = 0
        while actual is not None and contador < posicion-1:
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


# Ejemplo de uso
mi_lista = ListaEncadenadaPorPosicion()
mi_lista.Insertar(1, 1)
mi_lista.Insertar(2, 4)
mi_lista.Insertar(3, 2)
mi_lista.Insertar(4, 3)
print(mi_lista.Recorrer())  # Imprimir la lista: [1, 2, 3]
print('Recuperar posición 2:', mi_lista.Recuperar(2))  # Recuperar el elemento en la posición 2: 4
print('Buscar elemento 3:', mi_lista.Buscar(3))  # Buscar el elemento 3: Devuelve la posición 2
print('Siguiente posición después de 1:', mi_lista.Siguiente(1))  # Siguiente posición después de 1: 2
print('Posición anterior a 2:', mi_lista.Anterior(2))  # Posición anterior a 2: 1
