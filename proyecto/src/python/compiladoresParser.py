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
        4,1,16,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,28,8,0,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,37,8,2,1,3,1,3,1,3,3,3,42,8,3,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,0,0,7,0,2,
        4,6,8,10,12,0,0,56,0,27,1,0,0,0,2,29,1,0,0,0,4,36,1,0,0,0,6,41,1,
        0,0,0,8,43,1,0,0,0,10,47,1,0,0,0,12,52,1,0,0,0,14,15,5,16,0,0,15,
        16,6,0,-1,0,16,28,3,0,0,0,17,18,5,9,0,0,18,19,6,0,-1,0,19,28,3,0,
        0,0,20,21,5,15,0,0,21,22,6,0,-1,0,22,28,3,0,0,0,23,24,5,11,0,0,24,
        25,6,0,-1,0,25,28,3,0,0,0,26,28,5,0,0,1,27,14,1,0,0,0,27,17,1,0,
        0,0,27,20,1,0,0,0,27,23,1,0,0,0,27,26,1,0,0,0,28,1,1,0,0,0,29,30,
        3,4,2,0,30,31,5,0,0,1,31,3,1,0,0,0,32,33,3,6,3,0,33,34,3,4,2,0,34,
        37,1,0,0,0,35,37,1,0,0,0,36,32,1,0,0,0,36,35,1,0,0,0,37,5,1,0,0,
        0,38,42,3,8,4,0,39,42,3,10,5,0,40,42,3,12,6,0,41,38,1,0,0,0,41,39,
        1,0,0,0,41,40,1,0,0,0,42,7,1,0,0,0,43,44,5,10,0,0,44,45,5,16,0,0,
        45,46,5,6,0,0,46,9,1,0,0,0,47,48,5,11,0,0,48,49,5,2,0,0,49,50,5,
        16,0,0,50,51,5,3,0,0,51,11,1,0,0,0,52,53,5,4,0,0,53,54,3,4,2,0,54,
        55,5,5,0,0,55,13,1,0,0,0,3,27,36,41
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "';'", "'='", "'=='", "<INVALID>", "'int'", "'while'", 
                     "'for'", "'if'" ]

    symbolicNames = [ "<INVALID>", "INST", "PA", "PC", "LLA", "LLC", "PYC", 
                      "ASIG", "IGUAL", "NUMERO", "INT", "WHILE", "FOR", 
                      "IF", "WS", "OTRO", "ID" ]

    RULE_s = 0
    RULE_programa = 1
    RULE_instrucciones = 2
    RULE_instruccion = 3
    RULE_declaracion = 4
    RULE_iwhile = 5
    RULE_bloque = 6

    ruleNames =  [ "s", "programa", "instrucciones", "instruccion", "declaracion", 
                   "iwhile", "bloque" ]

    EOF = Token.EOF
    INST=1
    PA=2
    PC=3
    LLA=4
    LLC=5
    PYC=6
    ASIG=7
    IGUAL=8
    NUMERO=9
    INT=10
    WHILE=11
    FOR=12
    IF=13
    WS=14
    OTRO=15
    ID=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._NUMERO = None # Token
            self._OTRO = None # Token
            self._WHILE = None # Token

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def s(self):
            return self.getTypedRuleContext(compiladoresParser.SContext,0)


        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def OTRO(self):
            return self.getToken(compiladoresParser.OTRO, 0)

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = compiladoresParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                localctx._ID = self.match(compiladoresParser.ID)
                print("ID ->" + (None if localctx._ID is None else localctx._ID.text) + "<--") 
                self.state = 16
                self.s()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                localctx._NUMERO = self.match(compiladoresParser.NUMERO)
                print("NUMERO ->" + (None if localctx._NUMERO is None else localctx._NUMERO.text) + "<--") 
                self.state = 19
                self.s()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                localctx._OTRO = self.match(compiladoresParser.OTRO)
                print("Otro ->" + (None if localctx._OTRO is None else localctx._OTRO.text) + "<--") 
                self.state = 22
                self.s()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                localctx._WHILE = self.match(compiladoresParser.WHILE)
                print("WHILE ->" + (None if localctx._WHILE is None else localctx._WHILE.text) + "<--") 
                self.state = 25
                self.s()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.match(compiladoresParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.instrucciones()
            self.state = 30
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
        self.enterRule(localctx, 4, self.RULE_instrucciones)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.instruccion()
                self.state = 33
                self.instrucciones()
                pass
            elif token in [-1, 5]:
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


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


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
        self.enterRule(localctx, 6, self.RULE_instruccion)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.declaracion()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.iwhile()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.bloque()
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
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(compiladoresParser.INT)
            self.state = 44
            self.match(compiladoresParser.ID)
            self.state = 45
            self.match(compiladoresParser.PYC)
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
        self.enterRule(localctx, 10, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(compiladoresParser.WHILE)
            self.state = 48
            self.match(compiladoresParser.PA)
            self.state = 49
            self.match(compiladoresParser.ID)
            self.state = 50
            self.match(compiladoresParser.PC)
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
        self.enterRule(localctx, 12, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(compiladoresParser.LLA)
            self.state = 53
            self.instrucciones()
            self.state = 54
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





