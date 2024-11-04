class Contexto:
    
    def __init__(self):
        self.simbolos = dict()
        
    def agregarSimbolo(self, variable):
        self.simbolos[variable.nombre] = variable
        
    def getSimbolos(self):
        return self.simbolos
    
    def eliminarSimbolo(self, nombre):
        return self.simbolos.pop(nombre)
