from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Estructuras.TablaSimbolos import TablaSimbolos
from Estructuras.Id import Funcion, Variable
import copy
from Estructuras.Contexto import Contexto

class Escucha (compiladoresListener):
    #numTokens = 0
    #numNodos = 0
    oldSimbolos = dict()
    listaVariables = []
    listaParametros = []
    listaArgumentos = []
    helperArgumentos = []
    contadorParametros = 0
    contadorArgumentos = 0
    errores = open("./output/errores.txt", "w")
    flagFuncion = False
    tablaSimbolos = TablaSimbolos()
    
    
    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Comienzo de la compilacion")
        #self.archivo.write('Tabla de simbolos \n')

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        
        #self.archivo.write('Contexto \n')
        
        contextos = self.tablaSimbolos.getContextos()
        
        #for variable in contextos[-1].getSimbolos().values():
         #   self.archivo.write(f'{variable.nombre} : {variable.tipo}\n')
            
            
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        
        #Declaro variables
        if ctx.getChildCount() > 1:
            nombre_var = ctx.getChild(1).getText()
            tipo_dato = ctx.getChild(0).getText()
        else:
            nombre_var = None
            return
        

        #verifica si falta punto y coma
        if ctx.getChild(ctx.getChildCount() - 1).getText() != ';':
            print("Error Sintactico: Falta un punto y coma en la declaracion")
            self.errores.write(f"Error Sintactico: Falta un punto y coma en la declaracion de la variable {nombre_var} \n")

        #Busco si la variable ya fue declarada
        if not(self.tablaSimbolos.buscarLocalID(nombre_var)):
            nuevaVar = Variable(nombre_var, tipo_dato)
        else:
            print(f"Error semantico: Variable {nombre_var} ya declarada")
            return
        
        if ctx.getChild(2) is not None and (str(ctx.getChild(2).getText()) == '='):
            nuevaVar.setInicializado()
        self.tablaSimbolos.agregar(nuevaVar)
        
    
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.agregarContexto()
        for parametros in self.listaParametros:
            id = Variable(parametros['nombre'], parametros['tipo'])
            id.setInicializado()
            self.tablaSimbolos.agregar(id)
    
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.getContextos()
           
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        nombre_var = ctx.getChild(0).getText()


        variable = self.tablaSimbolos.buscarID(nombre_var)

        if variable == False:
            print ('Error Semantico: Variable no declarada, no se puede asignar')
        else:   
            variable.setInicializado()
    
    
    def identify(self, cadena):
        # Intentar convertir a entero
        if cadena.isdigit() or (cadena.startswith('-') and cadena[1:].isdigit()):
            return "int"
    
        # Intentar convertir a flotante
        try:
            float(cadena)
            return "double"
        except ValueError:
            return None  # No es un número

    
                
    def exitFactor(self, ctx: compiladoresParser.FactorContext):
    # Obtener el primer hijo del contexto, que puede ser una variable o función
        primer_hijo = ctx.getChild(0)
        nombre = primer_hijo.getText()
    
    # Caso 1: Si el primer hijo no tiene múltiples hijos, se considera una variable
        if primer_hijo.getChildCount() <= 1:
            tipo = self.identify(nombre)
            var = self.tablaSimbolos.buscarLocalID(nombre)
            # Comprobar si el tipo no es "int" o "double" (es decir, una variable)
            if tipo not in ["int", "double"]:
                helper = {'nombre': nombre, 'tipo': tipo}
                if var is not None:
                    # Verificar si la variable ha sido inicializada
                    if not var.getInicializado():
                        print(f"WARNING  Semantico: La variable {nombre} no está inicializada.\n")
                    # Verificar si estamos en usofuncion o asignando una variable
                    if self.flagFuncion:
                        self.helperArgumentos.append(helper)
                        self.contadorArgumentos += 1
                    else:
                        # Agregar variable a las asignaciones y marcar como accedida
                        self.listaVariables.append({'tipo': var.getTipo(), 'nombre': var.getNombre()})
                    var.setAccedido()
                    self.tablaSimbolos.actualizarId(var)  # Actualizar variable en la tabla de símbolos
                else:
                    print(f"WARNING [Semantico]: La variable {nombre} no está declarada.\n")
                    return
            else:
                helper = {'nombre': nombre, 'tipo': tipo}
                if self.flagFuncion:
                    self.helperArgumentos.append(helper)
                    self.contadorArgumentos += 1
                else:
                    # Si es una constante, agregar a las asignaciones
                    if var is not None:
                        self.listaVariables.append({'tipo': var.getTipo(), 'nombre': var.getNombre()})
        # Caso 2: Si el primer hijo tiene múltiples hijos, se considera una función
        else:
            
            func_nombre = primer_hijo.getChild(0).getText()
            func = self.tablaSimbolos.buscarID(func_nombre)
            if func is not None:
                helper = {'nombre': func_nombre, 'tipo': func.getTipo()}
                if self.flagFuncion:
                    self.helperArgumentos.append({'nombre': func.getNombre(), 'tipo': func.getTipo()})
                    self.contadorArgumentos += 1
                else:
                    self.listaVariables.append(helper)
                # Agregar función a las asignaciones y marcar como accedida
                func.setAccedido()
                self.tablaSimbolos.actualizarId(func)  # Actualizar función en la tabla de símbolos
            else:
                print(f"WARNING [Semantico]: La función {func_nombre} no está declarada.\n")
                return
        
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        if ctx.getChildCount() > 1:
            nombre_param = ctx.getChild(1).getText()
            tipo_param = ctx.getChild(0).getText()
        else:
            nombre_param = None
            tipo_param = None
        if ctx.getChildCount() != 0:
            self.listaParametros.append({'tipo': tipo_param, 'nombre': nombre_param})
            self.contadorParametros = self.contadorParametros + 1
            
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        if ctx.getChildCount() != 0:
            self.listaArgumentos.append(self.helperArgumentos) 
            self.contadorArgumentos = self.contadorArgumentos + 1
        self.helperArgumentos.clear() #Vaciamos la lista helper de argumentos
        
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        nombre_func = ctx.getChild(1).getText()
        tipo_func = ctx.getChild(0).getText()
        if(self.tablaSimbolos.buscarID(nombre_func) is None):
            funcion = Funcion(nombre_func, tipo_func, copy.deepcopy(self.listaParametros))
            self.tablaSimbolos.agregar(funcion)
            self.listaParametros.clear()
            self.listaVariables.clear()
        else:
            print("WARNING [Semantico]: Funcion ya declarada")
    
            
    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        # Verifica si la función está declarada
        funcion = self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        if funcion is None:
            print("WARNING [Semantico]: Funcion no declarada")
            return
    
        # Verificar los argumentos de la función
        self.listaLocalParametros = []
        for arg in self.listaArgumentos:
            for aux in arg:
                if aux['nombre'].isdigit():
                    tipo = self.identify(aux['nombre'])
                    self.listaLocalParametros.append({'nombre': aux['nombre'], 'tipo': tipo})
                else:
                    simbolo = self.tablaSimbolos.buscarID(aux['nombre'])
                    if simbolo is not None:
                        self.listaLocalParametros.append({'nombre': aux['nombre'], 'tipo': simbolo.getTipo()})
                    else:
                        print("WARNING [Semantico]: Argumento no declarado")
                        return

        # Compara los tipos de los parámetros con los argumentos
        parametros_funcion = funcion.getParametros()
        if self.contadorParametros != self.contadorArgumentos:
            print("WARNING [Semantico]: Cantidad de argumentos incorrecta")
            self.contadorParametros = 0
            self.contadorArgumentos = 0
            return
        self.contadorParametros = 0
        self.contadorArgumentos = 0

        for i, parametro in enumerate(parametros_funcion):
            if i < len(self.listaLocalParametros):
                parametro_local = self.listaLocalParametros[i]
                if parametro['tipo'] != parametro_local['tipo']:
                    print(f"WARNING: El argumento {parametro_local['nombre']} es de tipo {parametro_local['tipo']}. "
                        f"Se espera un argumento de tipo {parametro['tipo']}.")

        # Actualiza la función en la tabla de símbolos y marca como accedido el nodo del árbol
            self.tablaSimbolos.actualizarId(funcion)
            funcion.setAccedido()
            self.listaVariables.clear()

    
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        context = self.tablaSimbolos.getContextos()[-1]
        self.oldSimbolos = context.getSimbolos()
        self.tablaSimbolos.agregarContexto()
        for simbolos in self.oldSimbolos.values():
            self.tablaSimbolos.agregar(copy.deepcopy(simbolos))
        
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        
        contexto_actual = self.tablaSimbolos.getContextos()[-1]
        simbolos_actuales = contexto_actual.getSimbolos()

        # Crear conjuntos de nombres de los símbolos actuales y anteriores
        nombres_simbolos_actuales = set(simbolo.getNombre() for simbolo in simbolos_actuales.values())
        nombres_simbolos_anteriores = set(simbolo.getNombre() for simbolo in self.oldSimbolos.values())

        # Identificar nuevos símbolos
        nombres_nuevos_simbolos = nombres_simbolos_actuales - nombres_simbolos_anteriores

        # Imprimir los ID no accedidos y no inicializados
        for nombre_nuevo_simbolo in nombres_nuevos_simbolos:
            simbolo_nuevo = simbolos_actuales.get(nombre_nuevo_simbolo)
            if simbolo_nuevo:
                if not simbolo_nuevo.getAccedido():  
                    print(f"WARNING: La variable {simbolo_nuevo.getNombre()} no ha sido accedida.\n")
                if not simbolo_nuevo.getInicializado():  
                    print(f"WARNING: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada.\n")

        # Borrar el contexto actual
        self.tablaSimbolos.borrarContexto()

        
    def enterIfor(self, ctx:compiladoresParser.IforContext):

        context = self.tablaSimbolos.getContextos()[-1]
        self.oldSimbolos = context.getSimbolos()
        self.tablaSimbolos.agregarContexto()
        for simbolos in self.oldSimbolos.values():
            self.tablaSimbolos.agregar(copy.deepcopy(simbolos))
            
    
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        contexto_actual = self.tablaSimbolos.getContextos()[-1]
        simbolos_actuales = contexto_actual.getSimbolos()

        # Crear conjuntos de nombres de los símbolos actuales y anteriores
        nombres_simbolos_actuales = set(simbolo.getNombre() for simbolo in simbolos_actuales.values())
        nombres_simbolos_anteriores = set(simbolo.getNombre() for simbolo in self.oldSimbolos.values())

        # Identificar nuevos símbolos
        nombres_nuevos_simbolos = nombres_simbolos_actuales - nombres_simbolos_anteriores

        # Imprimir los ID no accedidos y no inicializados
        for nombre_nuevo_simbolo in nombres_nuevos_simbolos:
            simbolo_nuevo = simbolos_actuales.get(nombre_nuevo_simbolo)
            if simbolo_nuevo:
                if not simbolo_nuevo.getAccedido():  
                    print(f"WARNING: La variable {simbolo_nuevo.getNombre()} no ha sido accedida.\n")
                if not simbolo_nuevo.getInicializado():  
                    print(f"WARNING: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada.\n")

        # Borrar el contexto actual
        self.tablaSimbolos.borrarContexto()
    
    def enterIif(self, ctx:compiladoresParser.IifContext):
        
        context = self.tablaSimbolos.getContextos()[-1]
        self.oldSimbolos = context.getSimbolos()
        self.tablaSimbolos.agregarContexto()
        for simbolos in self.oldSimbolos.values():
            self.tablaSimbolos.agregar(copy.deepcopy(simbolos))
      
    def exitIif(self, ctx:compiladoresParser.IifContext):
        contexto_actual = self.tablaSimbolos.getContextos()[-1]
        simbolos_actuales = contexto_actual.getSimbolos()

        # Crear conjuntos de nombres de los símbolos actuales y anteriores
        nombres_simbolos_actuales = set(simbolo.getNombre() for simbolo in simbolos_actuales.values())
        nombres_simbolos_anteriores = set(simbolo.getNombre() for simbolo in self.oldSimbolos.values())

        # Identificar nuevos símbolos
        nombres_nuevos_simbolos = nombres_simbolos_actuales - nombres_simbolos_anteriores

        # Imprimir los ID no accedidos y no inicializados
        for nombre_nuevo_simbolo in nombres_nuevos_simbolos:
            simbolo_nuevo = simbolos_actuales.get(nombre_nuevo_simbolo)
            if simbolo_nuevo:
                if not simbolo_nuevo.getAccedido():  
                    print(f"WARNING: La variable {simbolo_nuevo.getNombre()} no ha sido accedida.\n")
                if not simbolo_nuevo.getInicializado():  
                    print(f"WARNING: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada.\n")

        # Borrar el contexto actual
        self.tablaSimbolos.borrarContexto()
      
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        for simbolosNoAccedidos in self.tablaSimbolos.getContextos()[-1].getSimbolos().values():
            if not simbolosNoAccedidos.getAccedido():
                print(f"WARNING: El simbolo {simbolosNoAccedidos.getNombre()} no ha sido accedido.")
      
    def exitInit(self, ctx: compiladoresParser.InitContext):
        tipo = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()

        def verificarTipoAsignacion(var):
            for aux in self.listaVariables:
                if aux["tipo"] != var.getTipo():
                    print(f"WARNING: La variable {aux['nombre']} es de tipo {aux['tipo']}. Se espera una variable tipo {var.getTipo()}\n")

        if tipo in {"int", "double", "char"}:
            if self.tablaSimbolos.buscarLocalID(nombre) is None:
                var = Variable(nombre, tipo)
                if ctx.getChild(2).getText() == '=':
                    verificarTipoAsignacion(var)
                    var.setInicializado()
                    self.listaVariables.clear()
                    self.tablaSimbolos.agregar(var)
            else:
                print(f"WARNING: Ya existe una variable llamada {nombre}.\n")
        elif nombre == "=":
            var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
            if var is not None:
                verificarTipoAsignacion(var)
                var.setInicializado()
                self.tablaSimbolos.actualizarId(var)
                self.variablesAsignacion.clear()
            else:
                print(f'WARNING: La variable {ctx.getChild(0).getText()} no está declarada.\n')
                self.variablesAsignacion.clear()

        
      
      
      
      # Enter a parse tree produced by compiladoresParser#programa.
    # def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
    #     print('Comienzo de la compilacion')
        

    # # Exit a parse tree produced by compiladoresParser#programa.
    # def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
    #     print('Fin de la compilacion')
    #     print("\tSe encontraron")
    #     print("\tNodos: " + str(self.numNodos))
    #     print("\tTokens: " + str(self.numTokens))
        
    # def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
    #     print("Encontre WHILE")
    #     print("\tCantidad hijos: " + str(ctx.getChildCount()))
    #     print("\tTokens: " + ctx.getText())

    # # Exit a parse tree produced by compiladoresParser#iwhile.
    # def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
    #     print("FIN DEL WHILE")
    #     print("\tCantidad hijos: " + str(ctx.getChildCount()))
    #     print("\tTokens: " + ctx.getText())
    
    # def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
    #     print("### Declaracion")

    # # Exit a parse tree produced by compiladoresParser#declaracion.
    # def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
    #     print("Nombre variable: " + ctx.getChild(1).getText())
    
    # def visitTerminal(self, node: TerminalNode):
    #     #print("-----> Token: " + node.getText())
    #     self.numTokens += 1
    
    # def visitErrorNode(self, node: ErrorNode):
    #     print("-----> Error")
    
    # def enterEveryRule(self, ctx):
    #     self.numNodos += 1
    