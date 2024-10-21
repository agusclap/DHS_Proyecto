from Estructuras.Contexto import Contexto


class TablaSimbolos:
    _instance = None
    _ctx = []

    def __new__(cls):
        if TablaSimbolos._instance is None:
            TablaSimbolos._instance = object.__new__(cls)
            TablaSimbolos._ctx.append(Contexto())
        return (TablaSimbolos._instance)

    def getContextos(self):
        return TablaSimbolos._ctx

    # Cada vez que se ingrese en un bloque, se agrega un contexto a la lista
    def agregarContexto(self):
        TablaSimbolos._ctx.append(Contexto())

    # Cada vez que salimos de un bloque, se elimina el contexto de la lista
    def borrarContexto(self):
        TablaSimbolos._ctx.pop()

    # Agregamos un ID en el ultimo contexto registrado
    # Dentro de la lista de contextos, tomo el ultimo diccionario
    # la entrada es {nombreId, Id}
    def agregar(self, variable):
        TablaSimbolos._ctx[-1].agregarSimbolo(variable)

    def actualizar(self, variable):
        TablaSimbolos.buscar(TablaSimbolos, variable.nombre).agregarSimbolo(variable)

    # Para el ultimo contexto guardado, buscamos por la key, el nombre del ID
    # Si esta en el diccionario, return true, else false

    def buscarLocal(self, nombre):
        if nombre in TablaSimbolos._ctx[-1].geTablaSimbolosimbolos():
            return TablaSimbolos._ctx[-1]
        return False

    # Buscamos la key en cualquiera de los contextos almacenados
    # Recorremos desde el global hacia el ultimo
    def buscar(self, nombre) -> Contexto:
        for context in TablaSimbolos._ctx[::-1]:
            if nombre in context.geTablaSimbolosimbolos():
                return context
        return False