from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class Walker (compiladoresVisitor):
    _temporales = []
    _etiquetas = []
    generador_temporales = Temporales()
    generador_etiquetas = Etiquetas()
    isFuncion = 0
    inFuncion = 0

    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Generando codigo intermedio".center(40, "*"))
        self.f = open("./output/CodigoIntermedio.txt", "w")

        self.visitInstrucciones(ctx.getChild(0))

        self.f.close()
        print("Codigo intermedio generado".center(40, "*"))

    def visitInstrucciones(self, ctx: compiladoresParser.InstruccionContext):
        self.visitInstruccion(ctx.getChild(0))

        if ctx.getChild(1).getChildCount() != 0:
            self.visitInstrucciones(ctx.getChild(1))

        return

