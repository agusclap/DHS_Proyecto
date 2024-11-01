class Contexto:
    
    def __init__(self):
        self.simbolos = dict()
        
    def agregarSimbolo(self, variable):
        self.simbolos[variable.nombre] = variable
        
    def getSimbolos(self) -> dict:
        return self.simbolos
    
    def eliminarSimbolo(self, nombre):

        if nombre in self.simbolos:

            del self.simbolos[nombre]

        else:

            raise ValueError(f"El identificador '{nombre}' no existe en el contexto.")
