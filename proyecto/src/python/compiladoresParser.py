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
        4,1,37,293,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,0,5,0,74,8,0,10,0,12,0,77,9,0,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,
        95,8,3,1,4,1,4,1,4,1,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,3,6,113,8,6,1,7,1,7,1,7,1,7,1,7,3,7,120,8,7,1,8,1,8,1,
        8,1,8,3,8,126,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,137,8,
        9,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,155,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,174,8,
        17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,184,8,19,1,20,1,
        20,1,20,1,20,1,20,3,20,191,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,3,22,205,8,22,1,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,223,
        8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,232,8,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,269,8,29,1,30,1,30,3,30,
        273,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,
        285,8,31,1,32,1,32,1,32,1,32,3,32,291,8,32,1,32,0,0,33,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,64,0,3,3,0,23,24,26,26,34,34,1,0,23,24,2,0,14,14,
        16,20,293,0,69,1,0,0,0,2,80,1,0,0,0,4,82,1,0,0,0,6,94,1,0,0,0,8,
        101,1,0,0,0,10,103,1,0,0,0,12,112,1,0,0,0,14,119,1,0,0,0,16,125,
        1,0,0,0,18,136,1,0,0,0,20,138,1,0,0,0,22,142,1,0,0,0,24,154,1,0,
        0,0,26,156,1,0,0,0,28,161,1,0,0,0,30,163,1,0,0,0,32,165,1,0,0,0,
        34,173,1,0,0,0,36,175,1,0,0,0,38,183,1,0,0,0,40,190,1,0,0,0,42,192,
        1,0,0,0,44,204,1,0,0,0,46,206,1,0,0,0,48,222,1,0,0,0,50,231,1,0,
        0,0,52,233,1,0,0,0,54,241,1,0,0,0,56,245,1,0,0,0,58,268,1,0,0,0,
        60,272,1,0,0,0,62,274,1,0,0,0,64,290,1,0,0,0,66,68,3,24,12,0,67,
        66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,75,1,0,0,
        0,71,69,1,0,0,0,72,74,3,4,2,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,
        1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,0,0,1,
        79,1,1,0,0,0,80,81,7,0,0,0,81,3,1,0,0,0,82,83,3,2,1,0,83,84,5,35,
        0,0,84,85,5,1,0,0,85,86,3,6,3,0,86,87,5,2,0,0,87,88,3,54,27,0,88,
        5,1,0,0,0,89,90,3,22,11,0,90,91,5,35,0,0,91,92,3,8,4,0,92,95,1,0,
        0,0,93,95,1,0,0,0,94,89,1,0,0,0,94,93,1,0,0,0,95,7,1,0,0,0,96,97,
        5,21,0,0,97,98,3,6,3,0,98,99,3,8,4,0,99,102,1,0,0,0,100,102,1,0,
        0,0,101,96,1,0,0,0,101,100,1,0,0,0,102,9,1,0,0,0,103,104,5,35,0,
        0,104,105,5,1,0,0,105,106,3,12,6,0,106,107,5,2,0,0,107,11,1,0,0,
        0,108,109,3,28,14,0,109,110,3,14,7,0,110,113,1,0,0,0,111,113,1,0,
        0,0,112,108,1,0,0,0,112,111,1,0,0,0,113,13,1,0,0,0,114,115,5,21,
        0,0,115,116,3,12,6,0,116,117,3,14,7,0,117,120,1,0,0,0,118,120,1,
        0,0,0,119,114,1,0,0,0,119,118,1,0,0,0,120,15,1,0,0,0,121,122,3,18,
        9,0,122,123,3,16,8,0,123,126,1,0,0,0,124,126,1,0,0,0,125,121,1,0,
        0,0,125,124,1,0,0,0,126,17,1,0,0,0,127,137,3,24,12,0,128,137,3,52,
        26,0,129,137,3,56,28,0,130,137,3,62,31,0,131,137,3,54,27,0,132,137,
        3,26,13,0,133,137,3,10,5,0,134,137,3,20,10,0,135,137,5,5,0,0,136,
        127,1,0,0,0,136,128,1,0,0,0,136,129,1,0,0,0,136,130,1,0,0,0,136,
        131,1,0,0,0,136,132,1,0,0,0,136,133,1,0,0,0,136,134,1,0,0,0,136,
        135,1,0,0,0,137,19,1,0,0,0,138,139,5,32,0,0,139,140,3,28,14,0,140,
        141,5,5,0,0,141,21,1,0,0,0,142,143,7,1,0,0,143,23,1,0,0,0,144,145,
        3,22,11,0,145,146,5,35,0,0,146,147,5,5,0,0,147,155,1,0,0,0,148,149,
        3,22,11,0,149,150,5,35,0,0,150,151,5,15,0,0,151,152,3,28,14,0,152,
        153,5,5,0,0,153,155,1,0,0,0,154,144,1,0,0,0,154,148,1,0,0,0,155,
        25,1,0,0,0,156,157,5,35,0,0,157,158,5,15,0,0,158,159,3,28,14,0,159,
        160,5,5,0,0,160,27,1,0,0,0,161,162,3,32,16,0,162,29,1,0,0,0,163,
        164,7,2,0,0,164,31,1,0,0,0,165,166,3,36,18,0,166,167,3,34,17,0,167,
        33,1,0,0,0,168,169,5,12,0,0,169,170,3,36,18,0,170,171,3,34,17,0,
        171,174,1,0,0,0,172,174,1,0,0,0,173,168,1,0,0,0,173,172,1,0,0,0,
        174,35,1,0,0,0,175,176,3,40,20,0,176,177,3,38,19,0,177,37,1,0,0,
        0,178,179,5,11,0,0,179,180,3,40,20,0,180,181,3,38,19,0,181,184,1,
        0,0,0,182,184,1,0,0,0,183,178,1,0,0,0,183,182,1,0,0,0,184,39,1,0,
        0,0,185,186,3,42,21,0,186,187,3,30,15,0,187,188,3,42,21,0,188,191,
        1,0,0,0,189,191,3,42,21,0,190,185,1,0,0,0,190,189,1,0,0,0,191,41,
        1,0,0,0,192,193,3,46,23,0,193,194,3,44,22,0,194,43,1,0,0,0,195,196,
        5,6,0,0,196,197,3,46,23,0,197,198,3,44,22,0,198,205,1,0,0,0,199,
        200,5,7,0,0,200,201,3,46,23,0,201,202,3,44,22,0,202,205,1,0,0,0,
        203,205,1,0,0,0,204,195,1,0,0,0,204,199,1,0,0,0,204,203,1,0,0,0,
        205,45,1,0,0,0,206,207,3,50,25,0,207,208,3,48,24,0,208,47,1,0,0,
        0,209,210,5,8,0,0,210,211,3,50,25,0,211,212,3,48,24,0,212,223,1,
        0,0,0,213,214,5,9,0,0,214,215,3,50,25,0,215,216,3,48,24,0,216,223,
        1,0,0,0,217,218,5,10,0,0,218,219,3,50,25,0,219,220,3,48,24,0,220,
        223,1,0,0,0,221,223,1,0,0,0,222,209,1,0,0,0,222,213,1,0,0,0,222,
        217,1,0,0,0,222,221,1,0,0,0,223,49,1,0,0,0,224,232,5,22,0,0,225,
        232,5,35,0,0,226,232,3,10,5,0,227,228,5,1,0,0,228,229,3,42,21,0,
        229,230,5,2,0,0,230,232,1,0,0,0,231,224,1,0,0,0,231,225,1,0,0,0,
        231,226,1,0,0,0,231,227,1,0,0,0,232,51,1,0,0,0,233,234,5,28,0,0,
        234,235,5,1,0,0,235,236,3,28,14,0,236,237,5,2,0,0,237,238,5,3,0,
        0,238,239,3,16,8,0,239,240,5,4,0,0,240,53,1,0,0,0,241,242,5,3,0,
        0,242,243,3,16,8,0,243,244,5,4,0,0,244,55,1,0,0,0,245,246,5,29,0,
        0,246,247,5,1,0,0,247,248,3,58,29,0,248,249,5,5,0,0,249,250,3,60,
        30,0,250,251,5,5,0,0,251,252,3,28,14,0,252,253,5,2,0,0,253,254,3,
        18,9,0,254,57,1,0,0,0,255,256,5,35,0,0,256,257,5,15,0,0,257,269,
        3,28,14,0,258,269,5,35,0,0,259,260,3,22,11,0,260,261,5,35,0,0,261,
        269,1,0,0,0,262,263,3,22,11,0,263,264,5,35,0,0,264,265,5,15,0,0,
        265,266,3,28,14,0,266,269,1,0,0,0,267,269,1,0,0,0,268,255,1,0,0,
        0,268,258,1,0,0,0,268,259,1,0,0,0,268,262,1,0,0,0,268,267,1,0,0,
        0,269,59,1,0,0,0,270,273,3,28,14,0,271,273,1,0,0,0,272,270,1,0,0,
        0,272,271,1,0,0,0,273,61,1,0,0,0,274,275,5,30,0,0,275,276,5,1,0,
        0,276,277,3,28,14,0,277,278,5,2,0,0,278,279,5,3,0,0,279,280,3,18,
        9,0,280,281,5,5,0,0,281,284,5,4,0,0,282,285,1,0,0,0,283,285,3,64,
        32,0,284,282,1,0,0,0,284,283,1,0,0,0,285,63,1,0,0,0,286,287,5,31,
        0,0,287,291,3,54,27,0,288,289,5,31,0,0,289,291,3,18,9,0,290,286,
        1,0,0,0,290,288,1,0,0,0,291,65,1,0,0,0,19,69,75,94,101,112,119,125,
        136,154,173,183,190,204,222,231,268,272,284,290
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'^'", 
                     "'=!'", "'='", "'=='", "'>'", "'<'", "'<='", "'>='", 
                     "','", "<INVALID>", "'int'", "'double'", "'long'", 
                     "'char'", "'string'", "'while'", "'for'", "'if'", "'else'", 
                     "'return'", "'do'", "'void'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "SUMA", 
                      "RESTA", "MULT", "DIV", "MOD", "AND", "OR", "ORX", 
                      "DIF", "ASIG", "IGUAL", "MAYOR", "MENOR", "MENORIG", 
                      "MAYORIG", "COMA", "NUMERO", "INT", "DOUBLE", "LONG", 
                      "CHAR", "STRING", "WHILE", "FOR", "IF", "ELSE", "RETURN", 
                      "DO", "VOID", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_tfuncion = 1
    RULE_funcion = 2
    RULE_parametro = 3
    RULE_parametros = 4
    RULE_usofuncion = 5
    RULE_argumentos = 6
    RULE_argumentosp = 7
    RULE_instrucciones = 8
    RULE_instruccion = 9
    RULE_return = 10
    RULE_tdato = 11
    RULE_declaracion = 12
    RULE_asignacion = 13
    RULE_opal = 14
    RULE_comparadores = 15
    RULE_lor = 16
    RULE_lorp = 17
    RULE_land = 18
    RULE_landp = 19
    RULE_comp = 20
    RULE_exp = 21
    RULE_e = 22
    RULE_term = 23
    RULE_t = 24
    RULE_factor = 25
    RULE_iwhile = 26
    RULE_bloque = 27
    RULE_ifor = 28
    RULE_init = 29
    RULE_cond = 30
    RULE_iif = 31
    RULE_ielse = 32

    ruleNames =  [ "programa", "tfuncion", "funcion", "parametro", "parametros", 
                   "usofuncion", "argumentos", "argumentosp", "instrucciones", 
                   "instruccion", "return", "tdato", "declaracion", "asignacion", 
                   "opal", "comparadores", "lor", "lorp", "land", "landp", 
                   "comp", "exp", "e", "term", "t", "factor", "iwhile", 
                   "bloque", "ifor", "init", "cond", "iif", "ielse" ]

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
    AND=11
    OR=12
    ORX=13
    DIF=14
    ASIG=15
    IGUAL=16
    MAYOR=17
    MENOR=18
    MENORIG=19
    MAYORIG=20
    COMA=21
    NUMERO=22
    INT=23
    DOUBLE=24
    LONG=25
    CHAR=26
    STRING=27
    WHILE=28
    FOR=29
    IF=30
    ELSE=31
    RETURN=32
    DO=33
    VOID=34
    ID=35
    WS=36
    OTRO=37

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

        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,i)


        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.FuncionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.FuncionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.declaracion() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17272143872) != 0):
                self.state = 72
                self.funcion()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TfuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(compiladoresParser.CHAR, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tfuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTfuncion" ):
                listener.enterTfuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTfuncion" ):
                listener.exitTfuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTfuncion" ):
                return visitor.visitTfuncion(self)
            else:
                return visitor.visitChildren(self)




    def tfuncion(self):

        localctx = compiladoresParser.TfuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tfuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17272143872) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tfuncion(self):
            return self.getTypedRuleContext(compiladoresParser.TfuncionContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def parametro(self):
            return self.getTypedRuleContext(compiladoresParser.ParametroContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compiladoresParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.tfuncion()
            self.state = 83
            self.match(compiladoresParser.ID)
            self.state = 84
            self.match(compiladoresParser.PA)
            self.state = 85
            self.parametro()
            self.state = 86
            self.match(compiladoresParser.PC)
            self.state = 87
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = compiladoresParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parametro)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.tdato()
                self.state = 90
                self.match(compiladoresParser.ID)
                self.state = 91
                self.parametros()
                pass
            elif token in [2, 21]:
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


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def parametro(self):
            return self.getTypedRuleContext(compiladoresParser.ParametroContext,0)


        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compiladoresParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parametros)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(compiladoresParser.COMA)
                self.state = 97
                self.parametro()
                self.state = 98
                self.parametros()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsofuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_usofuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsofuncion" ):
                listener.enterUsofuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsofuncion" ):
                listener.exitUsofuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsofuncion" ):
                return visitor.visitUsofuncion(self)
            else:
                return visitor.visitChildren(self)




    def usofuncion(self):

        localctx = compiladoresParser.UsofuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_usofuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(compiladoresParser.ID)
            self.state = 104
            self.match(compiladoresParser.PA)

            self.state = 105
            self.argumentos()
            self.state = 106
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def argumentosp(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compiladoresParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argumentos)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.opal()
                self.state = 109
                self.argumentosp()
                pass
            elif token in [2, 21]:
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


    class ArgumentospContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def argumentosp(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argumentosp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentosp" ):
                listener.enterArgumentosp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentosp" ):
                listener.exitArgumentosp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentosp" ):
                return visitor.visitArgumentosp(self)
            else:
                return visitor.visitChildren(self)




    def argumentosp(self):

        localctx = compiladoresParser.ArgumentospContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_argumentosp)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(compiladoresParser.COMA)
                self.state = 115
                self.argumentos()
                self.state = 116
                self.argumentosp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
        self.enterRule(localctx, 16, self.RULE_instrucciones)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5, 23, 24, 28, 29, 30, 32, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.instruccion()
                self.state = 122
                self.instrucciones()
                pass
            elif token in [4]:
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


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def return_(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnContext,0)


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
        self.enterRule(localctx, 18, self.RULE_instruccion)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.ifor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.iif()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.bloque()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.asignacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 133
                self.usofuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 134
                self.return_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 135
                self.match(compiladoresParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = compiladoresParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(compiladoresParser.RETURN)
            self.state = 139
            self.opal()
            self.state = 140
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TdatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tdato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTdato" ):
                listener.enterTdato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTdato" ):
                listener.exitTdato(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTdato" ):
                return visitor.visitTdato(self)
            else:
                return visitor.visitChildren(self)




    def tdato(self):

        localctx = compiladoresParser.TdatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tdato)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


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
        self.enterRule(localctx, 24, self.RULE_declaracion)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.tdato()
                self.state = 145
                self.match(compiladoresParser.ID)
                self.state = 146
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.tdato()
                self.state = 149
                self.match(compiladoresParser.ID)
                self.state = 150
                self.match(compiladoresParser.ASIG)
                self.state = 151
                self.opal()
                self.state = 152
                self.match(compiladoresParser.PYC)
                pass


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


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

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
        self.enterRule(localctx, 26, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(compiladoresParser.ID)
            self.state = 157
            self.match(compiladoresParser.ASIG)
            self.state = 158
            self.opal()
            self.state = 159
            self.match(compiladoresParser.PYC)
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

        def lor(self):
            return self.getTypedRuleContext(compiladoresParser.LorContext,0)


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
        self.enterRule(localctx, 28, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.lor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAYOR(self):
            return self.getToken(compiladoresParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(compiladoresParser.MENOR, 0)

        def IGUAL(self):
            return self.getToken(compiladoresParser.IGUAL, 0)

        def MENORIG(self):
            return self.getToken(compiladoresParser.MENORIG, 0)

        def MAYORIG(self):
            return self.getToken(compiladoresParser.MAYORIG, 0)

        def DIF(self):
            return self.getToken(compiladoresParser.DIF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_comparadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparadores" ):
                listener.enterComparadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparadores" ):
                listener.exitComparadores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparadores" ):
                return visitor.visitComparadores(self)
            else:
                return visitor.visitChildren(self)




    def comparadores(self):

        localctx = compiladoresParser.ComparadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2048000) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def lorp(self):
            return self.getTypedRuleContext(compiladoresParser.LorpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLor" ):
                listener.enterLor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLor" ):
                listener.exitLor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLor" ):
                return visitor.visitLor(self)
            else:
                return visitor.visitChildren(self)




    def lor(self):

        localctx = compiladoresParser.LorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.land()
            self.state = 166
            self.lorp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LorpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def lorp(self):
            return self.getTypedRuleContext(compiladoresParser.LorpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lorp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLorp" ):
                listener.enterLorp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLorp" ):
                listener.exitLorp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLorp" ):
                return visitor.visitLorp(self)
            else:
                return visitor.visitChildren(self)




    def lorp(self):

        localctx = compiladoresParser.LorpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lorp)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(compiladoresParser.OR)
                self.state = 169
                self.land()
                self.state = 170
                self.lorp()
                pass
            elif token in [2, 5, 21]:
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


    class LandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def landp(self):
            return self.getTypedRuleContext(compiladoresParser.LandpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_land

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLand" ):
                listener.enterLand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLand" ):
                listener.exitLand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLand" ):
                return visitor.visitLand(self)
            else:
                return visitor.visitChildren(self)




    def land(self):

        localctx = compiladoresParser.LandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_land)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.comp()
            self.state = 176
            self.landp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LandpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def landp(self):
            return self.getTypedRuleContext(compiladoresParser.LandpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_landp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLandp" ):
                listener.enterLandp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLandp" ):
                listener.exitLandp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLandp" ):
                return visitor.visitLandp(self)
            else:
                return visitor.visitChildren(self)




    def landp(self):

        localctx = compiladoresParser.LandpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_landp)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(compiladoresParser.AND)
                self.state = 179
                self.comp()
                self.state = 180
                self.landp()
                pass
            elif token in [2, 5, 12, 21]:
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


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ExpContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ExpContext,i)


        def comparadores(self):
            return self.getTypedRuleContext(compiladoresParser.ComparadoresContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)




    def comp(self):

        localctx = compiladoresParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comp)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.exp()
                self.state = 186
                self.comparadores()
                self.state = 187
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.exp()
                pass


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
        self.enterRule(localctx, 42, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.term()
            self.state = 193
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
        self.enterRule(localctx, 44, self.RULE_e)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(compiladoresParser.SUMA)
                self.state = 196
                self.term()
                self.state = 197
                self.e()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(compiladoresParser.RESTA)
                self.state = 200
                self.term()
                self.state = 201
                self.e()
                pass
            elif token in [2, 5, 11, 12, 14, 16, 17, 18, 19, 20, 21]:
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
        self.enterRule(localctx, 46, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.factor()
            self.state = 207
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
        self.enterRule(localctx, 48, self.RULE_t)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(compiladoresParser.MULT)
                self.state = 210
                self.factor()
                self.state = 211
                self.t()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(compiladoresParser.DIV)
                self.state = 214
                self.factor()
                self.state = 215
                self.t()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.match(compiladoresParser.MOD)
                self.state = 218
                self.factor()
                self.state = 219
                self.t()
                pass
            elif token in [2, 5, 6, 7, 11, 12, 14, 16, 17, 18, 19, 20, 21]:
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

        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


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
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.usofuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self.match(compiladoresParser.PA)
                self.state = 228
                self.exp()
                self.state = 229
                self.match(compiladoresParser.PC)
                pass


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

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

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
        self.enterRule(localctx, 52, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(compiladoresParser.WHILE)
            self.state = 234
            self.match(compiladoresParser.PA)
            self.state = 235
            self.opal()
            self.state = 236
            self.match(compiladoresParser.PC)
            self.state = 237
            self.match(compiladoresParser.LLA)
            self.state = 238
            self.instrucciones()
            self.state = 239
            self.match(compiladoresParser.LLC)
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
        self.enterRule(localctx, 54, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(compiladoresParser.LLA)
            self.state = 242
            self.instrucciones()
            self.state = 243
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


        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


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
        self.enterRule(localctx, 56, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(compiladoresParser.FOR)
            self.state = 246
            self.match(compiladoresParser.PA)
            self.state = 247
            self.init()
            self.state = 248
            self.match(compiladoresParser.PYC)
            self.state = 249
            self.cond()
            self.state = 250
            self.match(compiladoresParser.PYC)
            self.state = 251
            self.opal()
            self.state = 252
            self.match(compiladoresParser.PC)
            self.state = 253
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

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


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
        self.enterRule(localctx, 58, self.RULE_init)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(compiladoresParser.ID)
                self.state = 256
                self.match(compiladoresParser.ASIG)
                self.state = 257
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.tdato()
                self.state = 260
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.tdato()
                self.state = 263
                self.match(compiladoresParser.ID)
                self.state = 264
                self.match(compiladoresParser.ASIG)
                self.state = 265
                self.opal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


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

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


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
        self.enterRule(localctx, 60, self.RULE_cond)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.opal()
                pass
            elif token in [5]:
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


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def ielse(self):
            return self.getTypedRuleContext(compiladoresParser.IelseContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladoresParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(compiladoresParser.IF)
            self.state = 275
            self.match(compiladoresParser.PA)
            self.state = 276
            self.opal()
            self.state = 277
            self.match(compiladoresParser.PC)
            self.state = 278
            self.match(compiladoresParser.LLA)
            self.state = 279
            self.instruccion()
            self.state = 280
            self.match(compiladoresParser.PYC)
            self.state = 281
            self.match(compiladoresParser.LLC)
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 23, 24, 28, 29, 30, 32, 35]:
                pass
            elif token in [31]:
                self.state = 283
                self.ielse()
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


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladoresParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ielse)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(compiladoresParser.ELSE)
                self.state = 287
                self.bloque()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(compiladoresParser.ELSE)
                self.state = 289
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





