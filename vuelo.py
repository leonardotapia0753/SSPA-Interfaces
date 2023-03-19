class Vuelo:
    def __init__(self, id = "", origen = "", destino = "", peso = 0):
        self.__id = id
        self.__origen = origen
        self.__destino = destino
        self.__peso = peso

    def __str__(self):
        return(
            "Identificador: " + self.__id + "\n" +
            "Origen: " + self.__origen + "\n" +
            "Destino: " + self.__destino + "\n" +
            "Peso: " + str(self.__peso) + "\n"
        )
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origen": self.__origen,
            "destino": self.__destino,
            "peso": self.__peso
        }
