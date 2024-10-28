from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Estructuras.TablaSimbolos import TablaSimbolos
from Estructuras.Id import Variable

class Escucha (compiladoresListener):
    numTokens = 0
    numNodos = 0
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
        variable = self.tablaSimbolos.buscarLocal(nombre_var)
        
        if variable is None:
            print('Error: Variable no declarada')
            #self.errores.write('Error: Variable no declarada')
        else:
            variable.setInicializado() # ME tira error aca ver
            print('Variable asignada')
            
    
    
    
    
    
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