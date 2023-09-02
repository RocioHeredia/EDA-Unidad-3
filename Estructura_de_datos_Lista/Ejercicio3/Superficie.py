class superficie:
    __provincia = ''
    __superficie = ''

    def __init__(self, provincia, superficie):
        self.__provincia = provincia
        self.__superficie = superficie

    def __str__(self):
        return f'Provincia: {self.__provincia}, Superficie: {self.__superficie}'

    def __lt__(self, other):
        return self.__superficie < other.__superficie
