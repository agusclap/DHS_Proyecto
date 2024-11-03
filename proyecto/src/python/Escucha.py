from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Estructuras.TablaSimbolos import TablaSimbolos
from Estructuras.Id import Funcion, Variable
import copy
from Estructuras import Contexto

class Escucha (compiladoresListener):
    #numTokens = 0
    #numNodos = 0
    listaVariables = []
    listaParametros = []
    listaArgumentos = []
    helperArgumentos = []
    contadorParametros = 0
    contadorArgumentos = 0
    #archivo = open("./output/TabelaSimbolos.txt", "w")
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
        if not(self.tablaSimbolos.buscarLocal(nombre_var)):
            nuevaVar = Variable(nombre_var, tipo_dato)
            print("Nuevo simbolo agregado")
        else:
            print(f"Error semantico: Variable {nombre_var} ya declarada")
            return
        
        if ctx.getChild(2) is not None and (str(ctx.getChild(2).getText()) == '='):
            print('Declaracion con asignacion')
            nuevaVar.setInicializado()
        else:
            print('Declaracion sin asignacion')

        self.tablaSimbolos.agregar(nuevaVar)
        
    
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.agregarContexto()
    
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print("Fin de bloque")
        self.tablaSimbolos.getContextos()
           
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        print("Fin de asignacion")
        nombre_var = ctx.getChild(0).getText()


        variable = self.tablaSimbolos.buscar(nombre_var)

        if variable == False:
            print ('Error Semantico: Variable no declarada, no se puede asignar')
        else:   
            for sim in variable.getSimbolos().values():
                if sim.nombre == nombre_var:
                    sim.setInicializado()
                    print('Variable asignada')
                    break
    
    
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
        print("Fin de factor")
    # Obtener el primer hijo del contexto, que puede ser una variable o función
        primer_hijo = ctx.getChild(0)
        nombre = primer_hijo.getText()
    
    # Caso 1: Si el primer hijo no tiene múltiples hijos, se considera una variable
        if primer_hijo.getChildCount() <= 1:
            tipo = self.identify(nombre)
        
            # Comprobar si el tipo no es "int" o "double" (es decir, una variable)
            if tipo not in ["int", "double"]:
                var = self.tablaSimbolos.buscarLocalID(nombre)
                nombre_var = var.getNombre()
                tipo_var = var.getTipo()
                helper = {'nombre': nombre_var, 'tipo': tipo_var}
                if var is not None:
                    # Verificar si la variable ha sido inicializada
                    if not var.getInicializado():
                        print(f"ERROR Semantico: La variable {nombre} no está inicializada.\n")
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
                    print(f"ERROR Semantico: La variable {nombre} no está declarada.\n")
                    return
            else:
                helper = {'nombre': nombre_var, 'tipo': tipo_var}
                if self.flagFuncion:
                    self.helperArgumentos.append(helper)
                    self.contadorArgumentos += 1
                else:
                    # Si es una constante, agregar a las asignaciones
                    self.listaVariables.append({'tipo': var.getTipo(), 'nombre': var.getNombre()})
        # Caso 2: Si el primer hijo tiene múltiples hijos, se considera una función
        else:
            
            func_nombre = primer_hijo.getChild(0).getText()
            func = self.tablaSimbolos.buscarID(func_nombre)
            if func is not None:
                helper = {'nombre': nombre_var, 'tipo': tipo_var}
                if self.flagFuncion:
                    self.helperArgumentos.append({'nombre': func.getNombre(), 'tipo': func.getTipo()})
                    self.contadorArgumentos += 1
                else:
                    self.listaVariables.append(helper)
                # Agregar función a las asignaciones y marcar como accedida
                func.setAccedido()
                self.tablaSimbolos.actualizarFuncion(func)  # Actualizar función en la tabla de símbolos
            else:
                print(f"ERROR Semantico: La función {func_nombre} no está declarada.\n")
                return
        
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        print("Fin de parametro")
        if ctx.getChildCount() > 1:
            nombre_param = ctx.getChild(1).getText()
            tipo_param = ctx.getChild(0).getText()
        else:
            nombre_param = None
            tipo_param = None
        if ctx.getChildCount() != 0:
            self.listaParametros.append({'tipo': tipo_param, 'nombre': nombre_param})
            self.contadorParametros = self.contadorParametros + 1
        else:
            print("No hay parametros")
    
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        print("Fin de argumentos")
        nombre_arg = ctx.getChild(0).getText()
        if ctx.getChildCount() != 0:
            print("Hay argumentos")
            self.listaArgumentos.append(self.helperArgumentos) #VOLVER despues de usofuncion
        self.helperArgumentos.clear() #Vaciamos la lista helper de argumentos
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        print("Fin de funcion")
        nombre_func = ctx.getChild(1).getText()
        tipo_func = ctx.getChild(0).getText()
        print(nombre_func)
        if(self.tablaSimbolos.buscarID(nombre_func) is None):
            funcion = Funcion(nombre_func, tipo_func, copy.deepcopy(self.listaParametros))
            self.tablaSimbolos.agregar(funcion)
            print("Funcion agregada")
            self.listaParametros.clear()
            self.listaVariables.clear()
        else:
            print("Error Semantico: Funcion ya declarada")
    
            
    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        # Verifica si la función está declarada
        funcion = self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        if funcion is None:
            print("Error Semantico: Funcion no declarada")
            return
    
        # Verificar los argumentos de la función
        self.listaLocalParametros = []
        for arg in self.listaArgumentos:
            if arg['nombre'].isdigit():
                tipo = self.identify(arg['nombre'])
                self.listaLocalParametros.append({'nombre': arg['nombre'], 'tipo': tipo})
            else:
                simbolo = self.tablaSimbolos.buscarID(arg['nombre'])
                if simbolo is not None:
                    self.listaLocalParametros.append({'nombre': arg['nombre'], 'tipo': simbolo.getTipo()})
                else:
                    print("Error Semantico: Argumento no declarado")
                    return

        # Compara los tipos de los parámetros con los argumentos
        parametros_funcion = funcion.getParametros()
        if self.contadorParametros != self.contadorArgumentos:
            print("Error Semantico: Cantidad de argumentos incorrecta")
            return

        for i, parametro in enumerate(parametros_funcion):
            parametro_local = self.listaLocalParametros[i]
            if parametro['tipo'] != parametro_local['tipo']:
                print(f"WARNING: El argumento {parametro_local['nombre']} es de tipo {parametro_local['tipo']}. "
                    f"Se espera un argumento de tipo {parametro['tipo']}.")

        # Actualiza la función en la tabla de símbolos y marca como accedido el nodo del árbol
            self.tablaSimbolos.actualizarFuncion(ctx.getChild(0).getText())
            ctx.getChild(0).setAccedido()
            self.listaVariables.clear()

    
    def exitReturn(self, ctx: compiladoresParser.ReturnContext):
        if ctx.getChild(1).getText() is None:
            print("Contexto de retorno vacío")
            return

        print("Fin de return")
        
        if ctx.getChildCount() > 1:
            retorno_texto = ctx.getChild(1).getText()
            
            if retorno_texto.isdigit():  # Revisa si el retorno es un número entero
                print("El retorno es un número entero")
            else:
                nombre_var = retorno_texto
                print(nombre_var)
                for parametro in self.listaParametros:
                    print (parametro['nombre'])
                    if parametro['nombre'] == nombre_var:
                        print("Variable y parámetro concuerdan")
                        break
                    elif self.tablaSimbolos.buscarLocalID(nombre_var) is not None and nombre_var == self.tablaSimbolos.buscarLocalID(nombre_var).getNombre():
                        print("Variable encontrada")
                        break
                    else:
                        print("No se encontró una coincidencia para la variable en los parámetros")
        else:
            print("No hay retorno")

    def enterIwhile(self, ctx:compiladoresParser.WhileContext):
        
        context = Contexto()
        for simbolos in self.tablaSimbolos.getContextos()[-1]:
            context.agregarSimbolo(simbolos)
        self.tablaSimbolos.agregarContexto(context)
    
    def enterIfor(self, ctx:compiladoresParser.ForContext):

        context = Contexto()
        for simbolos in self.tablaSimbolos.getContextos()[-1]:
            context.agregarSimbolo(simbolos)
        self.tablaSimbolos.agregarContexto(context)
    
    def enterIif(self, ctx:compiladoresParser.IfContext):
        
        context = Contexto()
        for simbolos in self.tablaSimbolos.getContextos()[-1]:
            context.agregarSimbolo(simbolos)
        self.tablaSimbolos.agregarContexto(context)
      
      
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
          print("Fin de la compilacion")
          for simbolosNoAccedidos in self.tablaSimbolos.getContextos()[-1].getSimbolos().values():
              if not simbolosNoAccedidos.getAccedido():
                  print(f"WARNING: El simbolo {simbolosNoAccedidos.getNombre()} no ha sido accedido.")
      
    def exitInit(self, ctx: compiladoresParser.InitContext):
        tipo = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()

        def verificarTipoAsignacion(var):
            for aux in self.variablesAsignacion:
                if aux["tipo"] != var.getTipo():
                    print(f"WARNING: La variable {aux['nombre']} es de tipo {aux['tipo']}. Se espera una variable tipo {var.getTipo()}\n")

        if tipo in {"int", "double", "char"}:
            if self.tablaSimbolos.buscarLocalID(nombre) is None:
                var = Variable(nombre, tipo)
                if ctx.getChild(2).getText() == '=':
                    verificarTipoAsignacion(var)
                    var.setInicializado()
                    self.variablesAsignacion.clear()
                    self.tablaSimbolos.agregarID(var)
            else:
                print(f"ERROR: Ya existe una variable llamada {nombre}.\n")
        elif nombre == "=":
            var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
            if var is not None:
                verificarTipoAsignacion(var)
                var.setInicializado()
                self.tablaSimbolos.actualizarId(var)
                self.variablesAsignacion.clear()
            else:
                print(f'ERROR: La variable {ctx.getChild(0).getText()} no está declarada.\n')
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
    