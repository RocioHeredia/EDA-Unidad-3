import csv
from Designacion import designacion
from ListaEnalazadaPorContenido import ListaEnlazadaPorContenido

def contar_mujeres_por_anio_dado_un_cargo(lista):
    cargo_buscar = input('Ingrese Cargo para contar Mujeres: ')
    actual = lista.Primer_elemento()
    total_mujeres = 0
    anio_actual = actual.getdato().getanio()
    while actual is not None:
        anio = actual.getdato().getanio()
        if anio != anio_actual:
            if anio_actual is not None:
                print(f'Año: {anio_actual} Total de Mujeres: {total_mujeres}')
            anio_actual = anio
            total_mujeres = 0
        if actual.getdato().getcargo() == cargo_buscar:
            total_mujeres += actual.getdato().getmujeres()
        actual = actual.getsiguiente()
    if anio_actual is not None and total_mujeres > 0:
        print(f'Año: {anio_actual} Total de Mujeres: {total_mujeres}')
def contar_agentes_materia_cargo_anio(lista):
    cargo_buscar = input('Ingrese Cargo: ')
    materia = input('Ingrese Materia: ')
    anio = int(input('Ingrese año: '))
    actual = lista.Primer_elemento()
    agentes = 0
    while actual is not None:
        if actual.getdato().getcargo() == cargo_buscar and int(actual.getdato().getanio()) == anio and actual.getdato().getmateria() == materia:
            agentes += (actual.getdato().getmujeres() + actual.getdato().getvarones())
        actual = actual.getsiguiente()
    print(f'Total de Agentes: {agentes}')


if __name__ == '__main__':
    archivo = open('designacion.csv', encoding='utf-8-sig')
    reader = csv.reader(archivo, delimiter=',')
    principio = True
    mi_lista_designaciones = ListaEnlazadaPorContenido()

    for fila in reader:
        if principio:
            principio = False
        else:
            if fila[3]:
                mi_lista_designaciones.Insertar(
                    designacion(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5])))
            else:
                mi_lista_designaciones.Insertar(
                    designacion(int(fila[0]), fila[1], fila[2], 'sin datos', int(fila[4]), int(fila[5])))

    contar_mujeres_por_anio_dado_un_cargo(mi_lista_designaciones)
    contar_agentes_materia_cargo_anio(mi_lista_designaciones)

