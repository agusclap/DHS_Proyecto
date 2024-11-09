from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Estructuras.TablaSimbolos import TablaSimbolos
from Estructuras.Id import Funcion, Variable
import copy
from Estructuras.Contexto import Contexto

class Escucha (compiladoresListener):
    listaVariables = []
    tablaSimbolos = TablaSimbolos()
    listaParametros = []
    listaArgumentos = []
    helperArgumentos = []
    #contadorParametros = []
    contadorArgumentos = []
    declaration_type = None 
    flagFuncion = False
    flagUsoFuncion = False
    errores = open("./output/errores.txt", "w")
    
    
    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Comienzo de la compilacion")
        
    
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        self.declaration_type = str(ctx.getChild(0).getText())
        nombre_var = str(ctx.getChild(1).getText())
        if self.tablaSimbolos.buscarLocalID(nombre_var) == None:
            nuevaVar = Variable(nombre_var, self.declaration_type, False, False)
            if(ctx.getChildCount() > 2):
                for var in self.listaVariables:
                    if var['tipo'] != nuevaVar.getTipo():
                        print(f"WARNING semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion")
                        self.errores.write(f"WARNING Semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion \n")
                
                nuevaVar.setInicializado()
                self.listaVariables.clear()
            self.tablaSimbolos.agregar(nuevaVar)
        else:
            print(f"Error semantico: Variable {nombre_var} ya declarada")
            self.errores.write(f"Error Semantico: Variable {nombre_var} ya declarada \n")
            return
        
        
    def exitDeclaraciones(self, ctx:compiladoresParser.DeclaracionesContext):
        if ctx.getChildCount() > 0:
            if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText()) == None:
                nuevaVar = Variable(str(ctx.getChild(1).getText()), self.declaration_type)
                if(ctx.getChildCount() > 3):
                    for var in self.listaVariables:
                        if var["tipo"] != nuevaVar.getTipo():
                            print(f"WARNING semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion")
                            self.errores.write(f"WARNING Semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion \n")
                    nuevaVar.setInicializado()
                    self.listaVariables.clear()
                self.tablaSimbolos.agregar(nuevaVar)
            else:
                    print(f"Error semantico: Variable {str(ctx.getChild(1).getText())} ya declarada")
                    self.errores.write(f"Error Semantico: Variable {str(ctx.getChild(1).getText())} ya declarada \n")
                    return
    
    def exitDeclaracionesp(self, ctx:compiladoresParser.DeclaracionespContext):
        self.declaration_type = None # Limpiar el tipo de declaración  
        
    
    
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.agregarContexto() # Agrego el contexto ya que arranca un bloque
        # Agregar las variables locales al bloque
        if self.flagFuncion == True:
            for parametros in self.listaParametros:
                id = Variable(parametros['nombre'], parametros['tipo'])
                id.setInicializado()
                self.tablaSimbolos.agregar(id)
        self.flagFuncion == False
    
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        contexto = self.tablaSimbolos.borrarContexto() # Obtener el contexto actual
        for sim in contexto.getSimbolos().values():
            if isinstance(sim, Variable):
                if sim.getInicializado() == False:
                    print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada.\n")
                    self.errores.write(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada. \n")
                else:
                    if sim.getAccedido() == False:
                        print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida.\n")
                        self.errores.write(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida. \n")
            else:
                if sim.getAccedido() == False:
                    print(f"WARNING [Semantico]: La función {sim.getNombre()} no ha sido accedida.\n")
                    self.errores.write(f"WARNING [Semantico]: La funcion {sim.getNombre()} no ha sido accedida. \n")    
                               
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        self.listaVariables.clear()
        print("inicio asignacion")
    
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        #Busco la variable en la tabla de simbolos
        variable = self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        #Si la variable no esta declarada, no se puede asignar
        if variable != None:
            for var in self.listaVariables:
                if var["tipo"] != variable.getTipo():
                    print(f"WARNING semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion")
                    self.errores.write(f"WARNING Semantico: Variable {var['nombre']} de tipo {var['tipo']} no coincide con el tipo de la declaracion \n")
            variable.setInicializado()
            self.tablaSimbolos.actualizarId(variable)
            self.listaVariables.clear()
        else:   
            print(f'Error Semantico: Variable {ctx.getChild(0).getText()}  no esta declarada, no se puede asignar')
            self.errores.write(f"Error Semantico: Variable {ctx.getChild(0).getText()} no esta declarada, no se puede asignar \n")
            self.listaVariables.clear()
        return
    
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
                        helper = {'tipo': var.getTipo(), 'nombre': var.getNombre()}    
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
                        self.helperArgumentos.append(helper)
                    else:
                        self.listaVariables.append(helper)
        #Para una funcion
        else:
            nombre = ctx.getChild(0).getChild(0).getText()
            funcion = self.tablaSimbolos.buscarID(nombre)
            if funcion != None:
                helper = {'tipo': funcion.getTipo(), 'nombre': funcion.getNombre()}
                if self.flagUsoFuncion:
                    self.helperArgumentos.append(helper)
            else:
                self.listaVariables.append(helper)
            funcion.setAccedido()
            self.tablaSimbolos.actualizarId(funcion)
        
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        if ctx.getChildCount() != 0: #Si el contexto no esta vacio, entonces se agrega a la lista de parametros
            tipo_param = ctx.getChild(0).getText()
            nombre_param = ctx.getChild(1).getText()
            self.listaParametros.append({'nombre': nombre_param, 'tipo': tipo_param})
            
                        
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        if ctx.getChildCount() != 0: #Si el contexto no esta vacio, entonces se agrega a la lista de argumentos
            self.listaArgumentos.append(self.helperArgumentos) 
            if self.contadorArgumentos:
                self.contadorArgumentos[-1] += 1
            self.helperArgumentos = []
            
            
        
    def exitPrototipo(self, ctx:compiladoresParser.PrototipoContext):
        
        if self.tablaSimbolos.buscarID(ctx.getChild(1).getText()) != None:
            print(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada")
            self.errores.write(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada \n")
            return
        funcion = Funcion(ctx.getChild(1).getText(), ctx.getChild(0).getText(), copy.deepcopy(self.listaParametros))
        self.tablaSimbolos.agregar(funcion)
        self.listaParametros.clear()    
        
            
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        self.flagFuncion = True
        
        
        
        
        
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        funcion = Funcion(ctx.getChild(1).getText(),ctx.getChild(0).getText(), copy.deepcopy(self.listaParametros))
        funcion_aux = self.tablaSimbolos.buscarID(ctx.getChild(1).getText())
        if funcion_aux != None:
            if funcion_aux.getInicializado() :
                print(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada")
                self.errores.write(f"WARNING [Semantico]: Funcion {ctx.getChild(1).getText()} ya declarada \n")
                self.listaParametros.clear()
                return
            aux_prot = funcion_aux.getParametros()
            aux_funcion = copy.deepcopy(self.listaParametros)
            
            if len(aux_funcion) > len(aux_prot):
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(1).getText()} tiene mas parametros de los que deberia")
            elif len(aux_funcion) < len(aux_prot):
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(1).getText()} tiene menos parametros de los que deberia")

            for parametro in aux_prot:
                aux = aux_funcion.pop()
                if aux["tipo"] != parametro["tipo"]:
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
        self.flagUsoFuncion = True
        self.contadorArgumentos.append(0)
           
    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        # Verifica si la función está declarada
        self.flagUsoFuncion = False
        funcion = self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        if funcion != None:
    
            # Verificar los argumentos de la función
            listaArgumentos = []
            listaAuxiliar = []
        
            parametro = funcion.getParametros()
            for argumento in self.listaArgumentos:
                for arg in argumento:
                
                    if arg["tipo"] != "int" and arg["tipo"] != "double":
                    
                        if self.tablaSimbolos.buscarID(arg["nombre"]) == None:
                            print(f"WARNING [Semantico]: Variable {arg['nombre']} no declarada")
                            self.errores.write(f"WARNING [Semantico]: Variable {arg['nombre']} no declarada \n")
                        else:
                            listaAuxiliar.append(arg)
                            auxID = self.tablaSimbolos.buscarID(arg["nombre"])
                            auxID.setAccedido()
                            self.tablaSimbolos.actualizarId(auxID)
                    else:
                        listaAuxiliar.append(arg)
                listaArgumentos.append(listaAuxiliar)
                listaAuxiliar = []
            
            for param in parametro:
            
                aux = listaArgumentos.pop()
                for aux1 in aux:
                    if aux1['tipo'] != param['tipo']:
                        print(f"WARNING [Semantico]: El parametro {aux1['nombre']} de la funcion {ctx.getChild(0).getText()} no coincide con el tipo de la declaracion")
                        self.errores.write(f"WARNING [Semantico]: El parametro {aux1['nombre']} de la funcion {ctx.getChild(0).getText()} no coincide con el tipo de la declaracion \n") 

            cantidadArgumentos = self.contadorArgumentos.pop()
            if cantidadArgumentos < len(parametro):
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene menos parametros de los que deberia")
                self.errores.write(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene menos parametros de los que deberia \n")
            elif cantidadArgumentos > len(parametro):
                print(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene mas parametros de los que deberia")
                self.errores.write(f"WARNING [Semantico]: La funcion {ctx.getChild(0).getText()} tiene mas parametros de los que deberia \n")
            
            funcion.setAccedido()
            self.tablaSimbolos.actualizarId(funcion)
            return
        
        print(f"WARNING [Semantico]: Funcion {ctx.getChild(0).getText()} no declarada")
        self.errores.write(f"WARNING [Semantico]: Funcion {ctx.getChild(0).getText()} no declarada \n")
        return
            
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("Inicio declaracion")
      
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        #La funcion main siempre se va a acceder si es que existe
        main = self.tablaSimbolos.buscarID("main")
        if main is not None:
            main.setAccedido()
            self.tablaSimbolos.actualizarId(main)
        last_context = self.tablaSimbolos.borrarContexto()
        for sim in last_context.getSimbolos().values():
            if isinstance(sim, Variable):
                if sim.getAccedido == False:
                    print(f"WARNING: Variable {sim.getNombre} no accedida")
                else:
                    if sim.getInicializado == False:
                        print(f"WARNING: Variable {sim.getNombre} no inicializada")
            else:
                if sim.getAccedido == False:
                    print(f"WARNING: Funcion {sim.getNombre} no accedida")
        # # Verificar si hay variables no accedidas

    