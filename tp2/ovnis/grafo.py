from __future__ import annotations

from typing import Iterator
from grafo_utils import ExeptionGrafo

NOMBRE_FUENTE = "R"
NOMBRE_SUMIDERO = "S"


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
            aristas_vertice = self.__aristas.get(v)

            if aristas_vertice is not None:
                for u in aristas_vertice:
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

                    g.agregar_vertice(v_origen)
                    g.agregar_vertice(v_destino)

                    es_fuente_origen = v_origen == NOMBRE_FUENTE
                    es_sumidero_destino = v_destino == NOMBRE_SUMIDERO

                    if es_fuente_origen:
                        tiene_fuente = True
                    elif v_origen == NOMBRE_SUMIDERO:
                        raise ExeptionGrafo("El sumidero no puede tener ejes salientes")

                    if es_sumidero_destino:
                        tiene_sumidero = True
                    elif v_destino == NOMBRE_FUENTE:
                        raise ExeptionGrafo("La fuente no puede tener ejes entrantes")

                    if es_fuente_origen or es_sumidero_destino:
                        g.agregar_arista(v_origen, v_destino, capacidad)
                    else:
                        g.agregar_arista_bidireccional(v_origen, v_destino, capacidad)
        except ExeptionGrafo as e:
            raise e
        except FileNotFoundError as e:
            raise ExeptionGrafo(f"El archivo '{nombre_archivo}' no fue encontrado.")
        except Exception as e:
            raise ExeptionGrafo(
                f"Ocurrió un error al procesar el archivo: '{nombre_archivo}'. Error: {str(e)}"
            )

        if not tiene_fuente:
            raise ExeptionGrafo("No se ha proporcionado nodo Fuente")
        if not tiene_sumidero:
            raise ExeptionGrafo("No se ha proporcionado nodo Sumidero")

        return g

    def agregar_vertice(self, v):
        if not self.__vertices.__contains__(v):
            self.__vertices.append(v)

    def agregar_arista(self, v_origen, v_destino, capacidad):
        if self.__aristas.get(v_origen) is None:
            self.__aristas[v_origen] = {v_destino: capacidad}
        else:
            self.__aristas[v_origen][v_destino] = capacidad

    def agregar_arista_bidireccional(self, v, u, capacidad):
        self.agregar_arista(v, u, capacidad)
        self.agregar_arista(u, v, capacidad)
