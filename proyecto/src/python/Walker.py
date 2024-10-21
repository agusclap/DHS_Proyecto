from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class Walker (compiladoresVisitor):
    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("=-"*20)
        print("--> Comienza a caminar")
        return super().visitPrograma(ctx)
    def visitBloque(self, ctx: compiladoresParser.BloqueContext):
        print("Nuevo Contexto")
        #return super().visit(ctx)
        return super().visitInstrucciones(ctx.getChild(1))
    def visitTerminal(self, node):
        print("--> Token" + node.getText())
        return super().visitTerminal(node)

