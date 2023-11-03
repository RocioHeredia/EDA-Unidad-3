class grafo_encadenado:
    __lista_adyacencia = {}

    def __init__(self):
        self.__lista_adyacencia = {}

    def imprime_grafo(self):
        print(str(self.__lista_adyacencia))

    def agregar_vertice(self, vertice):
        if vertice not in self.__lista_adyacencia:
            self.__lista_adyacencia[vertice] = []


    def agregar_arista(self, i, j):
        if i in self.__lista_adyacencia and j in self.__lista_adyacencia:
            self.__lista_adyacencia[i].append(j)
            self.__lista_adyacencia[j].append(i)
        else:
            print(f'No se puede cargar la entrada ({i}, {j})')

    def cargar_grafo(self, entradas):
        for e in entradas:
            i, j = e
            self.agregar_vertice(i)
            self.agregar_vertice(j)
            if j not in self.__lista_adyacencia[i]:
                self.agregar_arista(i, j)

    def adyacentes(self, u):
        if u in self.__lista_adyacencia:
            return self.__lista_adyacencia[u]

    def camino(self, i, j, visitados, camino):
        visitados.add(i)
        camino.append(i)

        if i == j:
            return camino
        else:
            if i in self.__lista_adyacencia:
                for u in self.__lista_adyacencia[i]:
                    if u not in visitados:
                        resultado = self.camino(u, j, visitados, camino)
                        if resultado is not None:
                            return resultado
        # Si no encontramos un camino removemos los ultimos vertices ingresados
        camino.pop()
        visitados.remove(i)
        return

    def conexo(self):
        visitados = set()
        a = 0
        while a < len(self.__lista_adyacencia):
            for v in self.__lista_adyacencia:
                visitados.add(v)
                print(v)
                for u in self.__lista_adyacencia[v]:
                    visitados.add(u)
                    print(u)
                a += 1
        if a == len(self.__lista_adyacencia):
            return True
        else:
            return False




if __name__ == '__main__':
    g = grafo_encadenado()
    e = [(1, 2), (1, 4), (2, 5), (3, 5), (4, 5)]
    g.cargar_grafo(e)
    print('---------')
    u = int(input('Ingrese vertice para ver sus adyacentes: '))
    print(f'Los adyacentes de {u} son: ', g.adyacentes(u))
    print('---------')
    camino = g.camino(1, 5, set(), [])
    if camino:
        print('El camino de 1 a 5 es: ',camino)
    else:
        print('No hay camino 1 a 5 ')
    print('---------')
    print('Conexo:', g.conexo())
    g.imprime_grafo()