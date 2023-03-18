from vuelo import Vuelo

class Aeropuerto:
    def __init__(self):
        self.__vuelos = []

    def agregar_final(self, vuelo:Vuelo):
        self.__vuelos.append(vuelo)

    def agregar_inicio(self, vuelo:Vuelo):
        self.__vuelos.insert(0,vuelo)

    def mostrar(self):
        for v in self.__vuelos:
            print(v)

    def __str__(self) -> str:
        return "".join(
            str(v) + "\n" for v in self.__vuelos
        )
    
