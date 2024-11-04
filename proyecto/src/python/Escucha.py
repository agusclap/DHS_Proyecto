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
            
            
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        
        #Si la declaracion tiene mas de un hijo, entonces es una declaracion de variable
        if ctx.getChildCount() > 1:
            nombre_var = ctx.getChild(1).getText()
            tipo_dato = ctx.getChild(0).getText()
        else:
            nombre_var = None
            return
        

        #verifica si falta punto y coma
        if ctx.getChild(ctx.getChildCount() - 1).getText() != ';':
            print(f"Error Sintactico: Falta un punto y coma en la declaracion de la variable {nombre_var} \n")
            self.errores.write(f"Error Sintactico: Falta un punto y coma en la declaracion de la variable {nombre_var} \n")

        #Busco si la variable ya fue declarada sino la creo y agrego a la tabla de simbolos
        if not(self.tablaSimbolos.buscarLocalID(nombre_var)):
            nuevaVar = Variable(nombre_var, tipo_dato)
        else:
            print(f"Error semantico: Variable {nombre_var} ya declarada")
            self.errores.write(f"Error Semantico: Variable {nombre_var} ya declarada \n")
            return
        #Si la variable tiene asignacion, se marca como inicializada
        if ctx.getChild(2) is not None and (str(ctx.getChild(2).getText()) == '='):
            nuevaVar.setInicializado()
        self.tablaSimbolos.agregar(nuevaVar)
        
    
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.agregarContexto() # Agrego el contexto ya que arranca un bloque
        # Agregar las variables locales al bloque
        for parametros in self.listaParametros:
            id = Variable(parametros['nombre'], parametros['tipo'])
            id.setInicializado()
            self.tablaSimbolos.agregar(id)
    
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.getContextos() # Obtener el contexto actual
    
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        self.listaVariables.clear()
    
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        nombre_var = ctx.getChild(0).getText()

        #Busco la variable en la tabla de simbolos
        variable = self.tablaSimbolos.buscarID(nombre_var)
        #Si la variable no esta declarada, no se puede asignar
        if variable == False:
            print ('Error Semantico: Variable no declarada, no se puede asignar')
            self.errores.write("Error Semantico: Variable no declarada, no se puede asignar \n")
        else:   
            variable.setInicializado()
    
    
    def identify(self, cadena): #Funcion para identificar el tipo de dato
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
            if nombre != "(": # Si el nombre no es un paréntesis, esto para cuando se escriba entre parentesis un ID
                tipo = self.identify(nombre)
                var = self.tablaSimbolos.buscarLocalID(nombre)
                # Comprobar si el tipo no es "int" o "double" (es decir, una variable)
                if tipo not in ["int", "double"]:
                    helper = {'nombre': nombre, 'tipo': tipo}
                    if var is not None:
                        # Verificar si la variable ha sido inicializada
                        if not var.getInicializado():
                            print(f"WARNING  [Semantico]: La variable {nombre} no está inicializada.\n")
                            self.errores.write(f"WARNING [Semantico]:La variable {nombre} no esta inicializada \n")
                        # Verificar si estamos en usofuncion o asignando una variable
                        if self.flagFuncion:
                            self.helperArgumentos.append(helper)
                            self.contadorArgumentos += 1
                        else:
                            # Agregar variable a las asignaciones y marcar como accedida
                            self.listaVariables.append({'tipo': var.getTipo(), 'nombre': var.getNombre()})
                        var.setAccedido()
                        self.tablaSimbolos.actualizarId(var)  # Actualizar variable en la tabla de símbolos
                    else: # Si la variable no está declarada
                        print(f"WARNING [Semantico]: La variable {nombre} no está declarada.\n")
                        self.errores.write(f"WARNING [Semantico]: La variable {nombre} no esta declarada \n")
                        return
                else: # Si el tipo es "int" o "double" (es decir, una constante)
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
            if func is not None: # Si la función está declarada
                helper = {'nombre': func_nombre, 'tipo': func.getTipo()}
                if self.flagFuncion: # Si estamos en usofuncion, agregar a la lista de argumentos
                    self.helperArgumentos.append({'nombre': func.getNombre(), 'tipo': func.getTipo()})
                    self.contadorArgumentos += 1
                else:
                    self.listaVariables.append(helper) #Si no estamos en usofuncion, es una variable y se agrega a la lista de variables
                # Agregar función a las asignaciones y marcar como accedida
                func.setAccedido()
                self.tablaSimbolos.actualizarId(func)  # Actualizar función en la tabla de símbolos
            else: # Si la función no está declarada
                print(f"WARNING [Semantico]: La función {func_nombre} no está declarada.\n")
                self.errores.write(f"WARNING [Semantico]: La funcion {func_nombre} no esta declarada \n")
                return
        
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        if ctx.getChildCount() > 1: #Si tiene mas de un hijo, entonces es un parametro
            nombre_param = ctx.getChild(1).getText()
            tipo_param = ctx.getChild(0).getText()
        else: #Si no tiene mas de un hijo, entonces no es un parametro
            nombre_param = None
            tipo_param = None
        if ctx.getChildCount() != 0: #Si el contexto no esta vacio, entonces se agrega a la lista de parametros
            self.listaParametros.append({'tipo': tipo_param, 'nombre': nombre_param})
            self.contadorParametros = self.contadorParametros + 1
            
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        if ctx.getChildCount() != 0: #Si el contexto no esta vacio, entonces se agrega a la lista de argumentos
            self.listaArgumentos.append(self.helperArgumentos) 
            self.contadorArgumentos = self.contadorArgumentos + 1
        self.helperArgumentos.clear() #Vaciamos la lista helper de argumentos
       
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        self.flagFuncion = True
        self.contadorArgumentos += 1;
        
        
        
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        nombre_func = ctx.getChild(1).getText()
        tipo_func = ctx.getChild(0).getText()
        # Verificar si la función ya está declarada
        if(self.tablaSimbolos.buscarID(nombre_func) is None):
            funcion = Funcion(nombre_func, tipo_func, copy.deepcopy(self.listaParametros))
            self.tablaSimbolos.agregar(funcion)
            #self.listaParametros.clear()
            self.listaVariables.clear()
        else: # Si la función ya está declarada
            print(f"WARNING [Semantico]: Funcion {nombre_func} ya declarada")
            self.errores.write(f"WARNING [Semantico]: Funcion {nombre_func} ya declarada \n")
    
            
    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        # Verifica si la función está declarada
        funcion = self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        if funcion is None:
            print(f"WARNING [Semantico]: Funcion {ctx.getChild(0).getText()} no declarada")
            self.errores.write(f"WARNING [Semantico]: Funcion {ctx.getChild(0).getText()} no declarada \n")
            return
    
        # Verificar los argumentos de la función
        self.listaLocalParametros = []
        for arg in self.listaArgumentos: # Recorre los argumentos
            for aux in arg: # Recorre los argumentos de cada argumento
                if aux['nombre'].isdigit(): # Si el argumento es un número, se considera una constante
                    tipo = self.identify(aux['nombre']) # Identificar el tipo de dato
                    self.listaLocalParametros.append({'nombre': aux['nombre'], 'tipo': tipo}) # Agregar a la lista de parámetros
                else: # Si el argumento no es un número, se considera una variable
                    simbolo = self.tablaSimbolos.buscarID(aux['nombre'])
                    if simbolo is not None: # Si la variable está declarada
                        self.listaLocalParametros.append({'nombre': aux['nombre'], 'tipo': simbolo.getTipo()})
                    else: # Si la variable no está declarada
                        print(f"WARNING [Semantico]: Argumento {aux['nombre']} no declarado")
                        self.errores.write(f"WARNING [Semantico]: Argumento {aux['nombre']} no declarado \n")
                        return
        parametros_funcion = funcion.getParametros()
        # Compara los tipos de los parámetros con los argumentos
        if len(self.listaParametros) != len(self.listaArgumentos): # Verifica si la cantidad de argumentos es correcta
            print("WARNING [Semantico]: Cantidad de argumentos incorrecta")
            self.errores.write("WARNING [Semantico]: Cantidad de argumentos incorrecta \n")
        else: 
            for i, parametro in enumerate(parametros_funcion): # Recorre los parámetros de la función
                if i < len(self.listaLocalParametros): # Verifica si el índice es válido
                    parametro_local = self.listaLocalParametros[i] # Obtiene el parámetro local
                    if parametro['tipo'] != parametro_local['tipo']: # Compara los tipos de los parámetros
                        print(f"WARNING [Semantico]: El argumento {parametro_local['nombre']} es de tipo {parametro_local['tipo']}. "
                            f"Se espera un argumento de tipo {parametro['tipo']}.")
                        self.errores.write("WARNING [Semantico]: El argumento {parametro_local['nombre']} es de tipo {parametro_local['tipo']}. "
                            f"Se espera un argumento de tipo {parametro['tipo']}. \n")

        # Actualiza la función en la tabla de símbolos y marca como accedido el nodo del árbol
            self.tablaSimbolos.actualizarId(funcion)
            funcion.setAccedido()
            self.listaVariables.clear()
            self.listaArgumentos.clear() # Limpiar la lista de argumentos por cada uso de función sino se acumulan

    
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        context = self.tablaSimbolos.getContextos()[-1] # Obtener el contexto actual
        self.oldSimbolos = context.getSimbolos() # Guardar los símbolos actuales
        self.tablaSimbolos.agregarContexto() # Agregar un nuevo contexto
        for simbolos in self.oldSimbolos.values(): # Agregar los símbolos anteriores al nuevo contexto
            self.tablaSimbolos.agregar(copy.deepcopy(simbolos)) # Copiar los símbolos anteriores al nuevo contexto
        
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        
        contexto_actual = self.tablaSimbolos.getContextos()[-1] # Obtener el contexto actual
        simbolos_actuales = contexto_actual.getSimbolos() # Obtener los símbolos actuales

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
                    print(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido accedida.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido accedida. \n")
                if not simbolo_nuevo.getInicializado():  
                    print(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada. \n")


        # Borrar el contexto actual
        self.tablaSimbolos.borrarContexto()

        
    def enterIfor(self, ctx:compiladoresParser.IforContext):

        context = self.tablaSimbolos.getContextos()[-1] # Obtener el contexto actual
        self.oldSimbolos = context.getSimbolos() # Guardar los símbolos actuales
        self.tablaSimbolos.agregarContexto() # Agregar un nuevo contexto
        for simbolos in self.oldSimbolos.values(): # Agregar los símbolos anteriores al nuevo contexto
            self.tablaSimbolos.agregar(copy.deepcopy(simbolos)) # Copiar los símbolos anteriores al nuevo contexto
            
    
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
                    print(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido accedida.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido accedida. \n")
                if not simbolo_nuevo.getInicializado():  
                    print(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada. \n")

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
                    print(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido accedida.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido accedida. \n")
                if not simbolo_nuevo.getInicializado():  
                    print(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {simbolo_nuevo.getNombre()} no ha sido inicializada. \n")

        # Borrar el contexto actual
        self.tablaSimbolos.borrarContexto()
      
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        for simbolosNoAccedidos in self.tablaSimbolos.getContextos()[-1].getSimbolos().values(): # Recorrer los símbolos del contexto actual
            if not simbolosNoAccedidos.getAccedido(): # Verificar si el símbolo no ha sido accedido
                print(f"WARNING [Semantico]: La variable {simbolosNoAccedidos.getNombre()} no ha sido accedida.")
                self.errores.write(f"WARNING [Semantico]: La variable {simbolosNoAccedidos.getNombre()} no ha sido accedida. \n")
      
    def exitInit(self, ctx: compiladoresParser.InitContext):
        tipo = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()
        # Verificar si la variable ya está declarada
        def verificarTipoAsignacion(var): # Verificar el tipo de asignación
            for aux in self.listaVariables: # Recorrer las variables
                if aux["tipo"] != var.getTipo(): # Verificar si el tipo de la variable es diferente
                    print(f"WARNING [Semantico]: La variable {aux['nombre']} es de tipo {aux['tipo']}. Se espera una variable tipo {var.getTipo()}\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {aux['nombre']} es de tipo {aux['tipo']}. Se espera una variable tipo {var.getTipo()} \n")

        if tipo in {"int", "double", "char"}: # Verificar si el tipo es válido
            if self.tablaSimbolos.buscarLocalID(nombre) is None: # Verificar si la variable no está declarada
                var = Variable(nombre, tipo) # Crear una nueva variable
                if ctx.getChild(2).getText() == '=': # Verificar si la variable tiene asignación
                    verificarTipoAsignacion(var) # Verificar el tipo de asignación
                    var.setInicializado() # Marcar la variable como inicializada
                    self.listaVariables.clear() # Limpiar la lista de variables
                    self.tablaSimbolos.agregar(var) # Agregar la variable a la tabla de símbolos
            else: # Si la variable ya está declarada
                print(f"WARNING [Semantico]: Ya existe una variable llamada {nombre}.\n")
                self.errores.write(f"WARNING [Semantico]: Ya existe una variable llamada {nombre}. \n")
        elif nombre == "=": # Verificar si falta el tipo de dato
            var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
            if var is not None: # Verificar si la variable está declarada
                verificarTipoAsignacion(var)
                var.setInicializado()
                self.tablaSimbolos.actualizarId(var)
                self.listaVariables.clear()
            else: # Si la variable no está declarada
                print(f"WARNING [Semantico]: La variable {ctx.getChild(0).getText()} no está declarada.\n")
                self.errores.write(f"WARNING [Semantico]: La variable {ctx.getChild(0).getText()} no está declarada.\n")
                self.listaVariables.clear()

    