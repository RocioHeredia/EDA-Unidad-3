class designacion:
    __anio = ''
    __cargo_tipo = ''
    __instancia_tipo = ''
    __materia = ''
    __cantidad_varones = int
    __cantidad_mujeres = int

    def __init__(self, anio, cargo, instancia, materia, varones, mujeres):
        self.__anio = anio
        self.__cargo_tipo = cargo
        self.__instancia_tipo = instancia
        self.__materia = materia
        self.__cantidad_varones = varones
        self.__cantidad_mujeres = mujeres

    def __str__(self):
        return f'Año:{self.__anio}, Cargo:{self.__cargo_tipo}, Instancia:{self.__instancia_tipo}, Materia:{self.__materia}, Varones:{self.__cantidad_varones}, Mujeres:{self.__cantidad_mujeres}'

    def getanio(self):
        return self.__anio

    def getcargo(self):
        return self.__cargo_tipo

    def getmateria(self):
        return self.__materia

    def getinstancia(self):
        return self.__instancia_tipo

    def getvarones(self):
        return self.__cantidad_varones

    def getmujeres(self):
        return self.__cantidad_mujeres
