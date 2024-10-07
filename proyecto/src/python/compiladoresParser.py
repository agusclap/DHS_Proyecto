# Generated from /home/agustin/Desktop/DHS-Proyecto/proyecto/src/python/compiladores.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,42,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,74,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,92,8,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,100,8,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,136,8,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,149,8,16,1,16,0,
        0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,0,152,0,34,
        1,0,0,0,2,41,1,0,0,0,4,49,1,0,0,0,6,51,1,0,0,0,8,55,1,0,0,0,10,59,
        1,0,0,0,12,61,1,0,0,0,14,73,1,0,0,0,16,75,1,0,0,0,18,91,1,0,0,0,
        20,99,1,0,0,0,22,101,1,0,0,0,24,107,1,0,0,0,26,111,1,0,0,0,28,121,
        1,0,0,0,30,135,1,0,0,0,32,148,1,0,0,0,34,35,3,2,1,0,35,36,5,0,0,
        1,36,1,1,0,0,0,37,38,3,4,2,0,38,39,3,2,1,0,39,42,1,0,0,0,40,42,1,
        0,0,0,41,37,1,0,0,0,41,40,1,0,0,0,42,3,1,0,0,0,43,50,3,6,3,0,44,
        50,3,22,11,0,45,50,3,26,13,0,46,50,3,24,12,0,47,50,3,8,4,0,48,50,
        5,5,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,1,0,0,0,
        49,47,1,0,0,0,49,48,1,0,0,0,50,5,1,0,0,0,51,52,5,18,0,0,52,53,5,
        22,0,0,53,54,5,5,0,0,54,7,1,0,0,0,55,56,5,22,0,0,56,57,5,11,0,0,
        57,58,3,10,5,0,58,9,1,0,0,0,59,60,3,12,6,0,60,11,1,0,0,0,61,62,3,
        16,8,0,62,63,3,14,7,0,63,13,1,0,0,0,64,65,5,6,0,0,65,66,3,16,8,0,
        66,67,3,14,7,0,67,74,1,0,0,0,68,69,5,7,0,0,69,70,3,16,8,0,70,71,
        3,14,7,0,71,74,1,0,0,0,72,74,1,0,0,0,73,64,1,0,0,0,73,68,1,0,0,0,
        73,72,1,0,0,0,74,15,1,0,0,0,75,76,3,20,10,0,76,77,3,18,9,0,77,17,
        1,0,0,0,78,79,5,8,0,0,79,80,3,20,10,0,80,81,3,18,9,0,81,92,1,0,0,
        0,82,83,5,9,0,0,83,84,3,20,10,0,84,85,3,18,9,0,85,92,1,0,0,0,86,
        87,5,10,0,0,87,88,3,20,10,0,88,89,3,18,9,0,89,92,1,0,0,0,90,92,1,
        0,0,0,91,78,1,0,0,0,91,82,1,0,0,0,91,86,1,0,0,0,91,90,1,0,0,0,92,
        19,1,0,0,0,93,100,5,17,0,0,94,100,5,22,0,0,95,96,5,1,0,0,96,97,3,
        12,6,0,97,98,5,2,0,0,98,100,1,0,0,0,99,93,1,0,0,0,99,94,1,0,0,0,
        99,95,1,0,0,0,100,21,1,0,0,0,101,102,5,19,0,0,102,103,5,1,0,0,103,
        104,5,22,0,0,104,105,5,2,0,0,105,106,3,4,2,0,106,23,1,0,0,0,107,
        108,5,3,0,0,108,109,3,2,1,0,109,110,5,4,0,0,110,25,1,0,0,0,111,112,
        5,20,0,0,112,113,5,1,0,0,113,114,3,28,14,0,114,115,5,5,0,0,115,116,
        3,30,15,0,116,117,5,5,0,0,117,118,3,32,16,0,118,119,5,2,0,0,119,
        120,3,4,2,0,120,27,1,0,0,0,121,122,3,8,4,0,122,29,1,0,0,0,123,124,
        5,22,0,0,124,125,5,14,0,0,125,136,5,17,0,0,126,127,5,22,0,0,127,
        128,5,13,0,0,128,136,5,17,0,0,129,130,5,22,0,0,130,131,5,16,0,0,
        131,136,5,17,0,0,132,133,5,22,0,0,133,134,5,15,0,0,134,136,5,17,
        0,0,135,123,1,0,0,0,135,126,1,0,0,0,135,129,1,0,0,0,135,132,1,0,
        0,0,136,31,1,0,0,0,137,138,5,22,0,0,138,139,5,6,0,0,139,149,5,6,
        0,0,140,141,5,6,0,0,141,142,5,6,0,0,142,149,5,22,0,0,143,144,5,22,
        0,0,144,145,5,7,0,0,145,149,5,7,0,0,146,147,5,7,0,0,147,149,5,7,
        0,0,148,137,1,0,0,0,148,140,1,0,0,0,148,143,1,0,0,0,148,146,1,0,
        0,0,149,33,1,0,0,0,7,41,49,73,91,99,135,148
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'=='", "'>'", "'<'", 
                     "'<='", "'>='", "<INVALID>", "'int'", "'while'", "'for'", 
                     "'if'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "SUMA", 
                      "RESTA", "MULT", "DIV", "MOD", "ASIG", "IGUAL", "MAYOR", 
                      "MENOR", "MENORIG", "MAYORIG", "NUMERO", "INT", "WHILE", 
                      "FOR", "IF", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_declaracion = 3
    RULE_asignacion = 4
    RULE_opal = 5
    RULE_exp = 6
    RULE_e = 7
    RULE_term = 8
    RULE_t = 9
    RULE_factor = 10
    RULE_iwhile = 11
    RULE_bloque = 12
    RULE_ifor = 13
    RULE_init = 14
    RULE_cond = 15
    RULE_iter = 16

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracion", 
                   "asignacion", "opal", "exp", "e", "term", "t", "factor", 
                   "iwhile", "bloque", "ifor", "init", "cond", "iter" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    SUMA=6
    RESTA=7
    MULT=8
    DIV=9
    MOD=10
    ASIG=11
    IGUAL=12
    MAYOR=13
    MENOR=14
    MENORIG=15
    MAYORIG=16
    NUMERO=17
    INT=18
    WHILE=19
    FOR=20
    IF=21
    ID=22
    WS=23
    OTRO=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.instrucciones()
            self.state = 35
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5, 18, 19, 20, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.instruccion()
                self.state = 38
                self.instrucciones()
                pass
            elif token in [-1, 4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.declaracion()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.iwhile()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.ifor()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.bloque()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.asignacion()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(compiladoresParser.PYC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(compiladoresParser.INT)
            self.state = 52
            self.match(compiladoresParser.ID)
            self.state = 53
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(compiladoresParser.ID)
            self.state = 56
            self.match(compiladoresParser.ASIG)
            self.state = 57
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladoresParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladoresParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.term()
            self.state = 62
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


        def RESTA(self):
            return self.getToken(compiladoresParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladoresParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_e)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(compiladoresParser.SUMA)
                self.state = 65
                self.term()
                self.state = 66
                self.e()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(compiladoresParser.RESTA)
                self.state = 69
                self.term()
                self.state = 70
                self.e()
                pass
            elif token in [-1, 2, 3, 4, 5, 18, 19, 20, 22]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.factor()
            self.state = 76
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladoresParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_t)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(compiladoresParser.MULT)
                self.state = 79
                self.factor()
                self.state = 80
                self.t()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(compiladoresParser.DIV)
                self.state = 83
                self.factor()
                self.state = 84
                self.t()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(compiladoresParser.MOD)
                self.state = 87
                self.factor()
                self.state = 88
                self.t()
                pass
            elif token in [-1, 2, 3, 4, 5, 6, 7, 18, 19, 20, 22]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_factor)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(compiladoresParser.ID)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.match(compiladoresParser.PA)
                self.state = 96
                self.exp()
                self.state = 97
                self.match(compiladoresParser.PC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladoresParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(compiladoresParser.WHILE)
            self.state = 102
            self.match(compiladoresParser.PA)
            self.state = 103
            self.match(compiladoresParser.ID)
            self.state = 104
            self.match(compiladoresParser.PC)
            self.state = 105
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(compiladoresParser.LLA)
            self.state = 108
            self.instrucciones()
            self.state = 109
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def init(self):
            return self.getTypedRuleContext(compiladoresParser.InitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def iter_(self):
            return self.getTypedRuleContext(compiladoresParser.IterContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladoresParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(compiladoresParser.FOR)
            self.state = 112
            self.match(compiladoresParser.PA)
            self.state = 113
            self.init()
            self.state = 114
            self.match(compiladoresParser.PYC)
            self.state = 115
            self.cond()
            self.state = 116
            self.match(compiladoresParser.PYC)
            self.state = 117
            self.iter_()
            self.state = 118
            self.match(compiladoresParser.PC)
            self.state = 119
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = compiladoresParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.asignacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def MENOR(self):
            return self.getToken(compiladoresParser.MENOR, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def MAYOR(self):
            return self.getToken(compiladoresParser.MAYOR, 0)

        def MAYORIG(self):
            return self.getToken(compiladoresParser.MAYORIG, 0)

        def MENORIG(self):
            return self.getToken(compiladoresParser.MENORIG, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = compiladoresParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cond)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(compiladoresParser.ID)
                self.state = 124
                self.match(compiladoresParser.MENOR)
                self.state = 125
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(compiladoresParser.ID)
                self.state = 127
                self.match(compiladoresParser.MAYOR)
                self.state = 128
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(compiladoresParser.ID)
                self.state = 130
                self.match(compiladoresParser.MAYORIG)
                self.state = 131
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(compiladoresParser.ID)
                self.state = 133
                self.match(compiladoresParser.MENORIG)
                self.state = 134
                self.match(compiladoresParser.NUMERO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def SUMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.SUMA)
            else:
                return self.getToken(compiladoresParser.SUMA, i)

        def RESTA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.RESTA)
            else:
                return self.getToken(compiladoresParser.RESTA, i)

        def getRuleIndex(self):
            return compiladoresParser.RULE_iter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIter" ):
                listener.enterIter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIter" ):
                listener.exitIter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIter" ):
                return visitor.visitIter(self)
            else:
                return visitor.visitChildren(self)




    def iter_(self):

        localctx = compiladoresParser.IterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_iter)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(compiladoresParser.ID)
                self.state = 138
                self.match(compiladoresParser.SUMA)
                self.state = 139
                self.match(compiladoresParser.SUMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(compiladoresParser.SUMA)
                self.state = 141
                self.match(compiladoresParser.SUMA)
                self.state = 142
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(compiladoresParser.ID)
                self.state = 144
                self.match(compiladoresParser.RESTA)
                self.state = 145
                self.match(compiladoresParser.RESTA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.match(compiladoresParser.RESTA)
                self.state = 147
                self.match(compiladoresParser.RESTA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





