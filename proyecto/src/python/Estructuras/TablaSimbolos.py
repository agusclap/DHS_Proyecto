from Estructuras.Contexto import Contexto
from Estructuras.Id import Funcion


class TablaSimbolos:

    def __init__(self):
        self.listaSimbolos = []
        self.listaSimbolos.append(Contexto())
        #return (TablaSimbolos._instance)

    def getContextos(self):
        return self.listaSimbolos

    # Cada vez que se ingrese en un bloque, se agrega un contexto a la lista
    def agregarContexto(self):
        self.listaSimbolos.append(Contexto())

    # Cada vez que salimos de un bloque, se elimina el contexto de la lista
    def borrarContexto(self):
        return self.listaSimbolos.pop()

    # Agregamos un ID en el ultimo contexto registrado
    # Dentro de la lista de contextos, tomo el ultimo diccionario
    # la entrada es {nombreId, Id}
    def agregar(self, variable):
        
        if isinstance(variable, Funcion):
            self.listaSimbolos[0].agregarSimbolo(variable)
        else:
            self.listaSimbolos[-1].agregarSimbolo(variable)
        return variable


    # Para el ultimo contexto guardado, buscamos por la key, el nombre del ID
    # Si esta en el diccionario, return true, else false


    def buscarLocalID(self, id):
        return self.listaSimbolos[-1].getSimbolos().get(id)

    
    
    def buscarID(self, id):
        for cont in reversed(self.listaSimbolos): 
            simbolo = cont.getSimbolos().get(id)
            if simbolo is not None:
                return simbolo
        return None

    def actualizarId(self,id):
        if isinstance(id, Funcion):
            if id.nombre in self.listaSimbolos[0].getSimbolos():
                self.listaSimbolos[0].eliminarSimbolo(id.nombre)
                self.listaSimbolos[0].agregarSimbolo(id)
                return id
            else:
                print(f"WARNING: El identificador de la funcion '{id.nombre}' no existe en el contexto global.")
        else:
            for cont in reversed(self.listaSimbolos):
                if id.nombre in cont.getSimbolos():
                    cont.eliminarSimbolo(id.nombre)
                    cont.agregarSimbolo(id)
                    return id
                else:
                    print(f"WARNING: El identificador de la variable '{id.nombre}' no existe en el contexto actual.")
            return None
     