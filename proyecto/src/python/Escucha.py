from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Estructuras.TablaSimbolos import TablaSimbolos
from Estructuras.Id import Funcion, Variable
import copy
from Estructuras.Contexto import Contexto

class Escucha (compiladoresListener):
    listaVariables = [] # Lista de variables para asignaciones
    tablaSimbolos = TablaSimbolos() # Tabla de símbolos
    listaParametros = [] # Lista de parámetros de una función
    listaArgumentos = [] # Lista de argumentos de una función
    helperArgumentos = [] # Lista auxiliar de argumentos
    contadorArgumentos = [] # Contador de argumentos
    declaration_type = None   # Tipo de declaración
    flagFuncion = False # Bandera para saber si se está en una función
    flagUsoFuncion = False # Bandera para saber si se está en un uso de función
    errores = open("./output/errores.txt", "w") # Archivo de errores
    
    
    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Comienzo de la compilacion")
        
    
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        self.declaration_type = str(ctx.getChild(0).getText()) # Obtener el tipo de declaración
        nombre_var = str(ctx.getChild(1).getText()) # Obtener el nombre de la variable
        if self.tablaSimbolos.buscarLocalID(nombre_var) == None: # Verificar si la variable no está declarada
            nuevaVar = Variable(nombre_var, self.declaration_type, False, False) # Crear una nueva variable
            if(ctx.getChildCount() > 2): # Si la declaración tiene más de 2 hijos, entonces se está inicializando
                for var in self.listaVariables: # Verificar si las variables a inicializar son del mismo tipo
                    if var['tipo'] != nuevaVar.getTipo(): # Si no son del mismo tipo, mostrar un warning
                        print(f"WARNING semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion")
                        self.errores.write(f"WARNING Semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion \n")
                
                nuevaVar.setInicializado() # Marcar la variable como inicializada
                self.listaVariables.clear() # Limpiar la lista de variables
            self.tablaSimbolos.agregar(nuevaVar) # Agregar la variable a la tabla de símbolos
        else: # Si la variable ya está declarada, mostrar un error
            print(f"Error semantico: Variable {nombre_var} ya declarada")
            self.errores.write(f"Error Semantico: Variable {nombre_var} ya declarada \n")
            return
        
        
    def exitDeclaraciones(self, ctx:compiladoresParser.DeclaracionesContext):
        if ctx.getChildCount() > 0: # Si el contexto tiene más de 0 hijos, entonces se está declarando una variable
            if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText()) == None: # Verificar si la variable no está declarada
                nuevaVar = Variable(str(ctx.getChild(1).getText()), self.declaration_type) # Crear una nueva variable
                if(ctx.getChildCount() > 3): # Si la declaración tiene más de 3 hijos, entonces se está inicializando
                    for var in self.listaVariables: # Verificar si las variables a inicializar son del mismo tipo
                        if var["tipo"] != nuevaVar.getTipo(): # Si no son del mismo tipo, mostrar un warning
                            print(f"WARNING semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion")
                            self.errores.write(f"WARNING Semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion \n")
                    nuevaVar.setInicializado() # Marcar la variable como inicializada
                    self.listaVariables.clear() # Limpiar la lista de variables
                self.tablaSimbolos.agregar(nuevaVar) # Agregar la variable a la tabla de símbolos
            else: # Si la variable ya está declarada, mostrar un error
                    print(f"Error semantico: Variable {str(ctx.getChild(1).getText())} ya declarada")
                    self.errores.write(f"Error Semantico: Variable {str(ctx.getChild(1).getText())} ya declarada \n")
                    return
    
    def exitDeclaracionesp(self, ctx:compiladoresParser.DeclaracionespContext):
        self.declaration_type = None # Limpiar el tipo de declaración  
        
    
    
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.agregarContexto() # Agrego el contexto ya que arranca un bloque
        # Agregar las variables locales al bloque
        if self.flagFuncion == True: # Si se está en una función, agregar los parámetros
            for parametros in self.listaParametros: # Agregar los parámetros a la tabla de símbolos
                id = Variable(parametros['nombre'], parametros['tipo']) # Crear una nueva variable
                id.setInicializado() # Marcar la variable como inicializada
                self.tablaSimbolos.agregar(id) # Agregar la variable a la tabla de símbolos
        self.flagFuncion == False # Limpiar la bandera de función
    
    def exitBloque(self, ctx:compiladoresParser.BloqueContext): 
        contexto = self.tablaSimbolos.borrarContexto() # Obtener el contexto actual
        for sim in contexto.getSimbolos().values(): # Recorrer los símbolos del contexto
            if isinstance(sim, Variable): # Si el símbolo es una variable
                if sim.getInicializado() == False: # Si la variable no está inicializada, mostrar un warning
                    print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada. \n")
                else: # Si la variable está inicializada, verificar si fue accedida
                    if sim.getAccedido() == False: # Si la variable no fue accedida, mostrar un warning
                        print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida.\n")
                        self.errores.write(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida. \n")
            else: # Si el símbolo es una función
                if sim.getAccedido() == False:
                    print(f"WARNING [Semantico]: La función {sim.getNombre()} no ha sido accedida.\n")
                    self.errores.write(f"WARNING [Semantico]: La funcion {sim.getNombre()} no ha sido accedida. \n")    
                               
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        self.listaVariables.clear() # Limpiar la lista de variables para asignaciones
    
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        #Busco la variable en la tabla de simbolos
        variable = self.tablaSimbolos.buscarID(ctx.getChild(0).getText()) 
        #Si la variable no esta declarada, no se puede asignar
        if variable != None: 
            for var in self.listaVariables: # Verificar si las variables a asignar son del mismo tipo
                if var["tipo"] != variable.getTipo(): # Si no son del mismo tipo, mostrar un warning
                    print(f"WARNING semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion")
                    self.errores.write(f"WARNING Semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion \n")
            variable.setInicializado() # Marcar la variable como inicializada
            self.tablaSimbolos.actualizarId(variable) # Actualizar la variable en la tabla de símbolos
            self.listaVariables.clear() # Limpiar la lista de variables para asignaciones
        else:   #Si la variable no esta declarada, no se puede asignar
            print(f'Error Semantico: Variable {ctx.getChild(0).getText()}  no esta declarada, no se puede asignar')
            self.errores.write(f"Error Semantico: Variable {ctx.getChild(0).getText()} no esta declarada, no se puede asignar \n")
            self.listaVariables.clear() # Limpiar la lista de variables para asignaciones
        return #Retorno para no seguir con la ejecucion de la funcion
    
    def identify(self, cadena): #Funcion para identificar el tipo de dato
        # Intentar convertir a entero
        try:
            int(cadena)  
            return "int"
        except ValueError:
            #Verifica si la cadena ingresada es tipo Float en python que seria Double en C
            try:
                float(cadena)  
                return "double"
            #Si no es ni int ni double retorno que no es un numero
            except ValueError:
                return "no es un número"
                
    def exitFactor(self, ctx: compiladoresParser.FactorContext):
    # Obtener el primer hijo del contexto, que puede ser una variable o función
        primer_hijo = ctx.getChild(0)
    
    # Caso 1: Si el primer hijo no tiene múltiples hijos, se considera una variable
        if not primer_hijo.getChildCount() > 1:
            
            nombre = primer_hijo.getText()
            
            if nombre != "(": # Si el nombre no es un paréntesis, esto para cuando se escriba entre parentesis un ID
                # Comprobar si el tipo no es "int" o "double" (es decir, una variable)
                if self.identify(nombre) != "int" and self.identify(nombre) != "double":
                    var = self.tablaSimbolos.buscarID(nombre)
                    if var != None:
                        # Verificar si la variable ha sido inicializada
                        if not var.getInicializado() == True:
                            print(f"WARNING  [Semantico]: La variable {nombre} no está inicializada.\n")
                            self.errores.write(f"WARNING [Semantico]:La variable {nombre} no esta inicializada \n")
                        helper = {'tipo': var.getTipo(), 'nombre': var.getNombre()} # Crear un diccionario auxiliar    
                        # Verificar si estamos en usofuncion o asignando una variable
                        if self.flagUsoFuncion:
                            self.helperArgumentos.append(helper)
                        else: 
                            # Agregar variable a las asignaciones y marcar como accedida
                            self.listaVariables.append(helper)
                        var.setAccedido()
                        self.tablaSimbolos.actualizarId(var)  # Actualizar variable en la tabla de símbolos
                    else: # Si la variable no está declarada
                        print(f"WARNING [Semantico]: La variable {nombre} no está declarada.\n")
                        self.errores.write(f"WARNING [Semantico]: La variable {nombre} no esta declarada \n")
                        return
                else: # Si el tipo es "int" o "double" (es decir, una constante)
                    helper = {'tipo': self.identify(ctx.getChild(0).getText()), 'nombre': ctx.getChild(0).getText()}
                    if self.flagUsoFuncion:
                        self.helperArgumentos.append(helper) # Agregar la constante a los argumentos
                    else:
                        self.listaVariables.append(helper) # Agregar la constante a las asignaciones
        #Para una funcion
        else:
            nombre = ctx.getChild(0).getChild(0).getText()
            funcion = self.tablaSimbolos.buscarID(nombre)
            if funcion != None: # Si la función está declarada
                helper = {'tipo': funcion.getTipo(), 'nombre': funcion.getNombre()}
                if self.flagUsoFuncion: # Si se está en un uso de función
                    self.helperArgumentos.append(helper) # Agregar la función a los argumentos
            else: # Si no esta en uso de funcion
                self.listaVariables.append(helper) # Agregar a lista variables 
            funcion.setAccedido() # Marcar la función como accedida
            self.tablaSimbolos.actualizarId(funcion) # Actualizar la función en la tabla de símbolos
        
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        if ctx.getChildCount() != 0: #Si el contexto no esta vacio, entonces se agrega a la lista de parametros
            tipo_param = ctx.getChild(0).getText()
            nombre_param = ctx.getChild(1).getText()
            self.listaParametros.append({'nombre': nombre_param, 'tipo': tipo_param}) # Agregar el parámetro a la lista de parámetros
            
                        
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        if ctx.getChildCount() != 0: #Si el contexto no esta vacio, entonces se agrega a la lista de argumentos
            self.listaArgumentos.append(self.helperArgumentos) # Agregar los argumentos a la lista de argumentos
            if self.contadorArgumentos: # Incrementar el contador de argumentos
                self.contadorArgumentos[-1] += 1 
            self.helperArgumentos = [] # Limpiar la lista auxiliar de argumentos
            
            
        
    def exitPrototipo(self, ctx:compiladoresParser.PrototipoContext):
        # Verificar si la función ya está declarada
        if self.tablaSimbolos.buscarID(ctx.getChild(1).getText()) != None:
            print(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada")
            self.errores.write(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada \n")
            return
        funcion = Funcion(ctx.getChild(1).getText(), ctx.getChild(0).getText(), copy.deepcopy(self.listaParametros))
        self.tablaSimbolos.agregar(funcion) # Agregar la función a la tabla de símbolos
        self.listaParametros.clear()     # Limpiar la lista de parámetros
        
            
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        self.flagFuncion = True # Marcar que se está en una función
        
        
        
        
        
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext): 
        funcion = Funcion(ctx.getChild(1).getText(),ctx.getChild(0).getText(), copy.deepcopy(self.listaParametros))
        funcion_aux = self.tablaSimbolos.buscarID(ctx.getChild(1).getText())
        if funcion_aux != None: # Verificar si la función ya está declarada
            if funcion_aux.getInicializado() : # Verificar si la función ya fue inicializada
                print(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada")
                self.errores.write(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada \n")
                self.listaParametros.clear()
                return
            aux_prot = funcion_aux.getParametros() # Obtener los parámetros de la función
            aux_funcion = copy.deepcopy(self.listaParametros) # Obtener los parámetros de la función actual
            
            if len(aux_funcion) > len(aux_prot): # Verificar si la función tiene más parámetros de los que debería
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(1).getText()} tiene mas parametros de los que deberia")
            elif len(aux_funcion) < len(aux_prot): # Verificar si la función tiene menos parámetros de los que debería
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(1).getText()} tiene menos parametros de los que deberia")

            for parametro in aux_prot: # Verificar si los parámetros de la función coinciden con los de la declaración
                aux = aux_funcion.pop() # Obtener el parámetro de la función actual
                if aux["tipo"] != parametro["tipo"]: # Si los tipos no coinciden, mostrar un warning
                    print(f"WARNING [Semantico]: El parametro {aux['nombre']} de la funcion {ctx.getChild(1).getText()} no coincide con el tipo de la declaracion")
                    self.errores.write(f"WARNING [Semantico]: El parametro {aux['nombre']} de la funcion {ctx.getChild(1).getText()} no coincide con el tipo de la declaracion \n")
            funcion.setInicializado()
            self.tablaSimbolos.actualizarId(funcion)
            self.listaParametros.clear()        
            return
        funcion = Funcion(ctx.getChild(1).getText(), ctx.getChild(0).getText(), copy.deepcopy(self.listaParametros))
        funcion.setInicializado()
        self.tablaSimbolos.agregar(funcion)
        self.listaParametros.clear()
        
    def enterUsofuncion(self, ctx:compiladoresParser.UsofuncionContext):
        self.flagUsoFuncion = True # Marcar que se está en un uso de función
        self.contadorArgumentos.append(0) # Inicializar el contador de argumentos
           
    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        # Verifica si la función está declarada
        self.flagUsoFuncion = False
        funcion = self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        if funcion != None:
    
            # Verificar los argumentos de la función
            listaArgumentos = []
            listaAuxiliar = []
        
            parametro = funcion.getParametros()
            for argumento in self.listaArgumentos: # Verificar si los argumentos de la función coinciden con los de la declaración
                for arg in argumento:
                
                    if arg["tipo"] != "int" and arg["tipo"] != "double":
                    
                        if self.tablaSimbolos.buscarID(arg["nombre"]) == None: # Verificar si la variable no está declarada
                            print(f"WARNING [Semantico]: Variable {arg['nombre']} no declarada")
                            self.errores.write(f"WARNING [Semantico]: Variable {arg['nombre']} no declarada \n")
                        else: # Si la variable está declarada
                            listaAuxiliar.append(arg) # Agregar la variable a la lista auxiliar
                            auxID = self.tablaSimbolos.buscarID(arg["nombre"]) # Obtener la variable de la tabla de símbolos
                            auxID.setAccedido() # Marcar la variable como accedida
                            self.tablaSimbolos.actualizarId(auxID) # Actualizar la variable en la tabla de símbolos
                    else:
                        listaAuxiliar.append(arg) # Agregar la constante a la lista auxiliar
                listaArgumentos.append(listaAuxiliar) # Agregar la lista auxiliar a la lista de argumentos
                listaAuxiliar = [] # Limpiar la lista auxiliar
            
            for param in parametro: # Verificar si los argumentos de la función coinciden con los de la declaración
            
                aux = listaArgumentos.pop()
                for aux1 in aux:
                    if aux1['tipo'] != param['tipo']:
                        print(f"WARNING [Semantico]: El parametro {aux1['nombre']} de la funcion {ctx.getChild(0).getText()} no coincide con el tipo de la declaracion")
                        self.errores.write(f"WARNING [Semantico]: El parametro {aux1['nombre']} de la funcion {ctx.getChild(0).getText()} no coincide con el tipo de la declaracion \n") 

            cantidadArgumentos = self.contadorArgumentos.pop()
            if cantidadArgumentos < len(parametro): # Verificar si la función tiene menos parámetros de los que debería
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene menos parametros de los que deberia")
                self.errores.write(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene menos parametros de los que deberia \n")
            elif cantidadArgumentos > len(parametro): # Verificar si la función tiene más parámetros de los que debería
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene mas parametros de los que deberia")
                self.errores.write(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene mas parametros de los que deberia \n")
            
            funcion.setAccedido()
            self.tablaSimbolos.actualizarId(funcion)
            return
        #Si la funcion no esta declarada, se muestra un warning
        print(f"WARNING [Semantico]: Funcion {ctx.getChild(0).getText()} no declarada")
        self.errores.write(f"WARNING [Semantico]: Funcion {ctx.getChild(0).getText()} no declarada \n")
        return
            
      
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        #La funcion main siempre se va a acceder si es que existe
        main = self.tablaSimbolos.buscarID("main")
        if main is not None:
            main.setAccedido()
            self.tablaSimbolos.actualizarId(main)
        last_context = self.tablaSimbolos.borrarContexto()
        for sim in last_context.getSimbolos().values(): # Recorrer los símbolos del contexto
            if isinstance(sim, Variable): # Si el símbolo es una variable
                if sim.getAccedido == False:
                    print(f"WARNING: Variable {sim.getNombre()} no accedida")
                else:
                    if sim.getInicializado == False:
                        print(f"WARNING: Variable {sim.getNombre()} no inicializada")
            else:
                if sim.getAccedido() == False:
                    print(f"WARNING: Funcion {sim.getNombre()} no accedida")
        # # Verificar si hay variables no accedidas

    