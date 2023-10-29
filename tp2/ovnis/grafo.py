from __future__ import annotations

from typing import Iterator, Any
from grafo_utils import ExeptionGrafo

NOMBRE_FUENTE = 'R'
NOMBRE_SUMIDERO = 'S'

class Grafo:
    __vertices = []
    __aristas = {}

    def __int__(self):
        self.__vertices = []
        self.__aristas = {}

    def __iter__(self) -> Iterator:
        return iter(self.__vertices)

    def __str__(self) -> str:
        linea = ""
        for v in self.__vertices:
            for u in self.__aristas.get(v):
                linea += f"{v} -> {u}. Peso: {self.__aristas[v][u]} \n"
        return linea

    @classmethod
    def desde_archivo(self, nombre_archivo) -> Grafo:
        g = Grafo()
        tiene_fuente = False
        tiene_sumidero = False

        try:
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = linea.split(",", 2)
                    v_origen = datos[0]
                    v_destino = datos[1]
                    capacidad = int(datos[2])

                    if v_origen == NOMBRE_FUENTE and not tiene_fuente:
                        tiene_fuente = True
                    if v_origen == NOMBRE_SUMIDERO:
                        raise ExeptionGrafo("El sumidero no puede tener ejes salientes")

                    if v_destino == NOMBRE_SUMIDERO and not tiene_sumidero:
                        tiene_sumidero = True
                    if v_destino == NOMBRE_FUENTE:
                        raise ExeptionGrafo("La fuente no puede tener ejes entrantes")

                    g.agregar_vertice(v_origen)
                    g.agregar_vertice(v_destino)
                    g.agregar_arista_bidireccional(v_origen, v_destino, capacidad)
        except ExeptionGrafo as e:
            raise e
        except FileNotFoundError as e:
            raise ExeptionGrafo(f"El archivo '{nombre_archivo}' no fue encontrado.")
        except Exception as e:
            raise ExeptionGrafo(f"Ocurrió un error al procesar el archivo: '{nombre_archivo}'. Error: {str(e)}")

        return g

    def agregar_vertice(self, v):
        if not self.__vertices.__contains__(v):
            self.__vertices.append(v)

    def agregar_arista(self, v_origen, v_destino, capacidad):
        if self.__aristas.get(v_origen) is None:
            self.__aristas[v_origen] = { v_destino : capacidad }
        else:
            self.__aristas[v_origen][v_destino] = capacidad

    def agregar_arista_bidireccional(self, v, u, capacidad):
        self.agregar_arista(v, u, capacidad)
        self.agregar_arista(u, v, capacidad)
