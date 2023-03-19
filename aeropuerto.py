from vuelo import Vuelo
import json

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

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [vuelo.to_dict() for vuelo in self.__vuelos]
                print(lista)
                json.dump(lista, archivo, indent=4)
                return 1
        except:
            return 0
        
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__vuelos = [Vuelo(**vuelo) for vuelo in lista]
                return 1
        except:
            return 0

    def __str__(self) -> str:
        return "".join(
            str(v) + "\n" for v in self.__vuelos
        )
    
