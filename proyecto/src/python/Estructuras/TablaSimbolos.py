from Estructuras.Contexto import Contexto


class TablaSimbolos:
    #_instance = None
    #_ctx = []

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
        self.listaSimbolos.pop()

    # Agregamos un ID en el ultimo contexto registrado
    # Dentro de la lista de contextos, tomo el ultimo diccionario
    # la entrada es {nombreId, Id}
    def agregar(self, variable):
        existe = self.buscarLocal(variable.nombre)
        if existe:
            raise ValueError(f"El identificador '{variable.nombre}' ya existe en el contexto actual.")
        else:
            self.listaSimbolos[-1].agregarSimbolo(variable)
        return variable

    def actualizar(self, variable):
        self.listaSimbolos.buscar(TablaSimbolos, variable.nombre).agregarSimbolo(variable)

    # Para el ultimo contexto guardado, buscamos por la key, el nombre del ID
    # Si esta en el diccionario, return true, else false

    def buscarLocal(self, nombre):
        if nombre in self.listaSimbolos[-1].getSimbolos():
            return TablaSimbolos._ctx[-1]
        return None

    def buscarLocalID(self, id):
        return self.listaSimbolos[-1].getSimbolos().get(id)

    # Buscamos la key en cualquiera de los contextos almacenados
    # Recorremos desde el global hacia el ultimo
    def buscar(self, nombre) -> Contexto:
        for context in self.listaSimbolos:
            if nombre in context.getSimbolos():
                return context
        return False
    
    def buscarID(self, id):
        for cont in self.listaSimbolos:
            simbolo = cont.getSimbolos().get(id)
            if simbolo is not None:
                return simbolo
        return None

    def actualizarFuncion(self,id):
        if id.nombre in self.listaSimbolos[0].getSimbolos():
            self.listaSimbolos[0].eliminarSimbolo(id.nombre)
            self.listaSimbolos[0].agregarSimbolo(id)
        else:
            #raise ValueError(f"El identificador '{id.nombre}' no existe en el contexto global.")
            print(f"El identificador '{id.nombre}' no existe en el contexto global.")
        
    def actualizarId(self, id):
        if id.nombre in self.listaSimbolos[-1].getSimbolos():
            self.listaSimbolos[-1].eliminarSimbolo(id.nombre)
            self.listaSimbolos[-1].agregarSimbolo(id)
        else:
            raise ValueError(f"El identificador '{id.nombre}' no existe en el contexto actual.")