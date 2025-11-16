from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser


class Walker(compiladoresVisitor):
    def __init__(self):
        super().__init__()
        # si más adelante querés usar temporales/etiquetas los agregamos acá
        self.f = None

    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Generando codigo intermedio".center(40, "*"))
        self.f = open("./output/CodigoIntermedio.txt", "w")

        # por ahora solo caminamos las instrucciones
        self.visitInstrucciones(ctx.getChild(0))

        self.f.close()
        print("Codigo intermedio generado".center(40, "*"))

    def visitInstrucciones(self, ctx: compiladoresParser.InstruccionesContext):
        # visitamos la primera instrucción
        self.visitInstruccion(ctx.getChild(0))

        # si hay más, recursión
        if ctx.getChild(1).getChildCount() != 0:
            self.visitInstrucciones(ctx.getChild(1))

        return
