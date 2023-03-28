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
    
    @property
    def id(self):
        return self.__id
    
    @property
    def origen(self):
        return self.__origen
    
    @property
    def destino(self):
        return self.__destino
    
    @property
    def peso(self):
        return self.__peso
