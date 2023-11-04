import numpy as np

class grafoS:
    __arreglo = []
    __vertices = int

    def __init__(self, vertices):
        v = len(vertices)
        self.__vertices = vertices
        self.__arreglo = np.zeros((v, v), dtype=int)

    def imprime_grafo(self):
        print(self.__arreglo)

    def cargar_aristas(self, i, j):

        i = self.__vertices.index(i)
        j = self.__vertices.index(j)
        self.__arreglo[i][j] = 1
        self.__arreglo[j][i] = 1

    def cargar_entradas(self, entradas):
        for e in entradas:
            self.cargar_aristas(e[0], e[1])

    def adyacentes(self, u):
        adyacentes = []
        i = self.__vertices.index(u)
        for c in self.__vertices:
            j = self.__vertices.index(c)
            if self.__arreglo[i][j] == 1:
                adyacentes.append(c)
        return adyacentes

    def listaCamino(self, u):
        camino = []
        i = self.__vertices.index(u)
        for j, valor in enumerate(self.__arreglo[i]):
            if valor == 1:
                camino.append(self.__vertices[j])
        return camino

    def encontrar_camino(self, u, v, visitados, camino):
        visitados.add(u)
        camino.append(u)

        if u == v:
            return camino

        for nodo in self.listaCamino(u):
            if nodo not in visitados:
                resultado = self.encontrar_camino(nodo, v, visitados, camino)
                if resultado:
                    return resultado

        camino.pop()
        return None

    def conexo(self):
        conex = True
        a = 0
        while a < len(self.__vertices) and conex:
            i = 0
            while i < len(self.__vertices) and self.encontrar_camino(self.__vertices[a], self.__vertices[i], set(), []):
                i += 1
            if i < len(self.__vertices) and not self.encontrar_camino(self.__vertices[a], self.__vertices[i], set(),
                                                                      []):
                conex = False
            a += 1
        return conex

    def tiene_ciclo(self, vertice, visitados):
        if vertice in visitados:
            return True
        visitados.add(vertice)
        for vecino in self.adyacentes(vertice):
            if self.tiene_ciclo(vecino, visitados):
                return True
        visitados.remove(vertice)
        return False

    def aciclico(self):
        visitados = set()
        for vertice in self.__vertices:
            if self.tiene_ciclo(vertice, visitados):
                return False  # El grafo tiene un ciclo
        return True  # El grafo es acíclico

    def REA(self, u):
        visitados = set()
        resultado = []

        if u in self.__vertices:
            cola = []
            cola.append(u)
            while cola:
                actual = int(cola.pop(0))
                visitados.add(actual)
                resultado.append(actual)
                for adyacente in self.adyacentes(actual):
                    if adyacente not in visitados:
                        visitados.add(adyacente)
                        cola.append(adyacente)
            return resultado
        else:
            print('El elemento ingresado no se encuentra como vertice')

    def REP(self, u):
        visitados = set()
        resultado = []
        pila = [u]
        while pila:
            vertice = pila.pop()
            if vertice not in visitados:
                visitados.add(vertice)
                resultado.append(vertice)
                for adyacente in self.adyacentes(vertice):
                    if adyacente not in visitados:
                        pila.append(adyacente)

        return resultado


if __name__ == '__main__':
    v = [1, 2, 3, 4, 5]
    e = [(1, 2), (1, 4), (2, 5), (3, 5), (4, 5)]

    g = grafoS(v)
    g.cargar_entradas(e)
    g.imprime_grafo()
    u = int(input('Ingrese el vertice del cual quiere saber los adyacentes: '))
    print(g.adyacentes(u))
    print('--------')
    camino = g.encontrar_camino(1, 5, set(), [])
    if camino:
        print(f"Camino desde {1} a {5}: {camino}")
    else:
        print(f"No hay camino desde {1} a {5}")
    print('Conexo: ', g.conexo())
    print('Aciclico: ', g.aciclico())
    u = int(input('Ingrese vertice por el que quiere empezar a buscar por anchura: '))
    print(g.REA(u))
    print(g.REP(u))
