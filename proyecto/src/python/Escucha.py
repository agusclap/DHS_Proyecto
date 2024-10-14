from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser

class Escucha (compiladoresListener):
    numTokens = 0
    numNodos = 0

    
     # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienzo de la compilacion')

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Fin de la compilacion')
        print("\tSe encontraron")
        print("\tNodos: " + str(self.numNodos))
        print("\tTokens: " + str(self.numTokens))
        
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Encontre WHILE")
        print("\tCantidad hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("FIN DEL WHILE")
        print("\tCantidad hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
    
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("### Declaracion")

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("Nombre variable: " + ctx.getChild(1).getText())
    
    def visitTerminal(self, node: TerminalNode):
        #print("-----> Token: " + node.getText())
        self.numTokens += 1
    
    def visitErrorNode(self, node: ErrorNode):
        print("-----> Error")
    
    def enterEveryRule(self, ctx):
        self.numNodos += 1