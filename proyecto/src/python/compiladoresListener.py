# Generated from /home/agustin/Desktop/DHS-Proyecto/proyecto/src/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#funcion.
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcion.
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#funcionreturn.
    def enterFuncionreturn(self, ctx:compiladoresParser.FuncionreturnContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcionreturn.
    def exitFuncionreturn(self, ctx:compiladoresParser.FuncionreturnContext):
        pass


    # Enter a parse tree produced by compiladoresParser#returnblock.
    def enterReturnblock(self, ctx:compiladoresParser.ReturnblockContext):
        pass

    # Exit a parse tree produced by compiladoresParser#returnblock.
    def exitReturnblock(self, ctx:compiladoresParser.ReturnblockContext):
        pass


    # Enter a parse tree produced by compiladoresParser#voidfuncion.
    def enterVoidfuncion(self, ctx:compiladoresParser.VoidfuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#voidfuncion.
    def exitVoidfuncion(self, ctx:compiladoresParser.VoidfuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#parametro.
    def enterParametro(self, ctx:compiladoresParser.ParametroContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametro.
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        pass


    # Enter a parse tree produced by compiladoresParser#parametros.
    def enterParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametros.
    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#usofuncion.
    def enterUsofuncion(self, ctx:compiladoresParser.UsofuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#usofuncion.
    def exitUsofuncion(self, ctx:compiladoresParser.UsofuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumentos.
    def enterArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumentos.
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumentosp.
    def enterArgumentosp(self, ctx:compiladoresParser.ArgumentospContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumentosp.
    def exitArgumentosp(self, ctx:compiladoresParser.ArgumentospContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tdato.
    def enterTdato(self, ctx:compiladoresParser.TdatoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tdato.
    def exitTdato(self, ctx:compiladoresParser.TdatoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opal.
    def enterOpal(self, ctx:compiladoresParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opal.
    def exitOpal(self, ctx:compiladoresParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comparadores.
    def enterComparadores(self, ctx:compiladoresParser.ComparadoresContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comparadores.
    def exitComparadores(self, ctx:compiladoresParser.ComparadoresContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lor.
    def enterLor(self, ctx:compiladoresParser.LorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lor.
    def exitLor(self, ctx:compiladoresParser.LorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lorp.
    def enterLorp(self, ctx:compiladoresParser.LorpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lorp.
    def exitLorp(self, ctx:compiladoresParser.LorpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#land.
    def enterLand(self, ctx:compiladoresParser.LandContext):
        pass

    # Exit a parse tree produced by compiladoresParser#land.
    def exitLand(self, ctx:compiladoresParser.LandContext):
        pass


    # Enter a parse tree produced by compiladoresParser#landp.
    def enterLandp(self, ctx:compiladoresParser.LandpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#landp.
    def exitLandp(self, ctx:compiladoresParser.LandpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comp.
    def enterComp(self, ctx:compiladoresParser.CompContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comp.
    def exitComp(self, ctx:compiladoresParser.CompContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#e.
    def enterE(self, ctx:compiladoresParser.EContext):
        pass

    # Exit a parse tree produced by compiladoresParser#e.
    def exitE(self, ctx:compiladoresParser.EContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#t.
    def enterT(self, ctx:compiladoresParser.TContext):
        pass

    # Exit a parse tree produced by compiladoresParser#t.
    def exitT(self, ctx:compiladoresParser.TContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iif.
    def enterIif(self, ctx:compiladoresParser.IifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iif.
    def exitIif(self, ctx:compiladoresParser.IifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ielse.
    def enterIelse(self, ctx:compiladoresParser.IelseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ielse.
    def exitIelse(self, ctx:compiladoresParser.IelseContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ido.
    def enterIdo(self, ctx:compiladoresParser.IdoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ido.
    def exitIdo(self, ctx:compiladoresParser.IdoContext):
        pass



del compiladoresParser