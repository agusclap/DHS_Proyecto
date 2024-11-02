from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Estructuras.TablaSimbolos import TablaSimbolos
from Estructuras.Id import Funcion, Variable
import copy

class Escucha (compiladoresListener):
    numTokens = 0
    numNodos = 0
    listaVariables = []
    listaParametros = []
    listaArgumentos = []
    #archivo = open("./output/TabelaSimbolos.txt", "w")

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
            
            
    def enterDeclaracion(self, ctx):
        print("Inicio de declaracion")        
    
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        
        #Declaro variables
        nombre_var = ctx.getChild(1).getText()
        tipo_dato = ctx.getChild(0).getText()
        
        for i in range(ctx.getChildCount()):
            print(f"Child {i}: {ctx.getChild(i).getText()}")

        #verifica si falta punto y coma
        if ctx.getChild(ctx.getChildCount() - 1).getText() != ';':
            print('Error: Falta un punto y coma en la declaracion')

        #Busco si la variable ya fue declarada
        if not(self.tablaSimbolos.buscarLocal(nombre_var)):
            nuevaVar = Variable(nombre_var, tipo_dato)
            #self.tablaSimbolos.agregar(nuevaVar)
            print('Nuevo simbolo agregado')
        else:
            print('Error: Variable ya declarada')
            #self.errores.write('Error: Variable ya declarada')
        
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
        
    
    def enterAsignacion(self, ctx):
        print("Inicio de asignacion")
        
        
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        print("Fin de asignacion")
        nombre_var = ctx.getChild(0).getText()


        variable = self.tablaSimbolos.buscar(nombre_var)

        if variable == False:
            print ('Error: Variable no declarada, no se puede asignar')
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

    
    
    #def enterFactor(self, ctx: compiladoresParser.FactorContext):
    #    print("Inicio de factor")
    
                
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
            
                if var is not None:
                    # Verificar si la variable ha sido inicializada
                    if not var.getInicializado():
                        print(f"ERROR: La variable {nombre} no está inicializada.\n")
                        return
                
                    # Agregar variable a las asignaciones y marcar como accedida
                    self.listaVariables.append({'tipo': var.getTipo(), 'nombre': var.getNombre()})
                    var.setAccedido()
                else:
                    print(f"ERROR: La variable {nombre} no está declarada.\n")
                    return
            
                # Actualizar variable en la tabla de símbolos
                self.tablaSimbolos.actualizarId(var)
            else:
                # Si es una constante, agregar a las asignaciones
                self.listaVariables.append({'tipo': tipo, 'nombre': nombre})
            # Caso 2: Si el primer hijo tiene múltiples hijos, se considera una función
        else:
            
            func_nombre = primer_hijo.getChild(0).getText()
            func = self.tablaSimbolos.buscarID(func_nombre)
            if func is not None:
                # Agregar función a las asignaciones y marcar como accedida
                self.listaVariables.append({'tipo': func.getTipo(), 'nombre': func.getNombre()})
                func.setAccedido()
                self.tablaSimbolos.actualizarFuncion(func)
            else:
                print(f"ERROR: La función {func_nombre} no está declarada.\n")
                return
        
        # Actualizar función en la tabla de símbolos

    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Inicio de while")           
        
        
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        print("Fin de parametro")
        nombre_param = ctx.getChild(1).getText()
        tipo_param = ctx.getChild(0).getText()
        if ctx.getChildCount() != 0:
            self.listaParametros.append({'tipo': tipo_param, 'nombre': nombre_param})
        else:
            print("No hay parametros")
    
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        print("Fin de argumentos")
        nombre_arg = ctx.getChild(0).getText()
        if ctx.getChildCount() != 0:
            print("Hay argumentos")
            for var in TablaSimbolos.getSimbolos():
                if var.getNombre() == nombre_arg:
                    print("Variable encontrada")
                    self.listaArgumentos.append({'nombre': ctx.getChild(1).getText()})            
        else:
            print("No hay argumentos")
    
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        print("Fin de funcion")
        nombre_func = ctx.getChild(1).getText()
        tipo_func = ctx.getChild(0).getText()
        if(TablaSimbolos.buscarID(nombre_func) == None):
            funcion = Funcion(nombre_func, tipo_func, copy.deepcopy(self.listaParametros))
            TablaSimbolos.agregarID(funcion)
            print("Funcion agregada")
            self.listaParametros.clear()
            self.listaVariables.clear()
        else:
            print("Error: Funcion ya declarada")
    
            
    def exitUsofuncion(self, ctx:compiladoresParser.UsofuncionContext):
        if(TablaSimbolos.buscarID(ctx.getChild(0).getText()) == None):
            print("Error: Funcion no declarada")
        else:
            #Cuando encuentra la funcion tiene que verificar los argumentos
            argumentos = self.listaArgumentos
            listaLocalParametros = []
            for arg in argumentos:
                if arg.isdigit():
                    self.listaLocalParametros.append({'nombre': arg, 'tipo': self.identify(arg)})
                else:
                    if(TablaSimbolos.buscarID(arg) != None):
                        self.listaLocalParametros.append(arg,TablaSimbolos.buscarID(arg).getTipo())
                    else:
                        print("Error: Argumento no declarado")
          
        for parametro in self.TablaSimbolos.buscarID(ctx.getChild(0).getText()).getParametros():
            if parametro['tipo'] !=  self.listaLocalParametros[parametro['tipo']]:
                print("WARNNING: El argumento " + parametro['nombre'] + " es de tipo " + parametro['tipo'] + ". Se espera un argumento de tipo "+ self.listaLocalParametros[parametro['tipo']] + ".\n")
        self.TablaSimbolos.actualizarFuncion(ctx.getChild(0).getText())
        ctx.getChild(0).setAccedido()
        self.listaVariables.clear()
    
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
    